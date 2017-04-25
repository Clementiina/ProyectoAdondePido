# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0002_auto_20170414_1902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='id_distribuidora',
            new_name='distribuidora',
        ),
    ]
