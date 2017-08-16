# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0002_subcategoria_tipo_presentacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategoria',
            name='tipo_presentacion',
            field=models.ForeignKey(blank=True, to='productos.Tipo_Presentacion'),
        ),
    ]
