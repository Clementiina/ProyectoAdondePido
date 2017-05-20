# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0002_auto_20170520_1728'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='categoria_distribuidora',
            unique_together=set([('distribuidora', 'tipo_distribuidora')]),
        ),
    ]
