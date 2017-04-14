# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0002_auto_20170414_1902'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='tipo_producto',
        ),
        migrations.DeleteModel(
            name='Tipo_Producto',
        ),
    ]
