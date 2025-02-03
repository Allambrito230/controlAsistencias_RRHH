from datetime import date, time, timedelta, datetime
import json
import logging
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Apps.permisos.models import Sucursal, Departamento, Colaboradores, Jefes, registroPermisos
from Apps.roles.models import Rol, RolAsignado
from .models import  RegistroAsistencia

# Create your views here.

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
# Vistas para Registro de Asistencia
# ------------------------------

@login_required
def registroasistencia_list(request):
    try:
        registros = RegistroAsistencia.objects.filter(estado='ACTIVO')
        colaboradores = Colaboradores.objects.filter(estado='ACTIVO')

        colaborador_info = {}
        for c in colaboradores:
            sucursal_id = c.sucursal.id if c.sucursal else ""
            sucursal_nombre = c.sucursal.nombre_sucursal if c.sucursal else "N/A"

            def formatear_hora(hora):
                if hora:
                    return hora.strftime("%H:%M")
                return "N/A"

            rol_asignado = RolAsignado.objects.filter(
                colaborador=c, estado='ACTIVO').first()
            rol_id = rol_asignado.rol.id if rol_asignado else ""
            rol_nombre = rol_asignado.rol.nombre if rol_asignado else "Sin Rol"
            rol_horario_semana = (
                f"{formatear_hora(rol_asignado.rol.hora_inicio_semana)} - {formatear_hora(rol_asignado.rol.hora_fin_semana)}"
                if rol_asignado else "N/A"
            )
            rol_horario_sabado = (
                f"{formatear_hora(rol_asignado.rol.hora_inicio_sabado)} - {formatear_hora(rol_asignado.rol.hora_fin_sabado)}"
                if rol_asignado else "N/A"
            )
            rol_horario_domingo = (
                f"{formatear_hora(rol_asignado.rol.hora_inicio_domingo)} - {formatear_hora(rol_asignado.rol.hora_fin_domingo)}"
                if rol_asignado else "N/A"
            )

            colaborador_info[c.id] = {
                "sucursal_id": sucursal_id,
                "sucursal_nombre": sucursal_nombre,
                "rol_id": rol_id,
                "rol_nombre": rol_nombre,
                "rol_horario_semana": rol_horario_semana,
                "rol_horario_sabado": rol_horario_sabado,
                "rol_horario_domingo": rol_horario_domingo
            }
        return render(request, 'registroasistencia_crud.html', {
            'registros': registros,
            'colaboradores': colaboradores,
            'colaborador_info': colaborador_info,
        })
    except Exception as e:
        logger.exception("Error al listar registros de asistencia")
        messages.error(
            request, "Ocurrió un error al obtener los registros de asistencia.")
        return redirect('rol_list')


@login_required
def registroasistencia_create(request):
    """
    Crea un nuevo registro de asistencia, validando si la fecha está dentro de un RolAsignado.
    """
    if request.method == 'POST':
        try:
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
            fecha_obj = convertir_fecha(fecha_str)
            if not fecha_obj:
                messages.error(
                    request, "El formato de la fecha es incorrecto. Use AAAA-MM-DD.")
                return redirect('registroasistencia_list')

            # Convertir horas a objetos time
            hora_entrada = convertir_hora(hora_entrada_str)
            if hora_entrada_str and not hora_entrada:
                messages.error(
                    request, "El formato de la hora de entrada es incorrecto. Use HH:MM.")
                return redirect('registroasistencia_list')

            hora_salida = convertir_hora(hora_salida_str)
            if hora_salida_str and not hora_salida:
                messages.error(
                    request, "El formato de la hora de salida es incorrecto. Use HH:MM.")
                return redirect('registroasistencia_list')

            # Verificar si existe un rol asignado dentro del rango de fechas
            rol_asignado_valido = RolAsignado.objects.filter(
                colaborador=colaborador,
                estado='ACTIVO',
                fecha_inicio__lte=fecha_obj,
                fecha_fin__gte=fecha_obj
            ).first()

            if not rol_asignado_valido:
                messages.warning(request, (
                    "El colaborador no tiene un rol asignado en ese rango de fechas. "
                    "Se creará la asistencia sin rol asignado o con una advertencia."
                ))
                rol_obj = None
            else:
                if rol_id:
                    rol_obj = get_object_or_404(Rol, pk=rol_id)
                else:
                    rol_obj = rol_asignado_valido.rol

            nuevo_registro = RegistroAsistencia.objects.create(
                colaborador=colaborador,
                sucursal=sucursal,
                rol=rol_obj,
                fecha=fecha_obj,
                hora_entrada=hora_entrada,
                hora_salida=hora_salida,
                creado_por=request.user  # o None, si no se usa auth
            )

            messages.success(
                request, "Registro de asistencia creado correctamente.")
            return redirect('registroasistencia_list')
        except Exception as e:
            logger.exception("Error al crear registro de asistencia")
            messages.error(
                request, "Ocurrió un error al crear el registro de asistencia. Por favor, intente de nuevo.")
            return redirect('registroasistencia_list')
    return redirect('registroasistencia_list')


@login_required
def registroasistencia_update(request, registro_id):
    """
    Actualiza un registro de asistencia, validando también el rango de fechas del rol asignado.
    """
    try:
        registro = get_object_or_404(RegistroAsistencia, pk=registro_id)
        if request.method == 'POST':
            try:
                colaborador_id = request.POST.get('colaborador')
                sucursal_id = request.POST.get('sucursal')
                rol_id = request.POST.get('rol')
                fecha_str = request.POST.get('fecha')  # "YYYY-MM-DD"
                hora_entrada_str = request.POST.get('hora_entrada')  # "HH:MM"
                hora_salida_str = request.POST.get('hora_salida')    # "HH:MM"

                from .models import Colaboradores, Sucursal, Rol, RolAsignado
                colaborador = get_object_or_404(
                    Colaboradores, pk=colaborador_id)
                sucursal = get_object_or_404(Sucursal, pk=sucursal_id)

                fecha_obj = convertir_fecha(fecha_str)
                if not fecha_obj:
                    messages.error(
                        request, "El formato de la fecha es incorrecto. Use AAAA-MM-DD.")
                    return redirect('registroasistencia_list')

                hora_entrada_obj = convertir_hora(hora_entrada_str)
                if hora_entrada_str and not hora_entrada_obj:
                    messages.error(
                        request, "El formato de la hora de entrada es incorrecto. Use HH:MM.")
                    return redirect('registroasistencia_list')

                hora_salida_obj = convertir_hora(hora_salida_str)
                if hora_salida_str and not hora_salida_obj:
                    messages.error(
                        request, "El formato de la hora de salida es incorrecto. Use HH:MM.")
                    return redirect('registroasistencia_list')

                rol_asignado_valido = RolAsignado.objects.filter(
                    colaborador=colaborador,
                    estado='ACTIVO',
                    fecha_inicio__lte=fecha_obj,
                    fecha_fin__gte=fecha_obj
                ).first()

                if not rol_asignado_valido:
                    messages.warning(request, (
                        "El colaborador no tiene un rol asignado en este rango de fechas. "
                        "Se actualizará la asistencia sin rol asignado o con advertencia."
                    ))
                    rol_obj = None
                else:
                    if rol_id:
                        rol_obj = get_object_or_404(Rol, pk=rol_id)
                    else:
                        rol_obj = rol_asignado_valido.rol

                registro.colaborador = colaborador
                registro.sucursal = sucursal
                registro.rol = rol_obj
                registro.fecha = fecha_obj
                registro.hora_entrada = hora_entrada_obj
                registro.hora_salida = hora_salida_obj
                registro.save()

                messages.success(
                    request, "Registro de asistencia actualizado correctamente.")
                return redirect('registroasistencia_list')
            except Exception as e:
                logger.exception(
                    "Error al actualizar el registro de asistencia con id %s", registro_id)
                messages.error(
                    request, "Ocurrió un error al actualizar el registro de asistencia. Por favor, intente de nuevo.")
                return redirect('registroasistencia_list')
        return redirect('registroasistencia_list')
    except Exception as e:
        logger.exception(
            "Error al obtener el registro de asistencia con id %s", registro_id)
        messages.error(
            request, "No se pudo encontrar el registro de asistencia especificado.")
        return redirect('registroasistencia_list')


@login_required
def registroasistencia_inactivate(request, registro_id):
    """
    Marca un registro de asistencia como INACTIVO.
    """
    try:
        registro = get_object_or_404(RegistroAsistencia, pk=registro_id)
        if request.method == 'POST':
            registro.estado = 'INACTIVO'
            registro.save()
            messages.success(
                request, "Registro de asistencia inactivado correctamente.")
            return redirect('registroasistencia_list')
        return redirect('registroasistencia_list')
    except Exception as e:
        logger.exception(
            "Error al inactivar el registro de asistencia con id %s", registro_id)
        messages.error(
            request, "Ocurrió un error al inactivar el registro de asistencia. Por favor, intente de nuevo.")
        return redirect('registroasistencia_list')
