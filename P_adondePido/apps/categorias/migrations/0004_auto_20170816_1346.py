# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0003_auto_20170816_1335'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='marca_subcategoria',
            unique_together=set([]),
        ),
    ]
