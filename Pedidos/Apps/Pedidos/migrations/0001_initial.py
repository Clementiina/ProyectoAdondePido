# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0001_initial'),
        ('Distribudoras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Pedido',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('precio_unitario', models.FloatField()),
                ('cantidad', models.PositiveIntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Pedido',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('fecha_envio', models.DateTimeField()),
                ('fecha_recepcion', models.DateTimeField()),
                ('id_estado', models.ForeignKey(to='Pedidos.Estado_Pedido')),
                ('id_socio', models.ForeignKey(to='Distribudoras.Kiosko_Distribudora')),
            ],
        ),
        migrations.AddField(
            model_name='detalle_pedido',
            name='id_pedido',
            field=models.ForeignKey(to='Pedidos.Pedido'),
        ),
        migrations.AddField(
            model_name='detalle_pedido',
            name='id_producto',
            field=models.ForeignKey(to='Productos.Producto'),
        ),
    ]
