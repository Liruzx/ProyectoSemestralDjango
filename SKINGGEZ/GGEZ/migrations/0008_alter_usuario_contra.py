# Generated by Django 4.0.4 on 2022-06-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GGEZ', '0007_alter_juego_imagenjuego_alter_juego2_imagenjuego2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='contra',
            field=models.CharField(max_length=50, verbose_name='Contraseña'),
        ),
    ]