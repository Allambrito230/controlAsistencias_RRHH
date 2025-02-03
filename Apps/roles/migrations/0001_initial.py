# Generated by Django 5.1.5 on 2025-02-03 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('permisos', '0001_initial'),
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
