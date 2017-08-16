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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('capacidad', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('estado', models.BooleanField(default=True)),
                ('marcaSubCategoria', models.ForeignKey(to='categorias.Marca_SubCategoria')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Presentacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_presentacion',
            field=models.ForeignKey(blank=True, to='productos.Tipo_Presentacion'),
        ),
        migrations.AddField(
            model_name='presentacion',
            name='tipo_presentacion',
            field=models.ForeignKey(blank=True, to='productos.Tipo_Presentacion'),
        ),
    ]
