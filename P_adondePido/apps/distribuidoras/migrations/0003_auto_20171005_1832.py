# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.distribuidoras.models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0002_distribuidora_cuit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distribuidora',
            name='cuit',
        ),
        migrations.AddField(
            model_name='distribuidora',
            name='imagen',
            field=models.ImageField(null=True, upload_to=apps.distribuidoras.models.Distribuidora.url, blank=True),
        ),
    ]
