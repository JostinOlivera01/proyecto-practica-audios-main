# Generated by Django 4.1.5 on 2023-01-12 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_media_idpaciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intensidad',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]