# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Kioskos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Productos', '0001_initial'),
        ('Localidades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('fecha_ini', models.DateTimeField()),
                ('fecha_end', models.DateTimeField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Distribudora',
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
            name='Kiosko_Distribudora',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('alias_distribudora', models.CharField(max_length=50)),
                ('alias_kiosko', models.CharField(max_length=50)),
                ('id_kiosko', models.ForeignKey(to='Kioskos.Kiosko')),
            ],
        ),
        migrations.CreateModel(
            name='Permiso_Distribudora',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto_Distribudora',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('stock', models.PositiveIntegerField(max_length=10)),
                ('id_distribudora', models.ForeignKey(to='Distribudoras.Distribudora')),
                ('id_producto', models.ForeignKey(to='Productos.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('recorrido', models.TextField()),
                ('dia', models.CharField(max_length=1)),
                ('id_distribudora', models.ForeignKey(to='Distribudoras.Distribudora')),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto_Distribudora',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('fecha_ini', models.DateTimeField()),
                ('id_distribudora', models.ForeignKey(to='Distribudoras.Distribudora')),
                ('id_tipoProducto', models.ForeignKey(to='Productos.Tipo_Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Distribudora',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('estado', models.BooleanField()),
                ('id_distribudora', models.ForeignKey(to='Distribudoras.Distribudora')),
                ('id_permiso', models.ForeignKey(to='Distribudoras.Permiso_Distribudora')),
                ('id_usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='kiosko_distribudora',
            name='id_ruta',
            field=models.ForeignKey(to='Distribudoras.Ruta'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='id_distribudora',
            field=models.ForeignKey(to='Distribudoras.Distribudora'),
        ),
    ]
