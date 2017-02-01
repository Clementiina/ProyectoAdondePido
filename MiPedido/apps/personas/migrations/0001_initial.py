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
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('apellido', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('dni', models.PositiveIntegerField()),
                ('telefono', models.PositiveIntegerField()),
                ('celular', models.PositiveIntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('id_localidad', models.ForeignKey(to='localidades.Localidad')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
