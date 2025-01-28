from django.contrib import admin
from .models import Rol, RolAsignado, RegistroAsistencia

# Register your models here.


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'hora_inicio_semana', 'hora_fin_semana',
                    'hora_inicio_sabado', 'hora_fin_sabado', 'hora_inicio_domingo', 'hora_fin_domingo')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('hora_inicio_semana', 'hora_inicio_sabado')


@admin.register(RolAsignado)
class RolAsignadoAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'rol', 'fecha_inicio', 'fecha_fin')
    search_fields = ('empleado', 'rol')
    list_filter = ('fecha_inicio', 'fecha_fin')


@admin.register(RegistroAsistencia)
class RegistroAsistenciaAdmin(admin.ModelAdmin):
    # list_display = ('empleado', 'fecha', 'hora_entrada',
    #               'hora_salida', 'cumplimiento', 'comentario')
    list_display = ('colaborador', 'sucursal', 'rol', 'fecha', 'hora_entrada', 'hora_salida', 'cumplimiento',
                    'total_horas', 'creado_por', 'actualizado_por', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('colaborador', 'fecha')
    list_filter = ('fecha', 'hora_entrada', 'hora_salida', 'cumplimiento')
