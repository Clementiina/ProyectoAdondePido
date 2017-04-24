# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_auto_20170414_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='email',
            field=models.EmailField(default='sin@email.com', max_length=70),
            preserve_default=False,
        ),
    ]
