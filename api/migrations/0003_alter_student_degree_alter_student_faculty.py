# Generated by Django 5.2.1 on 2025-06-02 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_conductor_driver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='faculty',
            field=models.CharField(max_length=100),
        ),
    ]
