from datetime import date, time, timedelta, datetime
import json
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Rol, RolAsignado, RegistroAsistencia
from django.http import JsonResponse
from Apps.permisos.models import Sucursal, Departamento, Colaboradores, Jefes, registroPermisos
from django.utils.safestring import mark_safe
# Create your views here.
'''
Codigo necesario para la creacion de roles
'''

'''
@login_required
def crear_rol(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        hora_inicio_semana = request.POST.get('hora_inicio_semana')
        hora_fin_semana = request.POST.get('hora_fin_semana')
        hora_inicio_sabado = request.POST.get('hora_inicio_sabado') or None
        hora_fin_sabado = request.POST.get('hora_fin_sabado') or None
        hora_inicio_domingo = request.POST.get('hora_inicio_domingo') or None
        hora_fin_domingo = request.POST.get('hora_fin_domingo') or None

        # Crear el rol
        Rol.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            hora_inicio_semana=hora_inicio_semana,
            hora_fin_semana=hora_fin_semana,
            hora_inicio_sabado=hora_inicio_sabado,
            hora_fin_sabado=hora_fin_sabado,
            hora_inicio_domingo=hora_inicio_domingo,
            hora_fin_domingo=hora_fin_domingo
        )
        return redirect('listar_roles')
    elif request.method == 'GET':
        return render(request, 'crear_rol.html')


@login_required
def listar_roles(request):
    roles = Rol.objects.all()
    return render(request, 'listar_roles.html', {'roles': roles})



Codigo necesario para la asignacion de roles



@login_required
def asignar_rol(request):
    if request.method == 'POST':
        empleado_id = request.POST.get('empleado')
        rol_id = request.POST.get('rol')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        empleado = User.objects.get(id=empleado_id)
        rol = Rol.objects.get(id=rol_id)

        # Asignar el rol
        RolAsignado.objects.create(
            empleado=empleado,
            rol=rol,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )
        return redirect('listar_roles_asignados')

    empleados = User.objects.all()
    roles = Rol.objects.all()
    return render(request, 'asignar_rol.html', {'empleados': empleados, 'roles': roles})


@login_required
def listar_roles_asignados(request):
    roles_asignados = RolAsignado.objects.select_related('empleado', 'rol')
    return render(request, 'listar_roles_asignados.html', {'roles_asignados': roles_asignados})



Codigo necesario para el registro de asistencias



@login_required
def registrar_asistencia(request):
    if request.method == 'POST':
        empleado_id = request.POST.get('empleado')
        hora_entrada = request.POST.get('hora_entrada')
        hora_salida = request.POST.get('hora_salida')
        fecha_actual = date.today()

        empleado = User.objects.get(id=empleado_id)

        # Obtener el rol asignado vigente
        rol_asignado = RolAsignado.objects.filter(
            empleado=empleado,
            fecha_inicio__lte=fecha_actual,
            fecha_fin__gte=fecha_actual
        ).first()

        cumplimiento = False
        if rol_asignado:
            # Validar si la hora de entrada cumple con el horario del rol
            hora_inicio_rol = rol_asignado.rol.hora_inicio_semana
            cumplimiento = time.fromisoformat(hora_entrada) <= hora_inicio_rol

        # Registrar la asistencia
        RegistroAsistencia.objects.create(
            empleado=empleado,
            fecha=fecha_actual,
            hora_entrada=hora_entrada,
            hora_salida=hora_salida,
            cumplimiento=cumplimiento
        )
        return redirect('listar_asistencias')

    empleados = User.objects.all()
    return render(request, 'registrar_asistencia.html', {'empleados': empleados})


@login_required
def listar_asistencias(request):
    asistencias = RegistroAsistencia.objects.select_related('empleado')
    return render(request, 'listar_asistencias.html', {'asistencias': asistencias})



A continuacion se presentan las vistas de prueba



@login_required
def sucursales(request):
    if request.method == 'POST':
        # Crear una nueva sucursal
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        estado = request.POST.get('estado', 'ACTIVO')
        Sucursal.objects.create(
            nombre_sucursal=nombre,
            estado=estado,
            fechacreacion=request.user
        )
        return redirect('sucursales')

    # Listar todas las sucursales
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursales.html', {'sucursales': sucursales})


@login_required
def departamentos(request):
    if request.method == 'POST':
        # Crear un nuevo departamento
        nombre = request.POST.get('nombre')
        sucursal_id = request.POST.get('sucursal')
        sucursal = Sucursal.objects.get(id=sucursal_id)
        estado = request.POST.get('estado', 'ACTIVO')
        Departamento.objects.create(
            nombre_departamento=nombre,
            estado=estado,
            fechacreacion=request.user
        )
        return redirect('departamentos')

    # Listar todos los departamentos y sucursales para el formulario
    departamentos = Departamento.objects.all()
    sucursales = Sucursal.objects.all()
    return render(request, 'departamentos.html', {'departamentos': departamentos, 'sucursales': sucursales})


@login_required
def colaboradores(request):
    if request.method == 'POST':
        # Crear un nuevo colaborador
        codigo = request.POST.get('codigo')
        identidad = request.POST.get('identidad')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        departamento_id = request.POST.get('departamento')
        departamento = Departamento.objects.get(id=departamento_id)
        estado = request.POST.get('estado', 'ACTIVO')
        Colaboradores.objects.create(
            codigocolaborador=codigo,
            nombrecolaborador=nombre,
            departamento=departamento,
            estado=estado,
            fechacreacion=request.user
        )
        return redirect('colaboradores')

    # Listar todos los colaboradores y departamentos para el formulario
    colaboradores = Colaboradores.objects.select_related('departamento')
    departamentos = Departamento.objects.all()
    return render(request, 'colaboradores.html', {'colaboradores': colaboradores, 'departamentos': departamentos})


@login_required
def jefes(request):
    if request.method == 'POST':
        # Crear un nuevo jefe
        codigo = request.POST.get('codigo')
        identidad = request.POST.get('identidad')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        sucursal_id = request.POST.get('sucursal')
        sucursal = Sucursal.objects.get(id=sucursal_id)
        estado = request.POST.get('estado', 'ACTIVO')
        Jefes.objects.create(
            codigo=codigo,
            identidadjefe=identidad,
            nombrejefe=nombre,
            estado=estado,
            fechacreacion=request.user
        )
        return redirect('jefes')

    # Listar todos los jefes y sucursales para el formulario
    jefes = Jefes.objects.all()
    sucursales = Sucursal.objects.all()
    return render(request, 'jefes.html', {'jefes': jefes, 'sucursales': sucursales})


@login_required
def registro_asistencia(request):
    if request.method == 'POST':
        # Registrar asistencia
        colaborador_id = request.POST.get('colaborador')
        fecha = request.POST.get('fecha')
        hora_entrada = request.POST.get('hora_entrada')
        hora_salida = request.POST.get('hora_salida')
        colaborador = Colaboradores.objects.get(id=colaborador_id)

        # Obtener el rol asignado y validar el cumplimiento
        rol = colaborador.departamento.sucursal.roles.filter(
            estado='ACTIVO').first()
        cumplimiento = 'NO_CUMPLIO'
        if rol:
            if hora_entrada and hora_salida:
                hora_inicio = rol.hora_inicio_semana if int(
                    fecha.weekday()) < 5 else rol.hora_inicio_sabado
                cumplimiento = '<' if hora_entrada <= hora_inicio else '>'

        RegistroAsistencia.objects.create(
            colaborador=colaborador,
            sucursal=colaborador.departamento.sucursal,
            rol=rol,
            fecha=fecha,
            hora_entrada=hora_entrada,
            hora_salida=hora_salida,
            cumplimiento=cumplimiento,
            creado_por=request.user
        )
        return redirect('registro_asistencia')

    # Listar asistencias y colaboradores
    asistencias = RegistroAsistencia.objects.select_related(
        'colaborador', 'rol', 'sucursal')
    colaboradores = Colaboradores.objects.all()
    return render(request, 'registro_asistencia.html', {'asistencias': asistencias, 'colaboradores': colaboradores})
'''

# ------------------------------
# ROL
# ------------------------------


def rol_list(request):
    """
    Muestra la lista de roles en estado ACTIVO.
    """
    roles = Rol.objects.filter(estado='ACTIVO')
    return render(request, 'rol_crud.html', {
        'roles': roles,
    })


def rol_create(request):
    """
    Crea un nuevo rol (sin utilizar forms.py).
    """
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        hora_inicio_semana = request.POST.get('hora_inicio_semana')
        hora_fin_semana = request.POST.get('hora_fin_semana')
        hora_inicio_sabado = request.POST.get('hora_inicio_sabado')
        hora_fin_sabado = request.POST.get('hora_fin_sabado')
        hora_inicio_domingo = request.POST.get('hora_inicio_domingo')
        hora_fin_domingo = request.POST.get('hora_fin_domingo')

        # Aquí podrías hacer validaciones adicionales
        if not nombre or not hora_inicio_semana or not hora_fin_semana:
            messages.error(
                request, "Los campos nombre, hora inicio y hora fin entre semana son obligatorios.")
            return redirect('rol_list')

        # Crear la instancia del modelo
        nuevo_rol = Rol.objects.create(
            nombre=nombre.upper(),
            descripcion=descripcion.upper(),
            hora_inicio_semana=hora_inicio_semana,
            hora_fin_semana=hora_fin_semana,
            hora_inicio_sabado=hora_inicio_sabado if hora_inicio_sabado else None,
            hora_fin_sabado=hora_fin_sabado if hora_fin_sabado else None,
            hora_inicio_domingo=hora_inicio_domingo if hora_inicio_domingo else None,
            hora_fin_domingo=hora_fin_domingo if hora_fin_domingo else None,
            creado_por="SISTEMA"  # O el usuario autenticado
        )
        messages.success(
            request, f"Rol '{nuevo_rol.nombre}' creado exitosamente.")
        return redirect('rol_list')

    # Si no es POST, redirige a la lista
    return redirect('rol_list')


def rol_update(request, rol_id):
    """
    Actualiza un rol existente.
    """
    rol = get_object_or_404(Rol, pk=rol_id)

    if request.method == 'POST':
        rol.nombre = request.POST.get('nombre').upper()
        rol.descripcion = request.POST.get('descripcion').upper()
        rol.hora_inicio_semana = request.POST.get('hora_inicio_semana')
        rol.hora_fin_semana = request.POST.get('hora_fin_semana')
        rol.hora_inicio_sabado = request.POST.get('hora_inicio_sabado') or None
        rol.hora_fin_sabado = request.POST.get('hora_fin_sabado') or None
        rol.hora_inicio_domingo = request.POST.get(
            'hora_inicio_domingo') or None
        rol.hora_fin_domingo = request.POST.get('hora_fin_domingo') or None

        # rol.estado no lo cambiamos aquí, solo en inactivar
        rol.modificado_por = "SISTEMA"  # O el usuario actual
        rol.save()

        messages.success(
            request, f"Rol '{rol.nombre}' actualizado correctamente.")
        return redirect('rol_list')

    # Si no es POST, redirigimos a la lista
    return redirect('rol_list')


def rol_inactivate(request, rol_id):
    """
    Marca un rol como INACTIVO (no se elimina físicamente).
    """
    rol = get_object_or_404(Rol, pk=rol_id)
    if request.method == 'POST':
        rol.estado = 'INACTIVO'
        rol.save()
        messages.success(
            request, f"Rol '{rol.nombre}' fue marcado como INACTIVO.")
        return redirect('rol_list')

    # Por convención, si no es POST, redirigimos a la lista
    return redirect('rol_list')


def rolasignado_list(request):
    """
    Lista de roles asignados en estado ACTIVO.
    """
    roles_sinAsignar = Rol.objects.filter(estado='ACTIVO')
    colaboradores = Colaboradores.objects.all()
    roles_asignados = RolAsignado.objects.filter(estado='ACTIVO')
    return render(request, 'rolasignado_crud.html', {
        'roles_asignados': roles_asignados, 'colaboradores': colaboradores, 'roles': roles_sinAsignar,
    })


def rolasignado_create(request):
    """
    Crea un rol asignado a un colaborador, sin usar forms.py.
    """
    if request.method == 'POST':
        colaborador_id = request.POST.get('colaborador')  # ID del colaborador
        rol_id = request.POST.get('rol')                  # ID del rol
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        # Ejemplo: obtener instancias (asegúrate de haber importado el modelo Colaboradores)
        from .models import Colaboradores
        colaborador = get_object_or_404(Colaboradores, pk=colaborador_id)
        rol = get_object_or_404(Rol, pk=rol_id)

        nuevo_rol_asignado = RolAsignado.objects.create(
            colaborador=colaborador,
            rol=rol,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            creado_por="SISTEMA"  # O el usuario actual
        )
        messages.success(request, "Rol asignado creado con éxito.")
        return redirect('rolasignado_list')

    return redirect('rolasignado_list')


def rolasignado_update(request, rolasignado_id):
    """
    Actualiza la información de un rol asignado.
    """
    rol_asignado = get_object_or_404(RolAsignado, pk=rolasignado_id)

    if request.method == 'POST':
        colaborador_id = request.POST.get('colaborador')
        rol_id = request.POST.get('rol')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        from .models import Colaboradores
        colaborador = get_object_or_404(Colaboradores, pk=colaborador_id)
        rol = get_object_or_404(Rol, pk=rol_id)

        rol_asignado.colaborador = colaborador
        rol_asignado.rol = rol
        rol_asignado.fecha_inicio = fecha_inicio
        rol_asignado.fecha_fin = fecha_fin
        rol_asignado.modificado_por = "SISTEMA"  # O el usuario actual
        rol_asignado.save()

        messages.success(request, "Rol asignado actualizado correctamente.")
        return redirect('rolasignado_list')

    return redirect('rolasignado_list')


def rolasignado_inactivate(request, rolasignado_id):
    """
    Marca un rol asignado como INACTIVO.
    """
    rol_asignado = get_object_or_404(RolAsignado, pk=rolasignado_id)
    if request.method == 'POST':
        rol_asignado.estado = 'INACTIVO'
        rol_asignado.save()
        messages.success(request, "Rol asignado inactivado correctamente.")
        return redirect('rolasignado_list')

    return redirect('rolasignado_list')


# def registroasistencia_list(request):
#     """
#     Muestra la lista de registros de asistencia activos.
#     """

#     # Tu lista de registros
#     registros = RegistroAsistencia.objects.filter(estado='ACTIVO')

#     # Lista de colaboradores
#     colaboradores = Colaboradores.objects.filter(estado='ACTIVO')

#     # Opcional, si lo usas en otras partes
#     sucursales = Sucursal.objects.filter(estado='ACTIVO')
#     roles = Rol.objects.filter(estado='ACTIVO')

#     # Construimos un diccionario con la info que deseamos precargar
#     # Suponiendo que cada colaborador tiene un solo rol activo
#     # o tomamos el último rol asignado en fecha, etc.

#     colaborador_info = {}
#     for c in colaboradores:
#         # Encontrar la sucursal del colaborador (si tu modelo Colaboradores tiene un campo directo)
#         # Aquí asumimos `c.sucursal` es la sucursal del colaborador.
#         sucursal_id = c.sucursal.id if c.sucursal else ''
#         sucursal_nombre = c.sucursal.nombre_sucursal if c.sucursal else 'N/A'

#         # Buscar un rol asignado activo (o el más reciente). Aquí un ejemplo muy simplificado:
#         rol_asignado = RolAsignado.objects.filter(
#             colaborador=c, estado='ACTIVO').order_by('-fecha_inicio').first()
#         if rol_asignado:
#             rol_id = rol_asignado.rol.id
#             rol_nombre = rol_asignado.rol.nombre
#         else:
#             rol_id = ''
#             rol_nombre = ''

#         colaborador_info[c.id] = {
#             'sucursal_id': sucursal_id,
#             'sucursal_nombre': sucursal_nombre,
#             'rol_id': rol_id,
#             'rol_nombre': rol_nombre
#         }

#     registros = RegistroAsistencia.objects.filter(estado='ACTIVO')
#     return render(request, 'registroasistencia_crud.html', {
#         'registros': registros, 'colaboradores': colaboradores,
#         'sucursales': sucursales,
#         'roles': roles,
#         'colaborador_info': colaborador_info,
#     })

def registroasistencia_list(request):
    registros = RegistroAsistencia.objects.filter(estado='ACTIVO')
    colaboradores = Colaboradores.objects.filter(estado='ACTIVO')

    colaborador_info = {}
    for c in colaboradores:
        sucursal_id = c.sucursal.id if c.sucursal else ""
        sucursal_nombre = c.sucursal.nombre_sucursal if c.sucursal else "N/A"

        def formatear_hora(hora):
            if hora:  # Verifica si la hora existe (no es None)
                return hora.strftime("%H:%M")  # Formatea a HH:MM
            return "N/A"  # O cadena vacía si prefieres ""

        rol_asignado = RolAsignado.objects.filter(
            colaborador=c, estado='ACTIVO').first()
        rol_id = rol_asignado.rol.id if rol_asignado else ""
        rol_nombre = rol_asignado.rol.nombre if rol_asignado else "Sin Rol"
        rol_horario_semana = f"{formatear_hora(rol_asignado.rol.hora_inicio_semana)} - {formatear_hora(rol_asignado.rol.hora_fin_semana)}" if rol_asignado else "N/A"
        rol_horario_sabado = f"{formatear_hora(rol_asignado.rol.hora_inicio_sabado)} - {formatear_hora(rol_asignado.rol.hora_fin_sabado)}" if rol_asignado else "N/A"
        rol_horario_domingo = f"{formatear_hora(rol_asignado.rol.hora_inicio_domingo)} - {formatear_hora(rol_asignado.rol.hora_fin_domingo)}" if rol_asignado else "N/A"

        colaborador_info[c.id] = {
            "sucursal_id": sucursal_id,
            "sucursal_nombre": sucursal_nombre,
            "rol_id": rol_id,
            "rol_nombre": rol_nombre,
            "rol_horario_semana": rol_horario_semana,
            "rol_horario_sabado": rol_horario_sabado,
            "rol_horario_domingo": rol_horario_domingo
        }
    # colaborador_info = mark_safe(json.dumps(colaborador_info_json))
    # <--- Revisión en consola de Django
    print("DEBUG: colaborador_info =", colaborador_info)

    return render(request, 'registroasistencia_crud.html', {
        'registros': registros,
        'colaboradores': colaboradores,
        'colaborador_info': colaborador_info,
    })


def registroasistencia_create(request):
    """
    Crea un nuevo registro de asistencia, validando si la fecha está dentro de un RolAsignado.
    """
    if request.method == 'POST':
        colaborador_id = request.POST.get('colaborador')
        sucursal_id = request.POST.get('sucursal')
        rol_id = request.POST.get('rol')  # Puede ser opcional
        fecha_str = request.POST.get('fecha')  # "YYYY-MM-DD"
        hora_entrada_str = request.POST.get('hora_entrada')
        hora_salida_str = request.POST.get('hora_salida')

        # Obtener instancias base
        colaborador = get_object_or_404(Colaboradores, pk=colaborador_id)
        sucursal = get_object_or_404(Sucursal, pk=sucursal_id)

        # Convertir fecha a objeto date
        fecha_obj = datetime.strptime(
            fecha_str, '%Y-%m-%d').date() if fecha_str else None

        # Convertir horas a time
        hora_entrada = None
        if hora_entrada_str:
            hora_entrada = datetime.strptime(hora_entrada_str, '%H:%M').time()

        hora_salida = None
        if hora_salida_str:
            hora_salida = datetime.strptime(hora_salida_str, '%H:%M').time()

        # 1) Verificar si existe un rol asignado dentro del rango de fechas
        rol_asignado_valido = RolAsignado.objects.filter(
            colaborador=colaborador,
            estado='ACTIVO',
            fecha_inicio__lte=fecha_obj,
            fecha_fin__gte=fecha_obj
        ).first()

        # Si no existe un rol asignado para esa fecha, guardaremos la asistencia con advertencia
        if not rol_asignado_valido:
            messages.warning(request, (
                "El colaborador no tiene un rol asignado en ese rango de fechas. "
                "Se creará la asistencia sin rol asignado o con una advertencia."
            ))
            # Ejemplo: no asignamos rol para dejar en claro que está 'fuera de rango'
            rol_obj = None
        else:
            # Sí existe un rol asignado. Si el usuario eligió un rol en el formulario, lo tomamos
            if rol_id:
                rol_obj = get_object_or_404(Rol, pk=rol_id)
            else:
                # O podemos tomar directamente el rol de 'rol_asignado_valido.rol'
                rol_obj = rol_asignado_valido.rol

        # Creamos el registro
        nuevo_registro = RegistroAsistencia.objects.create(
            colaborador=colaborador,
            sucursal=sucursal,
            rol=rol_obj,
            fecha=fecha_obj,
            hora_entrada=hora_entrada,
            hora_salida=hora_salida,
            creado_por=None  # o request.user, si estás usando auth
        )

        messages.success(
            request, "Registro de asistencia creado correctamente.")
        return redirect('registroasistencia_list')

    # Si no es POST
    return redirect('registroasistencia_list')


def registroasistencia_update(request, registro_id):
    """
    Actualiza un registro de asistencia, validando también el rango de fechas del rol asignado.
    """
    registro = get_object_or_404(RegistroAsistencia, pk=registro_id)

    if request.method == 'POST':
        colaborador_id = request.POST.get('colaborador')
        sucursal_id = request.POST.get('sucursal')
        rol_id = request.POST.get('rol')
        fecha_str = request.POST.get('fecha')           # "YYYY-MM-DD"
        hora_entrada_str = request.POST.get('hora_entrada')  # "HH:MM"
        hora_salida_str = request.POST.get('hora_salida')    # "HH:MM"

        from .models import Colaboradores, Sucursal, Rol, RolAsignado
        colaborador = get_object_or_404(Colaboradores, pk=colaborador_id)
        sucursal = get_object_or_404(Sucursal, pk=sucursal_id)

        # 1) Convertir la fecha
        if fecha_str:
            fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        else:
            fecha_obj = None  # O maneja un default

        # 2) Convertir horas a objetos time
        if hora_entrada_str:
            hora_entrada_obj = datetime.strptime(
                hora_entrada_str, '%H:%M').time()
        else:
            hora_entrada_obj = None

        if hora_salida_str:
            hora_salida_obj = datetime.strptime(
                hora_salida_str, '%H:%M').time()
        else:
            hora_salida_obj = None

        # 3) Verificar si existe un rol asignado dentro del rango de fechas para esa fecha_obj
        rol_asignado_valido = RolAsignado.objects.filter(
            colaborador=colaborador,
            estado='ACTIVO',
            fecha_inicio__lte=fecha_obj,
            fecha_fin__gte=fecha_obj
        ).first()

        if not rol_asignado_valido:
            # No se encontró un rol válido para esa fecha.
            # Mostramos advertencia y podemos forzar a rol=None,
            # o respetar el rol_id que se recibió (depende de tu lógica)
            messages.warning(request, (
                "El colaborador no tiene un rol asignado en este rango de fechas. "
                "Se actualizará la asistencia sin rol asignado o con advertencia."
            ))
            # o podrías dejar get_object_or_404(Rol, pk=rol_id) si deseas
            rol_obj = None
        else:
            # Sí hay un rol válido
            if rol_id:
                rol_obj = get_object_or_404(Rol, pk=rol_id)
            else:
                # O tomamos el rol directamente de rol_asignado_valido
                rol_obj = rol_asignado_valido.rol

        # 4) Asignar los valores convertidos
        registro.colaborador = colaborador
        registro.sucursal = sucursal
        registro.rol = rol_obj
        registro.fecha = fecha_obj
        registro.hora_entrada = hora_entrada_obj
        registro.hora_salida = hora_salida_obj

        registro.save()
        return redirect('registroasistencia_list')

    # Si no es POST
    return redirect('registroasistencia_list')


def registroasistencia_inactivate(request, registro_id):
    """
    Marca un registro de asistencia como INACTIVO.
    """
    registro = get_object_or_404(RegistroAsistencia, pk=registro_id)
    if request.method == 'POST':
        registro.estado = 'INACTIVO'
        registro.save()
        messages.success(
            request, "Registro de asistencia inactivado correctamente.")
        return redirect('registroasistencia_list')

    return redirect('registroasistencia_list')
