# Generated by Django 4.1.7 on 2023-03-31 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partidas',
            old_name='id_usuario',
            new_name='id_usuarios',
        ),
    ]
