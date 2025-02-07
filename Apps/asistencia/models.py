from django.db import models
from django.contrib.auth.models import User
from Apps.permisos.models import Sucursal, Colaboradores, Departamento, Jefes, registroPermisos
from Apps.roles.models import Rol, RolAsignado
from datetime import date, datetime, timedelta
from django.utils import timezone

# Create your models here.

class RegistroAsistencia(models.Model):
    """Modelo para registrar asistencia diaria de empleados"""
    colaborador = models.ForeignKey(
        Colaboradores, on_delete=models.CASCADE, related_name='registros_asistencia', null=True)
    sucursal = models.ForeignKey(
        Sucursal, on_delete=models.CASCADE, related_name='asistencias')
    rol = models.ForeignKey(
        Rol, on_delete=models.SET_NULL, null=True, blank=True, related_name='registros_asistencia'
    )
    fecha = models.DateField()
    hora_entrada = models.TimeField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)

    cumplimiento = models.CharField(
        max_length=20,
        choices=[
            ('<', 'Llegó Antes'),
            ('=', 'Llegó Exacto'),  # <-- Nuevo
            ('>', 'Llegó Después'),
            ('CUMPLIO', 'Cumplió'),
            ('NO_CUMPLIO', 'No Marcó')
        ],
        default='NO_CUMPLIO'
    )

    total_horas = models.DurationField(null=True, blank=True)
    # Si la ausencia es justificada por un permiso aprobado
    justificado = models.BooleanField(default=False)

    estado = models.CharField(
        max_length=8,
        choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')],
        default='ACTIVO'
    )  # Control de estado

    # Auditoría
    creado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='asistencias_creadas')
    modificado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='asistencias_actualizadas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def calcular_total_horas(self):
        """Calcula el total de horas trabajadas"""
        if self.hora_entrada and self.hora_salida:
            entrada = timedelta(hours=self.hora_entrada.hour,
                                minutes=self.hora_entrada.minute)
            salida = timedelta(hours=self.hora_salida.hour,
                               minutes=self.hora_salida.minute)
            return salida - entrada
        return timedelta()

    def verificar_permiso(self):
        """Verifica si la ausencia es justificada por un permiso aprobado en ambas fases"""
        permiso_aprobado = registroPermisos.objects.filter(
            codigocolaborador=self.colaborador,
            fecha_inicio__lte=self.fecha,
            fecha_fin__gte=self.fecha,
            estado_inicial="PRE-APROBADO",
            estado_final="APROBADO"
        ).exists()
        self.justificado = permiso_aprobado
    def save(self, *args, **kwargs):
        """Sobrescribe el método save() para aplicar validaciones antes de guardar"""
        self.verificar_permiso()  # Validar si la ausencia es justificada

        # 1) Si hay un permiso justificado, la lógica posterior (cumplimiento) no aplica;
        #    pero si tuvieras otra lógica para permisos, podrías ajustarla aquí.

        if not self.justificado:
            # 2) Verificar si hay rol
            if not self.rol:
                # Si no hay rol (fuera de rango o no asignado), marcamos NO_CUMPLIO
                self.cumplimiento = 'NO_CUMPLIO'

            else:
                # 3) Sí hay rol, checamos la hora de entrada (y el día de la semana)
                dia_semana = self.fecha.weekday()  # 0: Lunes, ..., 6: Domingo
                if self.hora_entrada:
                    if dia_semana < 5:  # Lunes a viernes
                        # Ejemplo: hora_inicio_semana
                        if self.hora_entrada < self.rol.hora_inicio_semana:
                            self.cumplimiento = '<'
                        elif self.hora_entrada == self.rol.hora_inicio_semana:
                            self.cumplimiento = '='
                        else:
                            self.cumplimiento = '>'
                    elif dia_semana == 5 and self.rol.hora_inicio_sabado:
                        if self.hora_entrada < self.rol.hora_inicio_sabado:
                            self.cumplimiento = '<'
                        elif self.hora_entrada == self.rol.hora_inicio_sabado:
                            self.cumplimiento = '='
                        else:
                            self.cumplimiento = '>'
                    elif dia_semana == 6 and self.rol.hora_inicio_domingo:
                        if self.hora_entrada < self.rol.hora_inicio_domingo:
                            self.cumplimiento = '<'
                        elif self.hora_entrada == self.rol.hora_inicio_domingo:
                            self.cumplimiento = '='
                        else:
                            self.cumplimiento = '>'
                    else:
                        # Si es sábado o domingo y no hay hora_inicio_sabado/domingo en el rol
                        self.cumplimiento = 'NO_CUMPLIO'
                else:
                    # No hay hora de entrada => NO_CUMPLIO
                    self.cumplimiento = 'NO_CUMPLIO'

        # 4) Calcular total de horas
        self.total_horas = self.calcular_total_horas()

        # 5) Si falta hora_entrada o hora_salida => NO_CUMPLIO
        if not self.hora_entrada or not self.hora_salida:
            self.cumplimiento = 'NO_CUMPLIO'
            self.total_horas = timedelta()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Asistencia {self.colaborador.nombrecolaborador} {self.fecha}"

    class Meta:
        unique_together = ('colaborador', 'fecha')
        db_table = 'registro_asistencias'
        
        
        


# apps/biometrico/models.py
# class BiometricoAsistencia(models.Model):
#     id = models.AutoField(primary_key=True)
#     mes = models.CharField(max_length=20)
#     sucursal = models.CharField(max_length=100)
#     empresa = models.CharField(max_length=100)
#     ac_no = models.IntegerField()
#     nombre = models.CharField(max_length=255)
#     dni = models.CharField(max_length=20, null=True, blank=True)
#     dia = models.DateField()
#     horario_inicio = models.TimeField()
#     horario_salida = models.TimeField()
#     marcacion_entrada = models.TimeField()
#     marcacion_salida = models.TimeField(null=True, blank=True)
#     falta = models.BooleanField(default=False)
#     tiempo_trabajado = models.TimeField(null=True, blank=True)
#     simbolo = models.CharField(max_length=5, null=True, blank=True)
#     departamento = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'biometrico_asistencias'
#         managed = False  # No se administrará esta tabla con migraciones
#         app_label = 'biometrico'

#     def __str__(self):
#         return f"{self.nombre} - {self.dia}"

    
    
# apps/asistencias/models_sync.py
# from django.db import models

# class BiometricSyncStatus(models.Model):
#     """
#     Modelo para llevar el control incremental de la sincronización de registros biométricos.
#     Se guarda el último ID (de la tabla biométrico) que se procesó y que contaba con hora de salida real.
#     """
#     last_processed_id = models.IntegerField(default=0)

#     def __str__(self):
#         return f"Último ID procesado: {self.last_processed_id}"

#     class Meta:
#         verbose_name = 'Biometric Sync Status'
#         verbose_name_plural = 'Biometric Sync Status'


class CheckInOut(models.Model):
    user_id = models.IntegerField(db_column='USERID')
    checktime = models.DateTimeField(db_column='CHECKTIME')
    checktype = models.CharField(max_length=1, db_column='CHECKTYPE')  # Se asume 'I' o 'O'
    verifycode = models.IntegerField(db_column='VERIFYCODE', null=True, blank=True)
    sensorid = models.CharField(max_length=5, db_column='SENSORID', null=True, blank=True)
    workcode = models.IntegerField(db_column='WorkCode', null=True, blank=True)
    sn = models.CharField(max_length=20, db_column='sn', null=True, blank=True)
    user_ext_fmt = models.SmallIntegerField(db_column='UserExtFmt', null=True, blank=True)

    class Meta:
        db_table = 'CHECKINOUT'
        managed = False  # No administrado por Django
        app_label = 'biometrico'

class UserInfo(models.Model):
    user_id = models.IntegerField(db_column='USERID', primary_key=True)
    badgenumber = models.CharField(max_length=24, db_column='Badgenumber')
    ssn = models.CharField(max_length=20, db_column='SSN', null=True, blank=True)
    name = models.CharField(max_length=40, db_column='NAME', null=True, blank=True)
    # Otros campos se pueden agregar según sea necesario

    class Meta:
        db_table = 'USERINFO'
        managed = False
        app_label = 'biometrico'
