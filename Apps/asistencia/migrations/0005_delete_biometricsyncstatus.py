# Generated by Django 5.0.11 on 2025-02-05 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0004_biometricsyncstatus_delete_employeemapping'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BiometricSyncStatus',
        ),
    ]
