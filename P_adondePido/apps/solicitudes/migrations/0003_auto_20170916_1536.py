# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_auto_20170916_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='code',
            field=models.CharField(null=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='cuit',
            field=models.BigIntegerField(null=True),
        ),
    ]
