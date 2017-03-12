# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 03:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('localidades', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.BigIntegerField()),
                ('telefono', models.BigIntegerField()),
                ('celular', models.BigIntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localidades.Localidad')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
