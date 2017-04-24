# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0003_solicitud_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='n_nombre',
            field=models.CharField(default='negocio', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]
