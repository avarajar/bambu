from django.shortcuts import render
from .serializers import ProductoSerializer, CategoriaSerializer, ImagenesMenuSerializer
from .models import Producto, Categoria, ImagenesMenu
from .filters import ProductoFilter, CategoriaFilter, MenuFilter
from rest_framework import viewsets, filters


class ProductoViewSet(viewsets.ModelViewSet):
    """
    Rest Framework groups views
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductoFilter
    # permission_classes = (ReadOnlyPermission, )


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    Rest Framework groups views
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = CategoriaFilter


class ImagenesMenuViewSet(viewsets.ModelViewSet):
    """
    Rest Framework groups views
    """
    queryset = ImagenesMenu.objects.all()
    serializer_class = ImagenesMenuSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = MenuFilter
