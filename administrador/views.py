from django.shortcuts import render
from .serializers import ProductoSerializer
from .models import Producto
from .filters import ProductoFilter
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
