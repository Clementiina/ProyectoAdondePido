# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('localidades', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kioskos', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('imagen', models.ImageField(upload_to='')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('fecha_ini', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('estado', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Distribuidora',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('numero_contacto', models.PositiveIntegerField()),
                ('direccion', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('id_localidad', models.ForeignKey(to='localidades.Localidad')),
                ('persona_cargo', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Kiosko_Distribuidora',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('alias_distribuidora', models.CharField(max_length=50)),
                ('alias_kiosko', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('id_kiosko', models.ForeignKey(to='kioskos.Kiosko')),
            ],
        ),
        migrations.CreateModel(
            name='Permiso_Distribuidora',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto_Distribudora',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('stock', models.PositiveIntegerField()),
                ('estado', models.BooleanField(default=True)),
                ('id_distribudora', models.ForeignKey(to='distribuidoras.Distribuidora')),
                ('id_producto', models.ForeignKey(to='productos.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('recorrido', models.TextField()),
                ('dia', models.CharField(max_length=1)),
                ('estado', models.BooleanField(default=True)),
                ('id_distribuidora', models.ForeignKey(to='distribuidoras.Distribuidora')),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto_Distribuidora',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('estado', models.BooleanField(default=True)),
                ('id_distribuidora', models.ForeignKey(to='distribuidoras.Distribuidora')),
                ('id_tipoProducto', models.ForeignKey(to='productos.Tipo_Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Distribuidora',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('estado', models.BooleanField(default=True)),
                ('id_distribuidora', models.ForeignKey(to='distribuidoras.Distribuidora')),
                ('id_permiso', models.ForeignKey(to='distribuidoras.Permiso_Distribuidora')),
                ('id_usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='kiosko_distribuidora',
            name='id_ruta',
            field=models.ForeignKey(to='distribuidoras.Ruta'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='id_distribuidora',
            field=models.ForeignKey(to='distribuidoras.Distribuidora'),
        ),
    ]
