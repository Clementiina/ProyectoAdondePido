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
            name='apellido',
            field=models.CharField(max_length=30, default='apellido'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='code',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='usuario',
            field=models.CharField(max_length=20),
        ),
    ]
