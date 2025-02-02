from django.urls import path
from . import views

urlpatterns = [
    # ROL
    path('roles/', views.rol_list, name='rol_list'),
    path('roles/create/', views.rol_create, name='rol_create'),
    path('roles/<int:rol_id>/update/', views.rol_update, name='rol_update'),
    path('roles/<int:rol_id>/inactivate/',
         views.rol_inactivate, name='rol_inactivate'),

    # ROL ASIGNADO
    path('roles-asignados/', views.rolasignado_list, name='rolasignado_list'),
    path('roles-asignados/create/', views.rolasignado_create,
         name='rolasignado_create'),
    path('roles-asignados/<int:rolasignado_id>/update/',
         views.rolasignado_update, name='rolasignado_update'),
    path('roles-asignados/<int:rolasignado_id>/inactivate/',
         views.rolasignado_inactivate, name='rolasignado_inactivate'),

    # REGISTRO ASISTENCIA
    path('registros-asistencia/', views.registroasistencia_list,
         name='registroasistencia_list'),
    path('registros-asistencia/create/', views.registroasistencia_create,
         name='registroasistencia_create'),
    path('registros-asistencia/<int:registro_id>/update/',
         views.registroasistencia_update, name='registroasistencia_update'),
    path('registros-asistencia/<int:registro_id>/inactivate/',
         views.registroasistencia_inactivate, name='registroasistencia_inactivate'),
]
'''
    # Gestión de roles
    path('roles/crear/', views.crear_rol, name='crear_rol'),
    path('roles/', views.listar_roles, name='listar_roles'),

    # Asignación de roles
    path('roles/asignar/', views.asignar_rol, name='asignar_rol'),
    path('roles/asignados/', views.listar_roles_asignados,
         name='listar_roles_asignados'),

    # Registro de asistencias
    path('asistencias/registrar/', views.registrar_asistencia,
         name='registrar_asistencia'),
         
    path('asistencias/', views.listar_asistencias, name='listar_asistencias'),
    # Gestión de sucursales
    path('sucursales/', views.sucursales, name='sucursales'),

    # Gestión de departamentos
    path('departamentos/', views.departamentos, name='departamentos'),

    # Gestión de colaboradores
    path('colaboradores/', views.colaboradores, name='colaboradores'),

    # Gestión de jefes
    path('jefes/', views.jefes, name='jefes'),

    # Registro y listado de asistencias
    path('registro_asistencia/', views.registro_asistencia,
         name='registro_asistencia'),
'''
