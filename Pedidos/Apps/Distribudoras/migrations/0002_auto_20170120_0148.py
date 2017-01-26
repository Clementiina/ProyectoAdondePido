# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Distribudoras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribudora',
            name='numero_contacto',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='producto_distribudora',
            name='stock',
            field=models.PositiveIntegerField(),
        ),
    ]
