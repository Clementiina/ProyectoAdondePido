# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0002_distribuidora_cuit'),
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_pedido',
            name='producto_distribuidora',
            field=models.ForeignKey(to='distribuidoras.Producto_Distribudora', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 5, 18, 29, 18, 226224, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado_p',
            field=models.CharField(max_length=1, choices=[('n', 'No Enviado'), ('e', 'Enviado'), ('p', 'En Proseso'), ('r', 'Recivido')]),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_envio',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_recepcion',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='detalle_pedido',
            unique_together=set([('pedido', 'producto_distribuidora')]),
        ),
        migrations.RemoveField(
            model_name='detalle_pedido',
            name='producto',
        ),
    ]
