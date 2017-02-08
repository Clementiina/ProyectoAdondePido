# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='fecha_ini',
            new_name='fecha_inicio',
        ),
        migrations.AddField(
            model_name='anuncio',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 1, 31, 21, 41, 40, 52395, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
