# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negocios', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usuario_negocio',
            unique_together=set([('negocio', 'usuario', 'permiso')]),
        ),
    ]
