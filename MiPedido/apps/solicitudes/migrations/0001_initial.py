# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('localidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribuidora_Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distribuidora', models.ForeignKey(to='distribuidoras.Distribuidora')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(max_length=50)),
                ('dni', models.BigIntegerField()),
                ('telefono', models.BigIntegerField(blank=True)),
                ('celular', models.BigIntegerField(blank=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('numero_contacto', models.BigIntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=1, choices=[('p', 'Pendiente'), ('a', 'Activo')])),
                ('localidad', models.ForeignKey(default=3935, to='localidades.Localidad')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='distribuidora_solicitud',
            name='solicitud',
            field=models.ForeignKey(to='solicitudes.Solicitud'),
        ),
    ]
