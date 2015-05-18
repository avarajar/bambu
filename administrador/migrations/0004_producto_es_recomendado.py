# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_auto_20150518_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='es_recomendado',
            field=models.BooleanField(default=False),
        ),
    ]
