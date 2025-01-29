from django.db import models
from django.contrib.auth.models import User
from Apps.permisos.models import Sucursal, Colaboradores, Departamento, Jefes
from datetime import timedelta
from django.utils import timezone

# Create your models here.

'''
class Sucursal(models.Model):
    """Modelo para representar una sucursal"""
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.TextField()
    estado = models.CharField(max_length=8, choices=[(
        'ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], default='ACTIVO')
    creado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='sucursales_creadas')
    actualizado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='sucursales_actualizadas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'sucursales'


class Departamento(models.Model):
    """Modelo para representar un departamento dentro de una sucursal"""
    nombre = models.CharField(max_length=100, unique=True)
    sucursal = models.ForeignKey(
        Sucursal, on_delete=models.CASCADE, related_name='departamentos')
    estado = models.CharField(max_length=8, choices=[(
        'ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], default='ACTIVO')
    creado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='departamentos_creados')
    actualizado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='departamentos_actualizados')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.sucursal})"

    class Meta:
        db_table = 'departamentos'


class Jefe(models.Model):
    """Modelo para representar un jefe"""
    codigo = models.CharField(max_length=50, unique=True)
    identidad = models.CharField(max_length=13, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sucursal = models.ForeignKey(
        Sucursal, on_delete=models.SET_NULL, null=True, blank=True, related_name='jefes')
    estado = models.CharField(max_length=8, choices=[(
        'ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], default='ACTIVO')
    creado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='jefes_creados')
    actualizado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='jefes_actualizados')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.codigo})"

    class Meta:
        db_table = 'jefes'


class Colaborador(models.Model):
    """Modelo para representar un colaborador"""
    codigo = models.CharField(max_length=50, unique=True)
    identidad = models.CharField(max_length=13, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    departamento = models.ForeignKey(
        Departamento, on_delete=models.SET_NULL, null=True, blank=True, related_name='colaboradores')
    estado = models.CharField(max_length=8, choices=[(
        'ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], default='ACTIVO')
    creado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='colaboradores_creados')
    actualizado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='colaboradores_actualizados')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.codigo})"

    class Meta:
        db_table = 'colaboradores'
'''


'''
La seccion de anterior es de prueba
'''

'''
class Rol(models.Model):
    """Modelo para representar roles con horarios"""
    nombre = models.CharField(max_length=100, unique=True)  # Nombre del rol
    descripcion = models.TextField(
        null=True, blank=True)  # Descripción opcional
    hora_inicio_semana = models.TimeField()  # Horario de lunes a viernes (inicio)
    hora_fin_semana = models.TimeField()  # Horario de lunes a viernes (fin)
    hora_inicio_sabado = models.TimeField(
        null=True, blank=True)  # Horario del sábado (opcional)
    hora_fin_sabado = models.TimeField(
        null=True, blank=True)  # Horario del sábado (opcional)
    hora_inicio_domingo = models.TimeField(
        null=True, blank=True)  # Horario del domingo (opcional)
    hora_fin_domingo = models.TimeField(
        null=True, blank=True)  # Horario del domingo (opcional)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'roles'
'''


class Rol(models.Model):
    """Modelo para representar roles con horarios"""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    hora_inicio_semana = models.TimeField()
    hora_fin_semana = models.TimeField()
    hora_inicio_sabado = models.TimeField(null=True, blank=True)
    hora_fin_sabado = models.TimeField(null=True, blank=True)
    hora_inicio_domingo = models.TimeField(null=True, blank=True)
    hora_fin_domingo = models.TimeField(null=True, blank=True)
    estado = models.CharField(max_length=8, choices=[(
        'ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], default='ACTIVO')
    creado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='roles_creados')
    actualizado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='roles_actualizados')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'roles'


class RolAsignado(models.Model):
    """Modelo para asignar roles a empleados en períodos específicos"""
    empleado = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='roles_asignados'
    )  # Empleado al que se asigna el rol
    rol = models.ForeignKey(
        Rol, on_delete=models.CASCADE, related_name='empleados_asignados'
    )  # Rol que se asigna
    fecha_inicio = models.DateField()  # Fecha de inicio del rol
    fecha_fin = models.DateField()  # Fecha de fin del rol

    def __str__(self):
        return f"{self.rol.nombre} asignado a {self.empleado.username}"

    class Meta:
        # Evita duplicados
        unique_together = ('empleado', 'rol', 'fecha_inicio')
        db_table = 'roles_asignados'


'''
class RegistroAsistencia(models.Model):
    """Modelo para registrar asistencia diaria de empleados"""
    empleado = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='registros_asistencia'
    )  # Relación con el empleado
    fecha = models.DateField()  # Fecha del registro
    hora_entrada = models.TimeField(
        null=True, blank=True)  # Hora de entrada registrada
    hora_salida = models.TimeField(
        null=True, blank=True)  # Hora de salida registrada
    # Si cumplió con el horario asignado
    cumplimiento = models.BooleanField(default=False)
    comentario = models.TextField(
        null=True, blank=True)  # Observaciones opcionales

    def __str__(self):
        return f"Asistencia {self.empleado.username} - {self.fecha}"

    class Meta:
        # Un registro por empleado por día
        unique_together = ('empleado', 'fecha')
        db_table = 'registro_asistencias'
'''


class RegistroAsistencia(models.Model):
    """Modelo para registrar asistencia diaria de empleados"""
    colaborador = models.ForeignKey(
        Colaboradores, on_delete=models.CASCADE, related_name='registros_asistencia', null=True)
    sucursal = models.ForeignKey(
        Sucursal, on_delete=models.CASCADE, related_name='asistencias')
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL,
                            null=True, blank=True, related_name='registros_asistencia')
    fecha = models.DateField()
    hora_entrada = models.TimeField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)
    cumplimiento = models.CharField(
        max_length=20,
        choices=[('<', 'Llegó Antes'), ('>', 'Llegó Después'),
                 ('CUMPLIO', 'Cumplió'), ('NO_CUMPLIO', 'No Marcó')],
        default='NO_CUMPLIO'
    )
    total_horas = models.DurationField(null=True, blank=True)
    creado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='asistencias_creadas')
    actualizado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='asistencias_actualizadas')
    fecha_creacion = models.DateTimeField(
        auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def calcular_total_horas(self):
        if self.hora_entrada and self.hora_salida:
            entrada = timedelta(hours=self.hora_entrada.hour,
                                minutes=self.hora_entrada.minute)
            salida = timedelta(hours=self.hora_salida.hour,
                               minutes=self.hora_salida.minute)
            return salida - entrada
        return timedelta()

    def save(self, *args, **kwargs):
        # Determinar si cumple con el horario
        if self.hora_entrada:
            dia_semana = self.fecha.weekday()  # 0: Lunes, ..., 6: Domingo
            if dia_semana < 5:  # Lunes a viernes
                self.cumplimiento = '<' if self.hora_entrada <= self.rol.hora_inicio_semana else '>'
            elif dia_semana == 5:  # Sábado
                if self.rol.hora_inicio_sabado:
                    self.cumplimiento = '<' if self.hora_entrada <= self.rol.hora_inicio_sabado else '>'
            elif dia_semana == 6:  # Domingo
                if self.rol.hora_inicio_domingo:
                    self.cumplimiento = '<' if self.hora_entrada <= self.rol.hora_inicio_domingo else '>'

        # Calcular total de horas trabajadas
        self.total_horas = self.calcular_total_horas()

        # Si no hay hora de entrada o salida, establecer como incumplido
        if not self.hora_entrada or not self.hora_salida:
            self.cumplimiento = 'NO_CUMPLIO'
            self.total_horas = timedelta()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Asistencia {self.colaborador.nombre} {self.fecha}"

    class Meta:
        unique_together = ('colaborador', 'fecha')
        db_table = 'registro_asistencias'
