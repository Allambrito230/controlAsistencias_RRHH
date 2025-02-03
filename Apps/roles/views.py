from datetime import date, time, timedelta, datetime
import json
import logging
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Apps.permisos.models import Sucursal, Departamento, Colaboradores, Jefes, registroPermisos
from .models import Rol, RolAsignado#, RegistroAsistencia

# Configuración del logger
logger = logging.getLogger(__name__)

# ------------------------------
# Funciones Helper
# ------------------------------


def convertir_fecha(fecha_str):
    """
    Convierte una cadena en formato 'AAAA-MM-DD' a un objeto date.
    Devuelve None si falla la conversión.
    """
    try:
        return datetime.strptime(fecha_str, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        return None


def convertir_hora(hora_str):
    """
    Convierte una cadena en formato 'HH:MM' a un objeto time.
    Devuelve None si falla la conversión.
    """
    try:
        return datetime.strptime(hora_str, '%H:%M').time()
    except (ValueError, TypeError):
        return None

# ------------------------------
# Vistas para Roles
# ------------------------------


@login_required
def rol_list(request):
    """
    Muestra la lista de roles en estado ACTIVO.
    """
    try:
        roles = Rol.objects.filter(estado='ACTIVO')
    except Exception as e:
        logger.exception("Error al obtener la lista de roles")
        messages.error(request, "Error al obtener la lista de roles.")
        roles = []
    return render(request, 'rol_crud.html', {'roles': roles})


@login_required
def rol_create(request):
    """
    Crea un nuevo rol (sin utilizar forms.py).
    """
    if request.method == 'POST':
        try:
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion')
            hora_inicio_semana = request.POST.get('hora_inicio_semana')
            hora_fin_semana = request.POST.get('hora_fin_semana')
            hora_inicio_sabado = request.POST.get('hora_inicio_sabado')
            hora_fin_sabado = request.POST.get('hora_fin_sabado')
            hora_inicio_domingo = request.POST.get('hora_inicio_domingo')
            hora_fin_domingo = request.POST.get('hora_fin_domingo')

            # Validación de campos obligatorios
            if not nombre or not hora_inicio_semana or not hora_fin_semana:
                messages.error(
                    request, "Los campos nombre, hora inicio y hora fin entre semana son obligatorios.")
                return redirect('rol_list')

            # Crear la instancia del modelo
            nuevo_rol = Rol.objects.create(
                nombre=nombre.upper(),
                descripcion=descripcion.upper() if descripcion else '',
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
        except Exception as e:
            logger.exception("Error al crear el rol")
            messages.error(
                request, "Ha ocurrido un error al crear el rol. Por favor, intente de nuevo.")
            return redirect('rol_list')
    return redirect('rol_list')


@login_required
def rol_update(request, rol_id):
    """
    Actualiza un rol existente.
    """
    try:
        rol = get_object_or_404(Rol, pk=rol_id)
        if request.method == 'POST':
            try:
                nombre = request.POST.get('nombre')
                descripcion = request.POST.get('descripcion')
                hora_inicio_semana = request.POST.get('hora_inicio_semana')
                hora_fin_semana = request.POST.get('hora_fin_semana')
                hora_inicio_sabado = request.POST.get('hora_inicio_sabado')
                hora_fin_sabado = request.POST.get('hora_fin_sabado')
                hora_inicio_domingo = request.POST.get('hora_inicio_domingo')
                hora_fin_domingo = request.POST.get('hora_fin_domingo')

                # Validaciones básicas
                if not nombre or not hora_inicio_semana or not hora_fin_semana:
                    messages.error(
                        request, "Los campos nombre, hora inicio y hora fin entre semana son obligatorios.")
                    return redirect('rol_list')

                rol.nombre = nombre.upper()
                rol.descripcion = descripcion.upper() if descripcion else ''
                rol.hora_inicio_semana = hora_inicio_semana
                rol.hora_fin_semana = hora_fin_semana
                rol.hora_inicio_sabado = hora_inicio_sabado or None
                rol.hora_fin_sabado = hora_fin_sabado or None
                rol.hora_inicio_domingo = hora_inicio_domingo or None
                rol.hora_fin_domingo = hora_fin_domingo or None

                # Actualización de metadatos
                rol.modificado_por = "SISTEMA"  # O el usuario actual
                rol.save()

                messages.success(
                    request, f"Rol '{rol.nombre}' actualizado correctamente.")
                return redirect('rol_list')
            except Exception as e:
                logger.exception(
                    "Error al actualizar el rol con id %s", rol_id)
                messages.error(
                    request, "Ocurrió un error al actualizar el rol. Por favor, intente de nuevo.")
                return redirect('rol_list')
        return redirect('rol_list')
    except Exception as e:
        logger.exception("Error al obtener el rol con id %s", rol_id)
        messages.error(request, "No se pudo encontrar el rol especificado.")
        return redirect('rol_list')


@login_required
def rol_inactivate(request, rol_id):
    """
    Marca un rol como INACTIVO (no se elimina físicamente).
    """
    try:
        rol = get_object_or_404(Rol, pk=rol_id)
        if request.method == 'POST':
            rol.estado = 'INACTIVO'
            rol.save()
            messages.success(
                request, f"Rol '{rol.nombre}' fue marcado como INACTIVO.")
            return redirect('rol_list')
        return redirect('rol_list')
    except Exception as e:
        logger.exception("Error al inactivar el rol con id %s", rol_id)
        messages.error(
            request, "Ocurrió un error al inactivar el rol. Por favor, intente de nuevo.")
        return redirect('rol_list')


# ------------------------------
# Vistas para Rol Asignado
# ------------------------------

@login_required
def rolasignado_list(request):
    """
    Lista de roles asignados en estado ACTIVO.
    """
    try:
        roles_sinAsignar = Rol.objects.filter(estado='ACTIVO')
        colaboradores = Colaboradores.objects.all()
        roles_asignados = RolAsignado.objects.filter(estado='ACTIVO')
    except Exception as e:
        logger.exception("Error al obtener datos para roles asignados")
        messages.error(
            request, "Error al obtener la lista de roles asignados.")
        return redirect('rol_list')
    return render(request, 'rolasignado_crud.html', {
        'roles_asignados': roles_asignados,
        'colaboradores': colaboradores,
        'roles': roles_sinAsignar,
    })


@login_required
def rolasignado_create(request):
    """
    Crea un rol asignado a un colaborador, sin usar forms.py.
    """
    if request.method == 'POST':
        try:
            colaborador_id = request.POST.get('colaborador')
            rol_id = request.POST.get('rol')
            fecha_inicio = request.POST.get('fecha_inicio')
            fecha_fin = request.POST.get('fecha_fin')

            from .models import Colaboradores  # Import local
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
        except Exception as e:
            logger.exception("Error al crear rol asignado")
            messages.error(
                request, "Ocurrió un error al asignar el rol. Por favor, intente de nuevo.")
            return redirect('rolasignado_list')
    return redirect('rolasignado_list')


@login_required
def rolasignado_update(request, rolasignado_id):
    """
    Actualiza la información de un rol asignado.
    """
    try:
        rol_asignado = get_object_or_404(RolAsignado, pk=rolasignado_id)
        if request.method == 'POST':
            try:
                colaborador_id = request.POST.get('colaborador')
                rol_id = request.POST.get('rol')
                fecha_inicio = request.POST.get('fecha_inicio')
                fecha_fin = request.POST.get('fecha_fin')

                from .models import Colaboradores
                colaborador = get_object_or_404(
                    Colaboradores, pk=colaborador_id)
                rol = get_object_or_404(Rol, pk=rol_id)

                rol_asignado.colaborador = colaborador
                rol_asignado.rol = rol
                rol_asignado.fecha_inicio = fecha_inicio
                rol_asignado.fecha_fin = fecha_fin
                rol_asignado.modificado_por = "SISTEMA"  # O el usuario actual
                rol_asignado.save()

                messages.success(
                    request, "Rol asignado actualizado correctamente.")
                return redirect('rolasignado_list')
            except Exception as e:
                logger.exception(
                    "Error al actualizar rol asignado con id %s", rolasignado_id)
                messages.error(
                    request, "Ocurrió un error al actualizar el rol asignado. Por favor, intente de nuevo.")
                return redirect('rolasignado_list')
        return redirect('rolasignado_list')
    except Exception as e:
        logger.exception(
            "Error al obtener rol asignado con id %s", rolasignado_id)
        messages.error(
            request, "No se pudo encontrar el rol asignado especificado.")
        return redirect('rolasignado_list')


@login_required
def rolasignado_inactivate(request, rolasignado_id):
    """
    Marca un rol asignado como INACTIVO.
    """
    try:
        rol_asignado = get_object_or_404(RolAsignado, pk=rolasignado_id)
        if request.method == 'POST':
            rol_asignado.estado = 'INACTIVO'
            rol_asignado.save()
            messages.success(request, "Rol asignado inactivado correctamente.")
            return redirect('rolasignado_list')
        return redirect('rolasignado_list')
    except Exception as e:
        logger.exception(
            "Error al inactivar rol asignado con id %s", rolasignado_id)
        messages.error(
            request, "Ocurrió un error al inactivar el rol asignado. Por favor, intente de nuevo.")
        return redirect('rolasignado_list')


# ------------------------------
# Vistas para Registro de Asistencia
# ------------------------------

# @login_required
# def registroasistencia_list(request):
#     try:
#         registros = RegistroAsistencia.objects.filter(estado='ACTIVO')
#         colaboradores = Colaboradores.objects.filter(estado='ACTIVO')

#         colaborador_info = {}
#         for c in colaboradores:
#             sucursal_id = c.sucursal.id if c.sucursal else ""
#             sucursal_nombre = c.sucursal.nombre_sucursal if c.sucursal else "N/A"

#             def formatear_hora(hora):
#                 if hora:
#                     return hora.strftime("%H:%M")
#                 return "N/A"

#             rol_asignado = RolAsignado.objects.filter(
#                 colaborador=c, estado='ACTIVO').first()
#             rol_id = rol_asignado.rol.id if rol_asignado else ""
#             rol_nombre = rol_asignado.rol.nombre if rol_asignado else "Sin Rol"
#             rol_horario_semana = (
#                 f"{formatear_hora(rol_asignado.rol.hora_inicio_semana)} - {formatear_hora(rol_asignado.rol.hora_fin_semana)}"
#                 if rol_asignado else "N/A"
#             )
#             rol_horario_sabado = (
#                 f"{formatear_hora(rol_asignado.rol.hora_inicio_sabado)} - {formatear_hora(rol_asignado.rol.hora_fin_sabado)}"
#                 if rol_asignado else "N/A"
#             )
#             rol_horario_domingo = (
#                 f"{formatear_hora(rol_asignado.rol.hora_inicio_domingo)} - {formatear_hora(rol_asignado.rol.hora_fin_domingo)}"
#                 if rol_asignado else "N/A"
#             )

#             colaborador_info[c.id] = {
#                 "sucursal_id": sucursal_id,
#                 "sucursal_nombre": sucursal_nombre,
#                 "rol_id": rol_id,
#                 "rol_nombre": rol_nombre,
#                 "rol_horario_semana": rol_horario_semana,
#                 "rol_horario_sabado": rol_horario_sabado,
#                 "rol_horario_domingo": rol_horario_domingo
#             }
#         return render(request, 'registroasistencia_crud.html', {
#             'registros': registros,
#             'colaboradores': colaboradores,
#             'colaborador_info': colaborador_info,
#         })
#     except Exception as e:
#         logger.exception("Error al listar registros de asistencia")
#         messages.error(
#             request, "Ocurrió un error al obtener los registros de asistencia.")
#         return redirect('rol_list')


# @login_required
# def registroasistencia_create(request):
#     """
#     Crea un nuevo registro de asistencia, validando si la fecha está dentro de un RolAsignado.
#     """
#     if request.method == 'POST':
#         try:
#             colaborador_id = request.POST.get('colaborador')
#             sucursal_id = request.POST.get('sucursal')
#             rol_id = request.POST.get('rol')  # Puede ser opcional
#             fecha_str = request.POST.get('fecha')  # "YYYY-MM-DD"
#             hora_entrada_str = request.POST.get('hora_entrada')
#             hora_salida_str = request.POST.get('hora_salida')

#             # Obtener instancias base
#             colaborador = get_object_or_404(Colaboradores, pk=colaborador_id)
#             sucursal = get_object_or_404(Sucursal, pk=sucursal_id)

#             # Convertir fecha a objeto date
#             fecha_obj = convertir_fecha(fecha_str)
#             if not fecha_obj:
#                 messages.error(
#                     request, "El formato de la fecha es incorrecto. Use AAAA-MM-DD.")
#                 return redirect('registroasistencia_list')

#             # Convertir horas a objetos time
#             hora_entrada = convertir_hora(hora_entrada_str)
#             if hora_entrada_str and not hora_entrada:
#                 messages.error(
#                     request, "El formato de la hora de entrada es incorrecto. Use HH:MM.")
#                 return redirect('registroasistencia_list')

#             hora_salida = convertir_hora(hora_salida_str)
#             if hora_salida_str and not hora_salida:
#                 messages.error(
#                     request, "El formato de la hora de salida es incorrecto. Use HH:MM.")
#                 return redirect('registroasistencia_list')

#             # Verificar si existe un rol asignado dentro del rango de fechas
#             rol_asignado_valido = RolAsignado.objects.filter(
#                 colaborador=colaborador,
#                 estado='ACTIVO',
#                 fecha_inicio__lte=fecha_obj,
#                 fecha_fin__gte=fecha_obj
#             ).first()

#             if not rol_asignado_valido:
#                 messages.warning(request, (
#                     "El colaborador no tiene un rol asignado en ese rango de fechas. "
#                     "Se creará la asistencia sin rol asignado o con una advertencia."
#                 ))
#                 rol_obj = None
#             else:
#                 if rol_id:
#                     rol_obj = get_object_or_404(Rol, pk=rol_id)
#                 else:
#                     rol_obj = rol_asignado_valido.rol

#             nuevo_registro = RegistroAsistencia.objects.create(
#                 colaborador=colaborador,
#                 sucursal=sucursal,
#                 rol=rol_obj,
#                 fecha=fecha_obj,
#                 hora_entrada=hora_entrada,
#                 hora_salida=hora_salida,
#                 creado_por=request.user  # o None, si no se usa auth
#             )

#             messages.success(
#                 request, "Registro de asistencia creado correctamente.")
#             return redirect('registroasistencia_list')
#         except Exception as e:
#             logger.exception("Error al crear registro de asistencia")
#             messages.error(
#                 request, "Ocurrió un error al crear el registro de asistencia. Por favor, intente de nuevo.")
#             return redirect('registroasistencia_list')
#     return redirect('registroasistencia_list')


# @login_required
# def registroasistencia_update(request, registro_id):
#     """
#     Actualiza un registro de asistencia, validando también el rango de fechas del rol asignado.
#     """
#     try:
#         registro = get_object_or_404(RegistroAsistencia, pk=registro_id)
#         if request.method == 'POST':
#             try:
#                 colaborador_id = request.POST.get('colaborador')
#                 sucursal_id = request.POST.get('sucursal')
#                 rol_id = request.POST.get('rol')
#                 fecha_str = request.POST.get('fecha')  # "YYYY-MM-DD"
#                 hora_entrada_str = request.POST.get('hora_entrada')  # "HH:MM"
#                 hora_salida_str = request.POST.get('hora_salida')    # "HH:MM"

#                 from .models import Colaboradores, Sucursal, Rol, RolAsignado
#                 colaborador = get_object_or_404(
#                     Colaboradores, pk=colaborador_id)
#                 sucursal = get_object_or_404(Sucursal, pk=sucursal_id)

#                 fecha_obj = convertir_fecha(fecha_str)
#                 if not fecha_obj:
#                     messages.error(
#                         request, "El formato de la fecha es incorrecto. Use AAAA-MM-DD.")
#                     return redirect('registroasistencia_list')

#                 hora_entrada_obj = convertir_hora(hora_entrada_str)
#                 if hora_entrada_str and not hora_entrada_obj:
#                     messages.error(
#                         request, "El formato de la hora de entrada es incorrecto. Use HH:MM.")
#                     return redirect('registroasistencia_list')

#                 hora_salida_obj = convertir_hora(hora_salida_str)
#                 if hora_salida_str and not hora_salida_obj:
#                     messages.error(
#                         request, "El formato de la hora de salida es incorrecto. Use HH:MM.")
#                     return redirect('registroasistencia_list')

#                 rol_asignado_valido = RolAsignado.objects.filter(
#                     colaborador=colaborador,
#                     estado='ACTIVO',
#                     fecha_inicio__lte=fecha_obj,
#                     fecha_fin__gte=fecha_obj
#                 ).first()

#                 if not rol_asignado_valido:
#                     messages.warning(request, (
#                         "El colaborador no tiene un rol asignado en este rango de fechas. "
#                         "Se actualizará la asistencia sin rol asignado o con advertencia."
#                     ))
#                     rol_obj = None
#                 else:
#                     if rol_id:
#                         rol_obj = get_object_or_404(Rol, pk=rol_id)
#                     else:
#                         rol_obj = rol_asignado_valido.rol

#                 registro.colaborador = colaborador
#                 registro.sucursal = sucursal
#                 registro.rol = rol_obj
#                 registro.fecha = fecha_obj
#                 registro.hora_entrada = hora_entrada_obj
#                 registro.hora_salida = hora_salida_obj
#                 registro.save()

#                 messages.success(
#                     request, "Registro de asistencia actualizado correctamente.")
#                 return redirect('registroasistencia_list')
#             except Exception as e:
#                 logger.exception(
#                     "Error al actualizar el registro de asistencia con id %s", registro_id)
#                 messages.error(
#                     request, "Ocurrió un error al actualizar el registro de asistencia. Por favor, intente de nuevo.")
#                 return redirect('registroasistencia_list')
#         return redirect('registroasistencia_list')
#     except Exception as e:
#         logger.exception(
#             "Error al obtener el registro de asistencia con id %s", registro_id)
#         messages.error(
#             request, "No se pudo encontrar el registro de asistencia especificado.")
#         return redirect('registroasistencia_list')


# @login_required
# def registroasistencia_inactivate(request, registro_id):
#     """
#     Marca un registro de asistencia como INACTIVO.
#     """
#     try:
#         registro = get_object_or_404(RegistroAsistencia, pk=registro_id)
#         if request.method == 'POST':
#             registro.estado = 'INACTIVO'
#             registro.save()
#             messages.success(
#                 request, "Registro de asistencia inactivado correctamente.")
#             return redirect('registroasistencia_list')
#         return redirect('registroasistencia_list')
#     except Exception as e:
#         logger.exception(
#             "Error al inactivar el registro de asistencia con id %s", registro_id)
#         messages.error(
#             request, "Ocurrió un error al inactivar el registro de asistencia. Por favor, intente de nuevo.")
#         return redirect('registroasistencia_list')
