# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0010_imagenesmenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagenesmenu',
            name='slug',
            field=models.SlugField(default=b'', max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='imagenesmenu',
            name='icono',
            field=models.ImageField(null=True, upload_to=b'imagenes_menu/', blank=True),
        ),
        migrations.AlterField(
            model_name='imagenesmenu',
            name='imagen_principal',
            field=models.ImageField(null=True, upload_to=b'imagenes_menu/', blank=True),
        ),
    ]
