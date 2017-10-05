# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0004_distribuidora_cuit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribuidora',
            name='cuit',
            field=models.PositiveIntegerField(),
        ),
    ]
