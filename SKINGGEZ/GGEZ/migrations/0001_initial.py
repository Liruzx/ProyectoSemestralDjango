# Generated by Django 4.0.4 on 2022-05-25 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de usuario')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('nombreSkin', models.CharField(max_length=50, verbose_name='Nombre de la skin')),
                ('categoria', models.CharField(max_length=30, verbose_name='Categoria')),
                ('imagenSkin', models.ImageField(null=True, upload_to='skins')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idCliente', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de usuario')),
                ('nombreUsuario', models.CharField(max_length=50, verbose_name='Nombre de usuario')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo')),
                ('fechaNac', models.CharField(max_length=50, verbose_name='Fecha de nacimiento')),
                ('contra', models.CharField(max_length=50, verbose_name='Contraseña')),
            ],
        ),
    ]
