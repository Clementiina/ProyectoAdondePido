# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.distribuidoras.models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='imagen',
            field=models.ImageField(upload_to=apps.distribuidoras.models.Anuncio.url, null=True, blank=True),
        ),
    ]
