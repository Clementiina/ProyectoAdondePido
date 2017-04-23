# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('distribuidoras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_Distribuidora',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('estado', models.BooleanField(default=True)),
                ('distribuidora', models.ForeignKey(to='distribuidoras.Distribuidora')),
            ],
        ),
        migrations.CreateModel(
            name='MarcaXSubcategoria_Distribuidora',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('estado', models.BooleanField(default=True)),
                ('distribuidora', models.ForeignKey(to='distribuidoras.Distribuidora')),
                ('marcaSubCategoria', models.ForeignKey(to='categorias.Marca_SubCategoria')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Distribuidora',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tipoproducto_distribuidora',
            name='distribuidora',
        ),
        migrations.RemoveField(
            model_name='tipoproducto_distribuidora',
            name='tipoProducto',
        ),
        migrations.DeleteModel(
            name='TipoProducto_Distribuidora',
        ),
        migrations.AddField(
            model_name='categoria_distribuidora',
            name='tipo_distribuidora',
            field=models.ForeignKey(to='distribuidoras.Tipo_Distribuidora'),
        ),
        migrations.AddField(
            model_name='producto_distribudora',
            name='marcaXSubcategoriaDistribuidora',
            field=models.ForeignKey(default=1, to='distribuidoras.MarcaXSubcategoria_Distribuidora'),
            preserve_default=False,
        ),
    ]
