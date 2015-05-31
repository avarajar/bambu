# -*- coding:utf-8 -*-

from rest_framework import serializers


from .models import Categoria, Colore, Producto
# from .utils import extract_url_sources


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'colores', 'imagen_principal',
                  'imagen_dos', 'imagen_tres', 'imagen_cuatro', 'categoria')
        depth = 1
