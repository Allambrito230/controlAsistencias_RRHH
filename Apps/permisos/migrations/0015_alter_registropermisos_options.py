# Generated by Django 5.0.11 on 2025-02-07 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permisos', '0014_alter_jefes_identidadjefe'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registropermisos',
            options={'permissions': [('view_permisos_empleados', 'Puede ver permisos de empleados a su cargo'), ('view_todos_permisos', 'Puede ver todos los permisos'), ('gestionar_permisos', 'Puede aprobar/rechazar permisos')]},
        ),
    ]
