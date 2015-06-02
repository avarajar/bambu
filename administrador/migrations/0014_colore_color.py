# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0013_remove_colore_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='colore',
            name='color',
            field=colorfield.fields.ColorField(default=b'ffffff', max_length=10),
        ),
    ]
