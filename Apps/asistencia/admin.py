from django.contrib import admin
from .models import RegistroAsistencia

# Register your models here.
@admin.register(RegistroAsistencia)
class RegistroAsistenciaAdmin(admin.ModelAdmin):
    # list_display = ('empleado', 'fecha', 'hora_entrada',
    #               'hora_salida', 'cumplimiento', 'comentario')
    list_display = ('colaborador', 'sucursal', 'rol', 'fecha', 'hora_entrada', 'hora_salida', 'cumplimiento', 'justificado',
                    'creado_por', 'modificado_por', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('colaborador', 'fecha')
    list_filter = ('fecha', 'hora_entrada', 'hora_salida', 'cumplimiento')
