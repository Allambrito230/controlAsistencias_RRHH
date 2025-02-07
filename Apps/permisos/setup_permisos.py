from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import registroPermisos

def configurar_grupos():
    # Crear o recuperar grupos existentes
    grupo_jefes, _ = Group.objects.get_or_create(name='Jefes')
    grupo_rrhh, _ = Group.objects.get_or_create(name='RRHH')
    grupo_gestores, _ = Group.objects.get_or_create(name='Gestores de Permisos')
    grupo_comprobantes, _ = Group.objects.get_or_create(name='Usuarios de Comprobantes')

    # Obtener permisos relacionados con los permisos laborales
    permisos = Permission.objects.filter(content_type=ContentType.objects.get_for_model(registroPermisos))

    # permisos específicos a cada grupo
    grupo_jefes.permissions.set(permisos.filter(codename="view_permisos_empleados"))
    grupo_gestores.permissions.set(permisos.filter(codename="view_permisos_empleados"))
    grupo_rrhh.permissions.set(permisos.filter(codename__in=["view_todos_permisos", "gestionar_permisos"]))
    grupo_comprobantes.permissions.set(permisos.filter(codename="view_comprobantes"))

    print("Grupos y permisos configurados correctamente.")

if __name__ == "__main__":
    configurar_grupos()
