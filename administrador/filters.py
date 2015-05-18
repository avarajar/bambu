import django_filters
from .models import *


class ProductoFilter(django_filters.FilterSet):
    categoria = django_filters.CharFilter(name='categoria__slug')

    class Meta:
        model = Producto
        fields = ('categoria', )
