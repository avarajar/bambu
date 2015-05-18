from django.shortcuts import render
from .serializers import ProductoSerializer
from .models import Producto
from rest_framework import viewsets


class ProductoViewSet(viewsets.ModelViewSet):
    """
    Rest Framework groups views
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    # filter_class = CardGroupFilter
    # permission_classes = (ReadOnlyPermission, )
