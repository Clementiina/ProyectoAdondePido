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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('capacidad', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripsiom', models.TextField()),
                ('precio_unitario', models.FloatField()),
                ('estado', models.BooleanField(default=True)),
                ('id_marcaSubCategoria', models.ForeignKey(to='categorias.Marca_SubCategoria')),
                ('id_presentacion', models.ForeignKey(to='productos.Presentacion')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='id_tipo_producto',
            field=models.ForeignKey(to='productos.Tipo_Producto'),
        ),
    ]
