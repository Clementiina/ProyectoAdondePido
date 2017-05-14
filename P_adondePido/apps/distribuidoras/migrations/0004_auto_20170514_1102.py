# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20170514_1102'),
        ('distribuidoras', '0003_auto_20170424_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto_distribudora',
            name='precio_unitario',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto_distribudora',
            name='presentacion',
            field=models.ForeignKey(default=0, to='productos.Presentacion'),
            preserve_default=False,
        ),
    ]
