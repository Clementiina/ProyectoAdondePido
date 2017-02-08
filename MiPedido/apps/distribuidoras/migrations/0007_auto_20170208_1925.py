# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0006_auto_20170208_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='estado',
            field=models.CharField(choices=[('l', 'Listo'), ('v', 'vigente'), ('f', 'finalizado')], max_length=1),
        ),
    ]
