# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('solicitudes', '0004_auto_20170423_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='estado',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
