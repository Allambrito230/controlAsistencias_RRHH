from django.db import models
from django.contrib.auth.models import User
import os
from django.utils import timezone
from datetime import time, datetime

# Create your models here.


class tiposPermiso(models.Model):
    id_tipo_permiso = models.AutoField(primary_key=True)
    nombre_permiso = models.CharField(max_length=50)

    class Meta:
        db_table = 'tipos_de_permisos'

def comprobante_path(instance, filename):
    codigocolaborador = instance.codigocolaborador.codigocolaborador
    fecha_actual = datetime.now().strftime("%d%m%Y")
    extension = os.path.splitext(filename)[1]
    nuevo_nombre = f"COMPROBANTE-{codigocolaborador}_{fecha_actual}{extension}"
    return f"permisos/comprobantes/{nuevo_nombre}"


def permiso_firmado_path(instance, filename):
    codigocolaborador = instance.codigocolaborador.codigocolaborador
    fecha_actual = datetime.now().strftime("%d%m%Y")
    extension = os.path.splitext(filename)[1]
    nombre_permiso_firmado = f"PERMISO-FIRMADO-{codigocolaborador}_{fecha_actual}{extension}"
    
    return os.path.join("permisos/permisosFirmados", nombre_permiso_firmado)


class registroPermisos(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    codigocolaborador = models.ForeignKey(
        'colaboradores', on_delete=models.CASCADE)
    id_departamento = models.ForeignKey(
        'departamento', on_delete=models.CASCADE)
    id_empresa = models.ForeignKey(
        'empresas', null=True, blank=True, on_delete=models.CASCADE)
    id_sucursal = models.ForeignKey(
        'sucursal',  null=True, blank=True, on_delete=models.CASCADE)
    id_tipo_permiso = models.ForeignKey(
        'tiposPermiso', on_delete=models.CASCADE)
    colaborador = models.TextField(max_length=255, null=True, blank=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    permiso_de = models.CharField(max_length=50)  # Dias o Horas
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    motivo = models.TextField(max_length=255)
    comprobante = models.FileField(
        upload_to=comprobante_path, blank=True, null=True)
    permiso_firmado = models.FileField(
        upload_to=permiso_firmado_path, blank=True, null=True)
    estado_inicial = models.CharField(max_length=20, default='PENDIENTE')
    estado_final = models.CharField(max_length=20, default='PENDIENTE')
    descripcion = models.CharField(max_length=100, default='PENDIENTE')
    creado_por = models.CharField(max_length=100, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    modificado_por = models.CharField(max_length=100, null=True, blank=True)
    fecha_modificacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'permisos'

    def save(self, *args, **kwargs):
        """ Antes de guardar, asegurarse de que el campo 'codigo' almacene el código del colaborador """
        if self.codigocolaborador:
            self.codigo = self.codigocolaborador.codigocolaborador
        super().save(*args, **kwargs)



# ----------- Empresas ----------- #
class Empresas(models.Model):
    nombre_empresa = models.CharField(max_length=255)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    fechaactualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(
        max_length=8,
        choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')],
        default='ACTIVO'
    )

    def __str__(self):
        return self.nombre_empresa

    class Meta:
        db_table = 'empresas'


class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(max_length=255)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    fechaactualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(
        max_length=8,
        choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')],
        default='ACTIVO'
    )

    def __str__(self):
        return self.nombre_departamento

    class Meta:
        db_table = 'departamento'


class Jefes(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='jefe')
    codigo = models.CharField(max_length=20, null=True, blank=True)
    identidadjefe = models.CharField(max_length=13, null=True, blank=True)
    nombrejefe = models.CharField(max_length=255, null=True, blank=True)
    correo = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(
        max_length=8,
        choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')],
        default='ACTIVO'
    )
    fechacreacion = models.DateTimeField(auto_now_add=True)
    fechaactualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombrejefe

    class Meta:
        db_table = 'jefes'


class Colaboradores(models.Model):
    codigocolaborador = models.CharField(max_length=20, null=True, blank=True)
    empresa = models.ForeignKey(
        'Empresas',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='colaboradores'
    )
    sucursal = models.ForeignKey(
        'Sucursal',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='colaboradores'
    )
    unidad_de_negocio = models.ForeignKey(
        'Unidad_Negocio',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='colaboradores'
    )
    departamento = models.ForeignKey(
        'Departamento',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='colaboradores'
    )
    jefe = models.ForeignKey(
        'Jefes',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='colaboradores'
    )
    nombrecolaborador = models.CharField(max_length=255, null=True, blank=True)
    correo = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(
        max_length=8,
        choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')],
        default='ACTIVO'
    )
    fechacreacion = models.DateTimeField(auto_now_add=True)
    fechaactualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.empresa} - {self.nombrecolaborador}"

    class Meta:
        db_table = 'colaboradores'


class Unidad_Negocio(models.Model):
    nombre_unidad_de_negocio = models.CharField(max_length=255)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    fechaactualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(
        max_length=8,
        choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')],
        default='ACTIVO'
    )

    def __str__(self):
        return self.nombre_unidad_de_negocio

    class Meta:
        db_table = 'unidad_de_negocio'


class Sucursal(models.Model):
    nombre_sucursal = models.CharField(max_length=255)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    fechaactualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(
        max_length=8,
        choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')],
        default='ACTIVO'
    )

    def __str__(self):
        return self.nombre_sucursal

    class Meta:
        db_table = 'sucursal'


def politicas_path(instance, filename):
    return f"politicas"
