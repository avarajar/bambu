# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0011_auto_20150531_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='colore',
            name='color',
            field=colorfield.fields.ColorField(default=b'ffffff', max_length=10),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen_cuatro',
            field=models.ImageField(null=True, upload_to=b'imagenes_productos/', blank=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen_dos',
            field=models.ImageField(null=True, upload_to=b'imagenes_productos/', blank=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen_principal',
            field=models.ImageField(null=True, upload_to=b'imagenes_productos/', blank=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen_tres',
            field=models.ImageField(null=True, upload_to=b'imagenes_productos/', blank=True),
        ),
    ]
