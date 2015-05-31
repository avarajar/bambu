from django.contrib import admin
from .models import *


class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    list_filter = ('nombre',)
    #list_editable = ('color',)
    search_fields = ('nombre', )

admin.site.register(Colore, ColorAdmin)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(SliderPrincipal)
admin.site.register(ImagenesMenu)
