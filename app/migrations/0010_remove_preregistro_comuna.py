# Generated by Django 4.1.5 on 2023-02-13 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_password_preregistro_telefono_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preregistro',
            name='comuna',
        ),
    ]