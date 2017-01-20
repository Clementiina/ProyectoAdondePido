# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kioskos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kiosko',
            name='numero_contacto',
            field=models.PositiveIntegerField(),
        ),
    ]
