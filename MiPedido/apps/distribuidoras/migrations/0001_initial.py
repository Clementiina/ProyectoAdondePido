# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 03:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '__first__'),
        ('localidades', '__first__'),
        ('negocios', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.CharField(choices=[('l', 'Listo'), ('v', 'vigente'), ('f', 'finalizado')], max_length=1)),
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
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localidades.Localidad', verbose_name='Localidad')),
                ('persona_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.Persona', verbose_name='Persona a cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Negocio_Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias_distribuidora', models.CharField(blank=True, max_length=50)),
                ('alias_negocio', models.CharField(blank=True, max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('distribuidora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distribuidoras.Distribuidora')),
                ('negocio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='negocios.Negocio')),
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
                ('distribudora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distribuidoras.Distribuidora')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('recorrido', models.TextField()),
                ('dia', models.CharField(choices=[('lu', 'Lunes'), ('ma', 'Martes'), ('mi', 'Miercoles'), ('ju', 'Jueves'), ('vi', 'Viernes'), ('sa', 'Sabado'), ('do', 'Domingo')], max_length=2)),
                ('estado', models.BooleanField(default=True)),
                ('distribuidora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distribuidoras.Distribuidora')),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto_Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('distribuidora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distribuidoras.Distribuidora')),
                ('tipoProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Tipo_Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('distribuidora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distribuidoras.Distribuidora', verbose_name='Distribuidora')),
                ('permiso', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='distribuidoras.Permiso_Distribuidora', verbose_name='Permiso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='negocio_distribuidora',
            name='ruta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='distribuidoras.Ruta'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='distribuidora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distribuidoras.Distribuidora'),
        ),
        migrations.AlterUniqueTogether(
            name='negocio_distribuidora',
            unique_together=set([('negocio', 'distribuidora')]),
        ),
    ]
