# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields
from django.conf import settings
import apps.distribuidoras.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categorias', '0001_initial'),
        ('negocios', '0001_initial'),
        ('personas', '0001_initial'),
        ('localidades', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('imagen', models.ImageField(null=True, upload_to=apps.distribuidoras.models.Anuncio.url, blank=True)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria_Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('numero_contacto', models.PositiveIntegerField(verbose_name='Numero de contacto')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('estado', models.BooleanField(default=True)),
                ('localidad', models.ForeignKey(to='localidades.Localidad', verbose_name='Localidad')),
                ('persona_cargo', models.ForeignKey(to='personas.Persona', verbose_name='Persona a cargo')),
            ],
        ),
        migrations.CreateModel(
            name='MarcaXSubcategoria_Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('estado', models.BooleanField(default=True)),
                ('distribuidora', models.ForeignKey(to='distribuidoras.Distribuidora')),
                ('marcaSubCategoria', models.ForeignKey(to='categorias.Marca_SubCategoria')),
            ],
        ),
        migrations.CreateModel(
            name='Negocio_Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto_Distribudora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('precio_unitario', models.FloatField()),
                ('stock', models.PositiveIntegerField()),
                ('estado', models.BooleanField(default=True)),
                ('distribuidora', models.ForeignKey(to='distribuidoras.Distribuidora')),
                ('marcaXSubcategoriaDistribuidora', models.ForeignKey(to='distribuidoras.MarcaXSubcategoria_Distribuidora')),
                ('presentacion', models.ForeignKey(to='productos.Presentacion')),
                ('producto', models.ForeignKey(to='productos.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('recorrido', models.TextField()),
                ('dia', multiselectfield.db.fields.MultiSelectField(max_length=20, choices=[('lu', 'Lunes'), ('ma', 'Martes'), ('mi', 'Miercoles'), ('ju', 'Jueves'), ('vi', 'Viernes'), ('sa', 'Sabado'), ('do', 'Domingo')])),
                ('estado', models.BooleanField(default=True)),
                ('distribuidora', models.ForeignKey(to='distribuidoras.Distribuidora')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Distribuidora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('estado', models.BooleanField(default=True)),
                ('distribuidora', models.ForeignKey(to='distribuidoras.Distribuidora', verbose_name='Distribuidora')),
                ('permiso', models.ForeignKey(verbose_name='Permiso', to='distribuidoras.Permiso_Distribuidora', blank=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='negocio_distribuidora',
            name='ruta',
            field=models.ForeignKey(null=True, to='distribuidoras.Ruta', blank=True),
        ),
        migrations.AddField(
            model_name='categoria_distribuidora',
            name='distribuidora',
            field=models.ForeignKey(to='distribuidoras.Distribuidora'),
        ),
        migrations.AddField(
            model_name='categoria_distribuidora',
            name='tipo_distribuidora',
            field=models.ForeignKey(to='distribuidoras.Tipo_Distribuidora'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='distribuidora',
            field=models.ForeignKey(to='distribuidoras.Distribuidora'),
        ),
        migrations.AlterUniqueTogether(
            name='usuario_distribuidora',
            unique_together=set([('distribuidora', 'usuario', 'permiso')]),
        ),
        migrations.AlterUniqueTogether(
            name='producto_distribudora',
            unique_together=set([('distribuidora', 'marcaXSubcategoriaDistribuidora', 'producto', 'presentacion')]),
        ),
        migrations.AlterUniqueTogether(
            name='negocio_distribuidora',
            unique_together=set([('negocio', 'distribuidora')]),
        ),
        migrations.AlterUniqueTogether(
            name='marcaxsubcategoria_distribuidora',
            unique_together=set([('distribuidora', 'marcaSubCategoria')]),
        ),
        migrations.AlterUniqueTogether(
            name='categoria_distribuidora',
            unique_together=set([('distribuidora', 'tipo_distribuidora')]),
        ),
    ]
