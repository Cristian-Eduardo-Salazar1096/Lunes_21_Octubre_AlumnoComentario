# Generated by Django 5.1.2 on 2024-10-15 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumno',
            options={'verbose_name': 'Alumno', 'verbose_name_plural': 'Alumnos'},
        ),
        migrations.AlterModelTable(
            name='alumno',
            table='Alumnos',
        ),
    ]
