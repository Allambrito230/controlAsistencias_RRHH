# Generated by Django 5.1.5 on 2025-02-03 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asistencia', '0001_initial'),
        ('permisos', '0001_initial'),
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registroasistencia',
            name='rol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registros_asistencia', to='roles.rol'),
        ),
        migrations.AddField(
            model_name='registroasistencia',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistencias', to='permisos.sucursal'),
        ),
        migrations.AlterUniqueTogether(
            name='registroasistencia',
            unique_together={('colaborador', 'fecha')},
        ),
    ]
