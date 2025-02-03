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
        """Verifica si la ausencia es justificada por un permiso aprobado"""
        permiso_aprobado = registroPermisos.objects.filter(
            codigocolaborador=self.colaborador,
            fecha_inicio__lte=self.fecha,
            fecha_fin__gte=self.fecha,
            estado_inicial="Aprobado"
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
