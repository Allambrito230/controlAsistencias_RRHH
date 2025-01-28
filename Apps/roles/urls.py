from django.urls import path
from . import views

urlpatterns = [
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

]
