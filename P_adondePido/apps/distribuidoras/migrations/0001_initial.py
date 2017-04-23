# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.distribuidoras.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
        ('productos', '0001_initial'),
        ('negocios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('localidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to=apps.distribuidoras.models.Anuncio.url, blank=True, null=True)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('numero_contacto', models.PositiveIntegerField(verbose_name='Numero de contacto')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('estado', models.BooleanField(default=True)),
                ('localidad', models.ForeignKey(verbose_name='Localidad', to='localidades.Localidad')),
                ('persona_cargo', models.ForeignKey(verbose_name='Persona a cargo', to='personas.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Negocio_Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias_distribuidora', models.CharField(max_length=50, blank=True)),
                ('alias_negocio', models.CharField(max_length=50, blank=True)),
                ('estado', models.BooleanField(default=True)),
                ('distribuidora', models.ForeignKey(to='distribuidoras.Distribuidora')),
                ('negocio', models.ForeignKey(to='negocios.Negocio')),
            ],
        ),
        migrations.CreateModel(
            name='Permiso_Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto_Distribudora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.PositiveIntegerField()),
                ('estado', models.BooleanField(default=True)),
                ('distribudora', models.ForeignKey(to='distribuidoras.Distribuidora')),
                ('producto', models.ForeignKey(to='productos.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('recorrido', models.TextField()),
                ('dia', models.CharField(max_length=2, choices=[('lu', 'Lunes'), ('ma', 'Martes'), ('mi', 'Miercoles'), ('ju', 'Jueves'), ('vi', 'Viernes'), ('sa', 'Sabado'), ('do', 'Domingo')])),
                ('estado', models.BooleanField(default=True)),
                ('distribuidora', models.ForeignKey(to='distribuidoras.Distribuidora')),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto_Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('distribuidora', models.ForeignKey(to='distribuidoras.Distribuidora')),
                ('tipoProducto', models.ForeignKey(to='productos.Tipo_Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('distribuidora', models.ForeignKey(verbose_name='Distribuidora', to='distribuidoras.Distribuidora')),
                ('permiso', models.ForeignKey(verbose_name='Permiso', blank=True, to='distribuidoras.Permiso_Distribuidora')),
                ('usuario', models.ForeignKey(verbose_name='Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='negocio_distribuidora',
            name='ruta',
            field=models.ForeignKey(blank=True, null=True, to='distribuidoras.Ruta'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='id_distribuidora',
            field=models.ForeignKey(to='distribuidoras.Distribuidora'),
        ),
        migrations.AlterUniqueTogether(
            name='negocio_distribuidora',
            unique_together=set([('negocio', 'distribuidora')]),
        ),
    ]
