# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='cuit',
            field=models.BigIntegerField(default=0, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='es_distribuidora',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='code',
            field=models.CharField(max_length=8, blank=True),
        ),
    ]
