import inflect
from django.core.mail import send_mail
from django.conf import settings


def numero_a_letras(num):
    """Convierte un número en su representación en palabras"""
    p = inflect.engine()
    palabras = p.number_to_words(num, andword='', zero='cero', threshold=None).upper()
    
    return palabras



def enviar_correo_permiso(nuevo_permiso):
    asunto = f"Nuevo Permiso Solicitado por {nuevo_permiso.colaborador}"
    mensaje = f"""
    Se ha registrado una nueva solicitud de permiso:
    
    Colaborador: {nuevo_permiso.colaborador}
    Tipo de Permiso: {nuevo_permiso.id_tipo_permiso.nombre_permiso}
    Fecha de Inicio: {nuevo_permiso.fecha_inicio}
    Fecha de Fin: {nuevo_permiso.fecha_fin}
    Motivo: {nuevo_permiso.motivo}
    
    Por favor, revise esta solicitud en el sistema.
    """
    destinatarios = ['aatorres@uth.hn']  # Correo del administrador o RRHH
    remitente = settings.EMAIL_HOST_USER

    send_mail(asunto, mensaje, remitente, destinatarios)

