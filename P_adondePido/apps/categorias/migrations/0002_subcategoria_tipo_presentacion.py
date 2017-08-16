# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategoria',
            name='tipo_presentacion',
            field=models.ForeignKey(default=1, to='productos.Tipo_Presentacion'),
            preserve_default=False,
        ),
    ]
