# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personas', '0001_initial'),
        ('localidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Negocio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('descripcion', models.TextField(blank=True)),
                ('numero_contacto', models.PositiveIntegerField(blank=True)),
                ('direccion', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('localidad', models.ForeignKey(to='localidades.Localidad')),
                ('persona_cargo', models.ForeignKey(to='personas.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Permiso_Negocio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Negocio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('estado', models.BooleanField(default=True)),
                ('negocio', models.ForeignKey(to='negocios.Negocio')),
                ('permiso', models.ForeignKey(blank=True, to='negocios.Permiso_Negocio')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='usuario_negocio',
            unique_together=set([('negocio', 'usuario', 'permiso')]),
        ),
    ]
