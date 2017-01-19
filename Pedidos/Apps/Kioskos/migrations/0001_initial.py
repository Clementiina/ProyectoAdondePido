# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Localidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kiosko',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('numero_contacto', models.PositiveIntegerField(max_length=16)),
                ('direccion', models.CharField(max_length=50)),
                ('id_localidad', models.ForeignKey(to='Localidades.Localidad')),
                ('persona_cargo', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Permiso_Kiosko',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Kiosko',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('estado', models.BooleanField()),
                ('id_kiosko', models.ForeignKey(to='Kioskos.Kiosko')),
                ('id_permiso', models.ForeignKey(to='Kioskos.Permiso_Kiosko')),
                ('id_usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
