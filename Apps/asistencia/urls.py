from django.urls import path
from . import views

urlpatterns = [
# Renderiza la plantilla principal (tabla con DataTables)
    path('registros-asistencia/', views.registroasistencia_list, name='registroasistencia_list'),

    # Endpoint DataTables (Server-Side)
    path('registros-asistencia/api/', views.registroasistencia_list_api, name='registroasistencia_list_api'),

    # Endpoint AJAX para obtener el detalle de un registro (para editar).
    path('registros-asistencia/<int:registro_id>/detail/', views.registroasistencia_detail, name='registroasistencia_detail'),

    # Crear
    path('registros-asistencia/create/', views.registroasistencia_create, name='registroasistencia_create'),
    # Actualizar
    path('registros-asistencia/<int:registro_id>/update/', views.registroasistencia_update, name='registroasistencia_update'),
    # Inactivar
    path('registros-asistencia/<int:registro_id>/inactivate/', views.registroasistencia_inactivate, name='registroasistencia_inactivate'),

    # Sincronizar datos biométrico
    path('sync-biom/', views.sync_biometrico_view, name='sync_biometrico_view'),
    
    #Exportar datos en excel
    path('exportar-asistencias/', views.exportar_asistencias_excel, name='exportar-asistencias'),
]