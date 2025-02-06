from django.urls import path
from . import views

urlpatterns = [
    # REGISTRO ASISTENCIA
    path('registros-asistencia/', views.registroasistencia_list,
         name='registroasistencia_list'),
    path('registros-asistencia/create/', views.registroasistencia_create,
         name='registroasistencia_create'),
    path('registros-asistencia/<int:registro_id>/update/',
         views.registroasistencia_update, name='registroasistencia_update'),
    path('registros-asistencia/<int:registro_id>/inactivate/',
         views.registroasistencia_inactivate, name='registroasistencia_inactivate'),
    path('sync-biom/', views.sync_biometrico_view, name='sync_biometrico_view'),
]