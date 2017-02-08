# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.distribuidoras.models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0005_auto_20170208_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='imagen',
            field=models.ImageField(null=True, upload_to=apps.distribuidoras.models.Anuncio.url, blank=True),
        ),
    ]
