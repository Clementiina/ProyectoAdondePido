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
            name='Persona',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('apellido', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('dni', models.PositiveIntegerField(max_length=8)),
                ('telefono', models.PositiveIntegerField(max_length=16)),
                ('celular', models.PositiveIntegerField(max_length=16)),
                ('direccion', models.CharField(max_length=50)),
                ('id_localidad', models.ForeignKey(to='Localidades.Localidad')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
