# Generated by Django 4.1.5 on 2023-02-13 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_fonoaudilogos_preregistrado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preregistro',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='preregistro',
            name='telefono',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='preregistro',
            name='tipo_user',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='comuna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.comuna'),
        ),
    ]
