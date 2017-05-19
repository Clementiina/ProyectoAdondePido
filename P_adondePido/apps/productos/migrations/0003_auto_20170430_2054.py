# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20170414_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto_Presentacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('precio_unitario', models.FloatField()),
                ('estado', models.BooleanField(default=True)),
                ('presentacion', models.ForeignKey(to='productos.Presentacion')),
            ],
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='descripsiom',
            new_name='descripcion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio_unitario',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='presentacion',
        ),
        migrations.AddField(
            model_name='producto_presentacion',
            name='producto',
            field=models.ForeignKey(to='productos.Producto'),
        ),
        migrations.AlterUniqueTogether(
            name='producto_presentacion',
            unique_together=set([('producto', 'presentacion')]),
        ),
    ]
