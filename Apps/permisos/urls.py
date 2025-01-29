from django.urls import path
from . import views
from . views import exportar_permisos_excel


urlpatterns = [
    path('solicitud/', views.permisos_registro_view, name='permisos_solicitud'),
    # path('verificar_solicitud_activa/', views.verificar_solicitud_activa_view, name='verificar_solicitud_activa'),
    # path('Permisos/solicitud/exito/', views.exito_view, name='permisos_solicitud_exito'),

    path('Permisos/permisos_gestion',
         views.permisos_gestion_view, name='permisos_gestion'),
    path('permisos_historial/', views.permisos_historial_view,
         name='permisos_historial'),
    path('Listas/departamentosJson/',
         views.lista_departamentos_view, name='lista_departamentos'),
    path('Listas/empresasJson/', views.lista_empresas_view, name='lista_empresas'),
    path('Listas/sucursalesJson/',
         views.lista_sucursales_view, name='lista_sucursales'),
    path('colaboradores/<int:departamento_id>/',
         views.colaboradores_por_departamento_view, name='colaboradores_por_departamento'),

    path("exportar_permisos_excel/", exportar_permisos_excel,
         name="exportar_permisos_excel"),
]
