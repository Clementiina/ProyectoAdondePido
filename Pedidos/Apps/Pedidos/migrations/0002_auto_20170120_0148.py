# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_pedido',
            name='cantidad',
            field=models.PositiveIntegerField(),
        ),
    ]
