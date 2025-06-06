# Generated by Django 5.2.1 on 2025-05-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Conductor',
            new_name='Driver',
        ),
        migrations.RenameModel(
            old_name='PassengerRute',
            new_name='PassengerRoute',
        ),
        migrations.RenameModel(
            old_name='Rute',
            new_name='Route',
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='licence',
            new_name='license',
        ),
        migrations.RenameField(
            model_name='institution',
            old_name='direccion',
            new_name='adreess',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='rute_fk',
            new_name='route_fk',
        ),
        migrations.RenameField(
            model_name='passenger',
            old_name='conductor_fk',
            new_name='driver_fk',
        ),
        migrations.RenameField(
            model_name='passengerroute',
            old_name='rute_fk',
            new_name='route_fk',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='carrer',
            new_name='degree',
        ),
        migrations.RenameField(
            model_name='travel',
            old_name='rute_fk',
            new_name='route_fk',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='direccion',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='celular',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='fecha_registro',
            new_name='registration_date',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='conductor_fk',
            new_name='driver_fk',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('student', 'Estudiante'), ('driver', 'Conductor'), ('institution', 'Institucion'), ('admin', 'Administrador')], max_length=20),
        ),
    ]
