# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='marca_subcategoria',
            unique_together=set([('subCategoria', 'marca')]),
        ),
    ]
