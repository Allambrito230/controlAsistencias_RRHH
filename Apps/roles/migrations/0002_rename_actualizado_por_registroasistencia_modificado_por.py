# Generated by Django 5.0.11 on 2025-01-30 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registroasistencia',
            old_name='actualizado_por',
            new_name='modificado_por',
        ),
    ]
