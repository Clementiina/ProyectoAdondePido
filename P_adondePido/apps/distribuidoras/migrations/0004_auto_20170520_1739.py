# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0003_auto_20170520_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto_distribudora',
            old_name='distribudora',
            new_name='distribuidora',
        ),
        migrations.AlterUniqueTogether(
            name='producto_distribudora',
            unique_together=set([('distribuidora', 'marcaXSubcategoriaDistribuidora', 'producto', 'presentacion')]),
        ),
    ]
