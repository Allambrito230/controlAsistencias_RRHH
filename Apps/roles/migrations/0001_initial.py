# Generated by Django 5.0.11 on 2025-01-29 21:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('permisos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('hora_inicio_semana', models.TimeField()),
                ('hora_fin_semana', models.TimeField()),
                ('hora_inicio_sabado', models.TimeField(blank=True, null=True)),
                ('hora_fin_sabado', models.TimeField(blank=True, null=True)),
                ('hora_inicio_domingo', models.TimeField(blank=True, null=True)),
                ('hora_fin_domingo', models.TimeField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], default='ACTIVO', max_length=8)),
                ('creado_por', models.CharField(default='SISTEMA', max_length=100)),
                ('modificado_por', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='RegistroAsistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora_entrada', models.TimeField(blank=True, null=True)),
                ('hora_salida', models.TimeField(blank=True, null=True)),
                ('cumplimiento', models.CharField(choices=[('<', 'Llegó Antes'), ('>', 'Llegó Después'), ('CUMPLIO', 'Cumplió'), ('NO_CUMPLIO', 'No Marcó')], default='NO_CUMPLIO', max_length=20)),
                ('total_horas', models.DurationField(blank=True, null=True)),
                ('justificado', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('actualizado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='asistencias_actualizadas', to=settings.AUTH_USER_MODEL)),
                ('colaborador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registros_asistencia', to='permisos.colaboradores')),
                ('creado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='asistencias_creadas', to=settings.AUTH_USER_MODEL)),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistencias', to='permisos.sucursal')),
                ('rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registros_asistencia', to='roles.rol')),
            ],
            options={
                'db_table': 'registro_asistencias',
                'unique_together': {('colaborador', 'fecha')},
            },
        ),
        migrations.CreateModel(
            name='RolAsignado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.CharField(choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], default='ACTIVO', max_length=8)),
                ('creado_por', models.CharField(default='SISTEMA', max_length=100)),
                ('modificado_por', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles_asignados', to='permisos.colaboradores')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colaboradores_asignados', to='roles.rol')),
            ],
            options={
                'db_table': 'roles_asignados',
                'unique_together': {('colaborador', 'rol', 'fecha_inicio')},
            },
        ),
    ]
