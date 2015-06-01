import django_filters
from .models import *


class ProductoFilter(django_filters.FilterSet):
    categoria = django_filters.CharFilter(name='categoria__slug')
    recomendado = django_filters.CharFilter(name='es_recomendado')
    promocion = django_filters.CharFilter(name='es_promocion')

    class Meta:
        model = Producto
        fields = ('categoria', 'recomendado', 'promocion')
