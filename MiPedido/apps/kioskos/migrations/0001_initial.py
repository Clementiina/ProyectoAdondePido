# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('localidades', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kiosko',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('numero_contacto', models.PositiveIntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('id_localidad', models.ForeignKey(to='localidades.Localidad')),
                ('persona_cargo', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Permiso_Kiosko',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Kiosko',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('estado', models.BooleanField(default=True)),
                ('id_kiosko', models.ForeignKey(to='kioskos.Kiosko')),
                ('id_permiso', models.ForeignKey(to='kioskos.Permiso_Kiosko')),
                ('id_usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
