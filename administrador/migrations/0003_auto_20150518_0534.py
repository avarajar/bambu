# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_sliderprincipal'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=0, to='administrador.Categoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='colores',
            field=models.ManyToManyField(to='administrador.Colore'),
        ),
        migrations.AddField(
            model_name='producto',
            name='es_promocion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='producto',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 5, 34, 0, 159036, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen_cuatro',
            field=models.ImageField(null=True, upload_to=b'imagenes_productos/'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen_dos',
            field=models.ImageField(null=True, upload_to=b'imagenes_productos/'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen_principal',
            field=models.ImageField(null=True, upload_to=b'imagenes_productos/'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen_tres',
            field=models.ImageField(null=True, upload_to=b'imagenes_productos/'),
        ),
    ]
