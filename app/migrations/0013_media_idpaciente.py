# Generated by Django 4.1.5 on 2023-01-12 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_paciente_remove_intensidad_idusuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='idPaciente',
            field=models.CharField(default=11111, max_length=100),
            preserve_default=False,
        ),
    ]
