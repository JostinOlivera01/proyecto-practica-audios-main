# Generated by Django 4.1.5 on 2023-01-31 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_profesional_paciente_tipo_profesional'),
    ]

    operations = [
        migrations.CreateModel(
            name='App_documento',
            fields=[
                ('id_documento', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=1000)),
                ('documento', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=1000)),
                ('qr', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Diabetes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo_diabetes', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Hipertension',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('estado_hipertension', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Vocalizacion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('timestamp', models.CharField(max_length=100)),
                ('url_audio', models.FileField(upload_to='media')),
                ('duracion', models.CharField(max_length=100)),
                ('bpminute', models.CharField(max_length=100)),
                ('bpmeasure', models.CharField(max_length=100)),
                ('comentario', models.CharField(max_length=100)),
                ('paciente_id_paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='paciente_documento',
            fields=[
                ('id_paciente_documento', models.BigAutoField(primary_key=True, serialize=False)),
                ('autorizado', models.CharField(max_length=100)),
                ('documento_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.app_documento')),
                ('paciente_id_paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Intensidad',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('timestamp', models.CharField(max_length=100)),
                ('url_audio', models.FileField(upload_to='media')),
                ('intensidad', models.CharField(max_length=100)),
                ('mindb', models.CharField(max_length=100)),
                ('maxdb', models.CharField(max_length=100)),
                ('comentario', models.CharField(max_length=100)),
                ('paciente_id_paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.paciente')),
            ],
        ),
        migrations.AlterField(
            model_name='paciente',
            name='diabetes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.diabetes'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='hipertencion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.hipertension'),
        ),
    ]
