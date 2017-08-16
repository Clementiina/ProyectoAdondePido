# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('distribuidoras', '0001_initial'),
        ('localidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribuidora_Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('distribuidora', models.ForeignKey(to='distribuidoras.Distribuidora')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=70)),
                ('code', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dni', models.BigIntegerField()),
                ('telefono', models.BigIntegerField(blank=True)),
                ('celular', models.BigIntegerField(blank=True)),
                ('n_nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('numero_contacto', models.BigIntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('localidad', models.ForeignKey(default=3935, to='localidades.Localidad')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='distribuidora_solicitud',
            name='solicitud',
            field=models.ForeignKey(to='solicitudes.Solicitud'),
        ),
    ]
