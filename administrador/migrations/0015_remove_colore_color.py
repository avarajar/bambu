# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0014_colore_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colore',
            name='color',
        ),
    ]
