# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0005_producto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(default=b'', max_length=250, blank=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='slug',
            field=models.SlugField(default=b'', max_length=250, blank=True),
        ),
    ]
