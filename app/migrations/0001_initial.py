# Generated by Django 4.1.6 on 2023-02-21 23:22

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
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
            name='AudiosCoeficientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.CharField(max_length=100)),
                ('nombre_archivo', models.CharField(max_length=100)),
                ('timestamp', models.CharField(max_length=100)),
                ('F0', models.CharField(max_length=100)),
                ('F1', models.CharField(max_length=100)),
                ('F2', models.CharField(max_length=100)),
                ('F3', models.CharField(max_length=100)),
                ('F4', models.CharField(max_length=100)),
                ('Intensidad', models.CharField(max_length=100)),
                ('HNR', models.CharField(max_length=100)),
                ('Local_Jitter', models.CharField(max_length=100)),
                ('Local_Absolute_Jitter', models.CharField(max_length=100)),
                ('Rap_Jitter', models.CharField(max_length=100)),
                ('ppq5_Jitter', models.CharField(max_length=100)),
                ('ddp_Jitter', models.CharField(max_length=100)),
                ('Local_Shimmer', models.CharField(max_length=100)),
                ('Local_db_Shimmer', models.CharField(max_length=100)),
                ('apq3_Shimmer', models.CharField(max_length=100)),
                ('aqpq5_Shimmer', models.CharField(max_length=100)),
                ('apq11_Shimmer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_comuna', models.CharField(max_length=100)),
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
            name='Familiar',
            fields=[
                ('id_familiar', models.BigAutoField(primary_key=True, serialize=False)),
                ('rut_familiar', models.CharField(max_length=100)),
                ('id_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fonoaudilogos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=100)),
                ('NombreCompleto', models.CharField(max_length=100)),
                ('Registro', models.CharField(max_length=100)),
                ('RegionLaboral', models.CharField(max_length=100)),
                ('TituloProfesional', models.CharField(max_length=100)),
                ('preregistrado', models.CharField(max_length=100)),
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
            name='Institucion',
            fields=[
                ('id_institucion', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_institucion', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('comuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('idPaciente', models.BigAutoField(primary_key=True, serialize=False)),
                ('rut_paciente', models.CharField(max_length=100)),
                ('telegram_paciente', models.CharField(max_length=100)),
                ('Observacion', models.CharField(max_length=100)),
                ('diabetes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.diabetes')),
                ('hipertencion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.hipertension')),
                ('id_usuario', models.ForeignKey(limit_choices_to={'id_tipo_user': 1}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempoVocalizacion', models.CharField(max_length=100)),
                ('tiempoIntensidad', models.CharField(max_length=100)),
                ('Descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PreRegistro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('tipo_user', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipoaudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_usuario', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_usuario', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
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
            name='Provincia',
            fields=[
                ('id_provincia', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_provincia', models.CharField(max_length=100)),
                ('id_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.region')),
            ],
        ),
        migrations.CreateModel(
            name='Profesional_salud',
            fields=[
                ('id_profesional', models.BigAutoField(primary_key=True, serialize=False)),
                ('rut_profesional', models.CharField(max_length=100)),
                ('id_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('institucion_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.institucion')),
            ],
        ),
        migrations.CreateModel(
            name='Profesional_Paciente',
            fields=[
                ('id_prof_paci', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('id_paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.paciente')),
                ('id_profesional_salud', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.profesional_salud')),
                ('tipo_profesional', models.ForeignKey(limit_choices_to=models.Q(('id_tipo_user', 1), ('id_tipo_user', 2), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
        migrations.CreateModel(
            name='Familiar_paciente',
            fields=[
                ('id_fam_pac', models.BigAutoField(primary_key=True, serialize=False)),
                ('parentesco', models.CharField(max_length=100)),
                ('id_familiar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.familiar')),
                ('id_paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.paciente')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='id_provincia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.provincia'),
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id_audio', models.BigAutoField(primary_key=True, serialize=False)),
                ('url_audio', models.FileField(upload_to='media')),
                ('timestamp', models.CharField(max_length=100)),
                ('idusuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='comuna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.comuna'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='id_tipo_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.tipousuario'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
