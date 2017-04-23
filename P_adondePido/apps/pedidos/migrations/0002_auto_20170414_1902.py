# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Estado_Pedido',
        ),
        migrations.AddField(
            model_name='pedido',
            name='estado_p',
            field=models.CharField(max_length=1, default='e', choices=[('e', 'Enviado'), ('p', 'En Proseso'), ('r', 'Recivido')]),
            preserve_default=False,
        ),
    ]
