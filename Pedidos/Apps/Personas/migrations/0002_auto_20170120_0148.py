# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='celular',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.PositiveIntegerField(),
        ),
    ]
