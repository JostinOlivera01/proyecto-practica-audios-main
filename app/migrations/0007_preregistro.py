# Generated by Django 4.1.5 on 2023-02-08 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_fonoaudilogos_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreRegistro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('tipo_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.tipousuario')),
            ],
        ),
    ]