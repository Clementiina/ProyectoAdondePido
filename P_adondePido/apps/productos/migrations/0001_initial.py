# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacidad', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
                ('marcaSubCategoria', models.ForeignKey(to='categorias.Marca_SubCategoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto_Presentacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('presentacion', models.ForeignKey(to='productos.Presentacion')),
                ('producto', models.ForeignKey(to='productos.Producto')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='producto_presentacion',
            unique_together=set([('producto', 'presentacion')]),
        ),
    ]
