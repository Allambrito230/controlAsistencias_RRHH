# apps/asistencias/management/commands/sync_biometrico.py
from django.core.management.base import BaseCommand
from datetime import date, timedelta
import logging

from django.db.models import Min, Max, Case, When, DateTimeField
from django.db.models.functions import TruncDate

# Importamos nuestros modelos
from Apps.asistencia.models import RegistroAsistencia,CheckInOut, UserInfo
from Apps.permisos.models import Colaboradores
from Apps.roles.models import RolAsignado


logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Sincroniza la asistencia desde la BD real (CHECKINOUT y USERINFO) con RegistroAsistencia"

    def handle(self, *args, **options):
        self.stdout.write("Iniciando sincronización con la BD real de biometría...")

        # 1. Definimos la ventana de tiempo para procesar (por ejemplo, los últimos 2 días)
        ventana_dias = 1
        fecha_limite = date.today() - timedelta(days=ventana_dias)
        self.stdout.write(f"Procesando registros con fecha >= {fecha_limite}")

        # 2. Agrupamos las marcaciones de CHECKINOUT por usuario y día
        # Se asume que CHECKTYPE 'I' es para entrada y 'O' para salida.
        registros = (CheckInOut.objects.using('biometrico')
                     .filter(checktime__date__gte=fecha_limite)
                     .annotate(day=TruncDate('checktime'))
                     .values('user_id', 'day')
                     .annotate(
                         entrada=Min(Case(
                             When(checktype='I', then='checktime'),
                             output_field=DateTimeField()
                         )),
                         salida=Max(Case(
                             When(checktype='O', then='checktime'),
                             output_field=DateTimeField()
                         ))
                     )
                     .order_by('day'))
        total = registros.count()
        self.stdout.write(f"Total registros agrupados en la ventana: {total}")

        # Contadores para log
        creados = 0
        actualizados = 0
        omitidos = 0

        # 3. Procesamos cada grupo (por usuario y día)
        for rec in registros:
            try:
                user_id = rec['user_id']
                day = rec['day']  # Este es un objeto date
                entrada_dt = rec['entrada']  # Es un datetime o None
                salida_dt = rec['salida']      # Es un datetime o None

                if not entrada_dt:
                    self.stdout.write(f"Usuario {user_id} en {day} no tiene marcación de entrada; se omite.")
                    omitidos += 1
                    continue

                # 4. Obtenemos la información del empleado desde USERINFO usando el user_id
                try:
                    user_info = UserInfo.objects.using('biometrico').get(user_id=user_id)
                except UserInfo.DoesNotExist:
                    self.stdout.write(f"Usuario con ID {user_id} no existe en USERINFO; se omite.")
                    omitidos += 1
                    continue

                # 5. Usamos el campo SSN de USERINFO para relacionarlo con Colaboradores
                ssn = user_info.ssn
                if not ssn:
                    self.stdout.write(f"Usuario {user_id} en USERINFO no tiene SSN; se omite.")
                    omitidos += 1
                    continue

                colaborador = Colaboradores.objects.filter(codigocolaborador=ssn, estado='ACTIVO').first()
                if not colaborador:
                    self.stdout.write(f"No se encontró colaborador para SSN {ssn} (USERID {user_id}); se omite.")
                    omitidos += 1
                    continue

                # 6. Si falta la salida, intentar asignar la hora de salida programada según el rol asignado
                if not salida_dt:
                    rol_asignado = RolAsignado.objects.filter(
                        colaborador=colaborador,
                        estado='ACTIVO',
                        fecha_inicio__lte=day,
                        fecha_fin__gte=day
                    ).first()
                    if rol_asignado and rol_asignado.rol:
                        dia_semana = day.weekday()  # 0 = lunes, ..., 6 = domingo
                        if dia_semana < 5:
                            salida_programada = rol_asignado.rol.hora_fin_semana
                        elif dia_semana == 5:
                            salida_programada = rol_asignado.rol.hora_fin_sabado
                        elif dia_semana == 6:
                            salida_programada = rol_asignado.rol.hora_fin_domingo
                        else:
                            salida_programada = None
                        salida_final = salida_programada
                        self.stdout.write(f"Usuario {user_id} en {day}: sin salida real, se asigna salida programada {salida_programada}.")
                    else:
                        salida_final = None
                else:
                    salida_final = salida_dt.time()  # Convertimos a time

                # Convertimos la entrada a solo hora
                entrada_time = entrada_dt.time()

                # 7. Crear o actualizar el registro en RegistroAsistencia
                asistencia = RegistroAsistencia.objects.filter(colaborador=colaborador, fecha=day).first()
                # Buscamos el rol asignado activo para este colaborador en la fecha, para asignarlo (si lo hay)
                rol_asig = RolAsignado.objects.filter(
                    colaborador=colaborador,
                    estado='ACTIVO',
                    fecha_inicio__lte=day,
                    fecha_fin__gte=day
                ).first()

                if asistencia:
                    asistencia.hora_entrada = entrada_time
                    asistencia.hora_salida = salida_final
                    asistencia.rol = rol_asig.rol if rol_asig else None
                    asistencia.save()
                    actualizados += 1
                    self.stdout.write(f"Actualizada asistencia para {colaborador} en {day}.")
                else:
                    RegistroAsistencia.objects.create(
                        colaborador=colaborador,
                        sucursal=colaborador.sucursal,  # Se asume que el colaborador tiene asignada la sucursal
                        fecha=day,
                        hora_entrada=entrada_time,
                        hora_salida=salida_final,
                        rol=(rol_asig.rol if rol_asig else None)
                    )
                    creados += 1
                    self.stdout.write(f"Creada asistencia para {colaborador} en {day}.")
            except Exception as e:
                logger.exception(f"Error procesando usuario {rec['user_id']} en {rec['day']}: {e}")
                omitidos += 1
                continue

        self.stdout.write(f"Sincronización completada. Creados: {creados}, Actualizados: {actualizados}, Omitidos: {omitidos}.")