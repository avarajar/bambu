# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0012_auto_20150531_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colore',
            name='color',
        ),
    ]
