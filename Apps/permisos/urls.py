from django.urls import path
from . import views
from . views import exportar_permisos_excel


urlpatterns = [

    path('solicitud/', views.permisos_registro_view, name='permisos_solicitud'),
    path('permisos_gestion', views.permisos_gestion_view, name='permisos_gestion'),
    path('permisos_historial/', views.permisos_historial_view,name='permisos_historial'),
    path('permisos_aprobados/', views.permisos_aprobados_view,name='permisos_aprobados'),
    path('Listas/departamentosJson/', views.lista_departamentos_view, name='lista_departamentos'),
    path('Listas/empresasJson/', views.lista_empresas_view, name='lista_empresas'),
    path('comprobantes/', views.cargar_comprobantes_view, name='comprobantes'),
    path('Listas/sucursalesJson/', views.lista_sucursales_view, name='lista_sucursales'),
    path('colaboradores/<int:departamento_id>/', views.colaboradores_por_departamento_view, name='colaboradores_por_departamento'),
    path('exportar_excel/', exportar_permisos_excel, name='exportar_permisos_excel'),

    path('permisos-pendientes/', views.permisos_pendientes_view, name="permisos_pendientes"),
    path('actualizar_estado_jefe/', views.actualizar_estado_jefe, name="actualizar_estado_jefe"),
    path('actualizar_estado_rrhh/', views.actualizar_estado_rrhh, name="actualizar_estado_rrhh"),
    #path('actualizar-permiso/', views.actualizar_estado_permiso, name="actualizar-permiso"),
    path('verificar-colaborador/', views.verificar_colaborador_view, name="verificar_colaborador"),
    path('colaboradores_con_permiso/', views.colaboradores_con_permisos, name='colaboradores_con_permisos'),
    path('guardar_comprobante/', views.guardar_comprobante, name='guardar_comprobante'),

]
