# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0004_producto_es_recomendado'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(default=b'', help_text=b'Descripcion del producto'),
        ),
    ]
