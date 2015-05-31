# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0008_auto_20150531_0308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='imagen',
            new_name='imagen_icono',
        ),
        migrations.RemoveField(
            model_name='colore',
            name='color',
        ),
        migrations.AddField(
            model_name='categoria',
            name='imagen_principal',
            field=models.ImageField(null=True, upload_to=b'imagenes_categorias/'),
        ),
    ]
