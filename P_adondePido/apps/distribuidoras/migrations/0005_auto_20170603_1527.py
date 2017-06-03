# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('distribuidoras', '0004_auto_20170520_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruta',
            name='dia',
            field=multiselectfield.db.fields.MultiSelectField(max_length=20, choices=[('lu', 'Lunes'), ('ma', 'Martes'), ('mi', 'Miercoles'), ('ju', 'Jueves'), ('vi', 'Viernes'), ('sa', 'Sabado'), ('do', 'Domingo')]),
        ),
    ]
