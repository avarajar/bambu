# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0009_auto_20150531_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenesMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('icono', models.ImageField(null=True, upload_to=b'imagenes_menu/')),
                ('imagen_principal', models.ImageField(null=True, upload_to=b'imagenes_menu/')),
            ],
        ),
    ]
