# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0002_auto_20170131_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='fecha_fin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='fecha_inicio',
            field=models.DateField(),
        ),
    ]
