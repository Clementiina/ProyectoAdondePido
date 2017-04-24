# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_unitario', models.FloatField()),
                ('cantidad', models.PositiveIntegerField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_envio', models.DateTimeField()),
                ('fecha_recepcion', models.DateTimeField()),
                ('estado', models.BooleanField(default=True)),
                ('socio', models.ForeignKey(to='distribuidoras.Negocio_Distribuidora')),
            ],
        ),
        migrations.AddField(
            model_name='detalle_pedido',
            name='pedido',
            field=models.ForeignKey(to='pedidos.Pedido'),
        ),
        migrations.AddField(
            model_name='detalle_pedido',
            name='producto',
            field=models.ForeignKey(to='productos.Producto'),
        ),
    ]