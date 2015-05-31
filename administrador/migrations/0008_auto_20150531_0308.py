# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0007_categoria_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='colore',
            name='nombre',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='colore',
            name='color',
            field=colorfield.fields.ColorField(default=b'ffffff', max_length=10),
        ),
        migrations.AlterField(
            model_name='sliderprincipal',
            name='nombre',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
