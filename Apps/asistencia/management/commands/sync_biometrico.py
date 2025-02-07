# apps/asistencias/management/commands/sync_biometrico.py

from django.core.management.base import BaseCommand
from django.db.models import Min, Max, Case, When, DateTimeField
from django.db.models.functions import TruncDate
from django.db import transaction
from datetime import date, timedelta
import logging
from Apps.asistencia.models import RegistroAsistencia, CheckInOut, UserInfo
from Apps.permisos.models import Colaboradores
from Apps.roles.models import RolAsignado

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Sincroniza la asistencia desde la BD real (CHECKINOUT y USERINFO) con RegistroAsistencia"

    def handle(self, *args, **options):
        self.stdout.write("Iniciando sincronización con la BD real de biometría...")

        # 1. Definimos la ventana de tiempo para procesar
        ventana_dias = 5
        fecha_limite = date.today() - timedelta(days=ventana_dias)
        self.stdout.write(f"Procesando registros con fecha >= {fecha_limite}")

        # 2. Agrupamos las marcaciones de CHECKINOUT por usuario y día (una sola consulta)
        registros = (
            CheckInOut.objects.using('biometrico')
            .filter(checktime__date__gte=fecha_limite)
            .annotate(day=TruncDate('checktime'))
            .values('user_id', 'day')
            .annotate(
                entrada=Min(
                    Case(
                        When(checktype='I', then='checktime'),
                        output_field=DateTimeField()
                    )
                ),
                salida=Max(
                    Case(
                        When(checktype='O', then='checktime'),
                        output_field=DateTimeField()
                    )
                )
            )
            .order_by('day')
        )

        # Convertimos el QuerySet a lista (para iterar varias veces si hace falta)
        registros_list = list(registros)
        total = len(registros_list)
        self.stdout.write(f"Total registros agrupados en la ventana: {total}")

        if not registros_list:
            self.stdout.write("No hay registros que procesar.")
            return

        # 3. Extraemos los user_ids únicos
        user_ids = {r['user_id'] for r in registros_list}

        # 4. Obtenemos todos los UserInfo de una sola vez (diccionario: user_id -> UserInfo)
        userinfo_qs = UserInfo.objects.using('biometrico').filter(user_id__in=user_ids)
        userinfo_map = {u.user_id: u for u in userinfo_qs}

        # 5. De todos esos UserInfo, sacamos los SSN para buscar Colaboradores
        ssn_set = {u.ssn for u in userinfo_qs if u.ssn}  # ignoramos SSN vacío o None

        # 6. Obtenemos Colaboradores en una sola consulta (diccionario: ssn -> Colaboradores)
        colaboradores_qs = Colaboradores.objects.filter(
            codigocolaborador__in=ssn_set, estado='ACTIVO'
        )
        colaboradores_map = {c.codigocolaborador: c for c in colaboradores_qs}

        # 7. Hallar min_day y max_day en registros_list para traer roles y asistencias existentes
        #    (siempre que 'day' exista, en la ventana).
        fechas = [r['day'] for r in registros_list if r['day']]
        min_day, max_day = min(fechas), max(fechas)

        # 8. Traer en bloque las asignaciones de rol, para cada colaborador, dentro del rango [min_day, max_day]
        #    (diccionario: colaborador.id -> lista de RolAsignado)
        rol_asignado_qs = RolAsignado.objects.filter(
            colaborador__in=colaboradores_map.values(),
            estado='ACTIVO',
            fecha_inicio__lte=max_day,
            fecha_fin__gte=min_day
        ).select_related('rol', 'colaborador')

        from collections import defaultdict
        roles_por_colaborador = defaultdict(list)
        for ra in rol_asignado_qs:
            roles_por_colaborador[ra.colaborador_id].append(ra)

        # Pequeña función para obtener el rol que aplique a un día determinado
        def get_rol_para_fecha(colaborador_id, fecha):
            """ Retorna la instancia de rol si la fecha cae dentro de (ra.fecha_inicio, ra.fecha_fin). """
            if not roles_por_colaborador[colaborador_id]:
                return None
            for ra in roles_por_colaborador[colaborador_id]:
                if ra.fecha_inicio <= fecha <= ra.fecha_fin:
                    return ra.rol
            return None

        # 9. Cargar los registros de RegistroAsistencia existentes para no duplicarlos
        #    (diccionario clave (colaborador_id, fecha))
        asistencias_existentes = RegistroAsistencia.objects.filter(
            colaborador__in=colaboradores_map.values(),
            fecha__range=[min_day, max_day]
        )
        asistencia_map = {
            (a.colaborador_id, a.fecha): a
            for a in asistencias_existentes
        }

        creados = 0
        actualizados = 0
        omitidos = 0

        # 10. Usar una transacción para agrupar las operaciones en BD
        with transaction.atomic():
            for rec in registros_list:
                user_id = rec['user_id']
                day = rec['day']
                entrada_dt = rec['entrada']
                salida_dt = rec['salida']

                # Validaciones mínimas
                if not day or not entrada_dt:
                    # Sin fecha o sin marcación de entrada => se omite
                    omitidos += 1
                    continue

                # Buscar user_info en el diccionario
                user_info = userinfo_map.get(user_id)
                if not user_info or not user_info.ssn:
                    # UserInfo no encontrado o SSN vacío => se omite
                    omitidos += 1
                    continue

                # Buscar colaborador
                colaborador = colaboradores_map.get(user_info.ssn)
                if not colaborador:
                    # Colaborador no encontrado => se omite
                    omitidos += 1
                    continue

                # Resolver hora de salida: si no hay marcación real, buscamos la programada
                salida_final = None
                if salida_dt:
                    salida_final = salida_dt.time()
                else:
                    # Buscar rol asignado para ver si hay hora_fin configurada
                    rol_para_dia = get_rol_para_fecha(colaborador.id, day)
                    if rol_para_dia:
                        # Lunes=0 ... Domingo=6
                        dia_semana = day.weekday()
                        if dia_semana < 5:
                            salida_final = rol_para_dia.hora_fin_semana
                        elif dia_semana == 5:
                            salida_final = rol_para_dia.hora_fin_sabado
                        elif dia_semana == 6:
                            salida_final = rol_para_dia.hora_fin_domingo

                entrada_time = entrada_dt.time()
                rol_asig = get_rol_para_fecha(colaborador.id, day)

                # Verificar si ya existe la asistencia en ese (colaborador, fecha)
                asistencia = asistencia_map.get((colaborador.id, day))

                if asistencia:
                    # Actualizar
                    asistencia.hora_entrada = entrada_time
                    asistencia.hora_salida = salida_final
                    asistencia.rol = rol_asig
                    asistencia.save()  # dispara la lógica de .save() en el modelo
                    actualizados += 1
                else:
                    # Crear nuevo
                    nueva_asistencia = RegistroAsistencia(
                        colaborador=colaborador,
                        sucursal=colaborador.sucursal,
                        fecha=day,
                        hora_entrada=entrada_time,
                        hora_salida=salida_final,
                        rol=rol_asig
                    )
                    nueva_asistencia.save()  # dispara la lógica del modelo
                    # Lo guardamos en el map por si viene otra marcación del mismo día (raro, pero puede pasar)
                    asistencia_map[(colaborador.id, day)] = nueva_asistencia
                    creados += 1

        self.stdout.write(
            f"Sincronización completada. Creados: {creados}, Actualizados: {actualizados}, Omitidos: {omitidos}."
        )
