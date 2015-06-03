# -*- coding:utf-8 -*-

from rest_framework import serializers


from .models import Categoria, Producto, ImagenesMenu
# from .utils import extract_url_sources


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'descripcion', 'colores', 'imagen_principal',
                  'imagen_dos', 'imagen_tres', 'imagen_cuatro', 'categoria',)
        depth = 1


class ProductoRSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'descripcion', 'colores', 'imagen_principal',
                  'imagen_dos', 'imagen_tres', 'imagen_cuatro', 'categoria',)
        depth = 1


class ProductoPSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ('id', 'nombre', 'descripcion', 'colores', 'imagen_principal',
                  'imagen_dos', 'imagen_tres', 'imagen_cuatro', 'categoria',)
        depth = 1


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('categoria', 'imagen_icono', 'imagen_principal')
        depth = 1


class ImagenesMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImagenesMenu
        fields = ('nombre', 'icono', 'imagen_principal', 'slug')
        depth = 1
