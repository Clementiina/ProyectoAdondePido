# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Localidades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='localidad',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='provincia',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
