# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='marcaxsubcategoria_distribuidora',
            unique_together=set([('distribuidora', 'marcaSubCategoria')]),
        ),
        migrations.AlterUniqueTogether(
            name='usuario_distribuidora',
            unique_together=set([('distribuidora', 'usuario', 'permiso')]),
        ),
    ]
