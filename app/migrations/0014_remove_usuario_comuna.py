# Generated by Django 4.1.5 on 2023-02-13 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_preregistro_email_alter_preregistro_telefono_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='comuna',
        ),
    ]