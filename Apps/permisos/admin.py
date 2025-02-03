from django.contrib import admin
from .models import registroPermisos, tiposPermiso, Empresas, Departamento, Jefes, Colaboradores, Unidad_Negocio, Sucursal

# Register your models here.

@admin.register(registroPermisos)
class registroPermisosAdmin(admin.ModelAdmin):
    list_display = ('id_permiso', 'codigocolaborador', 'id_departamento', 'id_empresa', 'id_sucursal', 'id_tipo_permiso', 
                    'colaborador', 'permiso_de', 'fecha_inicio', 'fecha_fin', 'motivo', 'comprobante', 'permiso_firmado',
                    'estado_inicial', 'estado_final', 'creado_por', 'fecha_creacion', 'modificado_por', 'fecha_modificacion')
    search_fields = ('colaborador', 'fecha_inicio', 'fecha_fin')
    list_filter = ('fecha_inicio', 'fecha_fin', 'estado_inicial', 'estado_final')

@admin.register(tiposPermiso)
class TipoPermisoAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_permiso', 'nombre_permiso')
    search_fields = ('nombre_permiso',)
    list_filter = ('nombre_permiso',)
    
@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('nombre_empresa', 'fechacreacion', 'fechaactualizacion', 'estado')
    search_fields = ('nombre_empresa', 'fechacreacion', 'fechaactualizacion')
    list_filter = ('estado',)
    
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_departamento', 'fechacreacion', 'fechaactualizacion', 'estado')
    search_fields = ('nombre_departamento', 'fechacreacion', 'fechaactualizacion')
    list_filter = ('estado',)
    
@admin.register(Jefes)
class JefesAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'identidadjefe', 'nombrejefe', 'fechacreacion', 'fechaactualizacion', 'estado')
    search_fields = ('codigo', 'identidadjefe', 'nombrejefe', 'estado')
    list_filter = ('estado', 'fechacreacion', 'fechaactualizacion')
    
@admin.register(Colaboradores)
class ColaboradoresAdmin(admin.ModelAdmin):
    list_display = ('codigocolaborador', 'empresa', 'sucursal', 'unidad_de_negocio', 'departamento', 'jefe', 'nombrecolaborador', 'estado', 'fechacreacion', 'fechaactualizacion')
    search_fields = ('codigocolaborador', 'nombrecolaborador', 'fechacreacion', 'fechaactualizacion')
    list_filter = ('estado', 'fechacreacion', 'fechaactualizacion')

@admin.register(Unidad_Negocio)
class Unidad_NegocioAdmin(admin.ModelAdmin):
    list_display = ('nombre_unidad_de_negocio', 'fechacreacion', 'fechaactualizacion', 'estado')
    search_fields = ('nombre_unidad_de_negocio', 'fechacreacion', 'fechaactualizacion')
    list_filter = ('estado', 'fechacreacion', 'fechaactualizacion')

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre_sucursal', 'fechacreacion', 'fechaactualizacion', 'estado')
    search_fields = ('nombre_sucursal', 'fechacreacion', 'fechaactualizacion')
    list_filter = ('estado', 'fechacreacion', 'fechaactualizacion')


