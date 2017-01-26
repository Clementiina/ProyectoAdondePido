# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('capacidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripsiom', models.TextField()),
                ('precio_unitario', models.FloatField()),
                ('id_marcaSubCategoria', models.ForeignKey(to='Categorias.Marca_SubCategoria')),
                ('id_presentacion', models.ForeignKey(to='Productos.Presentacion')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Producto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='id_tipo',
            field=models.ForeignKey(to='Productos.Tipo_Producto'),
        ),
    ]
