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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('precio_unitario', models.FloatField()),
                ('cantidad', models.PositiveIntegerField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=10)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('fecha_envio', models.DateTimeField()),
                ('fecha_recepcion', models.DateTimeField()),
                ('estado', models.BooleanField(default=True)),
                ('id_estado', models.ForeignKey(to='pedidos.Estado_Pedido')),
                ('id_socio', models.ForeignKey(to='distribuidoras.Kiosko_Distribuidora')),
            ],
        ),
        migrations.AddField(
            model_name='detalle_pedido',
            name='id_pedido',
            field=models.ForeignKey(to='pedidos.Pedido'),
        ),
        migrations.AddField(
            model_name='detalle_pedido',
            name='id_producto',
            field=models.ForeignKey(to='productos.Producto'),
        ),
    ]
