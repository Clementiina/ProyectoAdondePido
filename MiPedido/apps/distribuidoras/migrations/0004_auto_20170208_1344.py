# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0003_auto_20170206_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='imagen',
            field=models.ImageField(upload_to='', blank=True),
        ),
    ]
