from django.db import models


class SliderPrincipal(models.Model):
    nombre = models.CharField(max_length=30)
    imagenes = models.ImageField(upload_to='imagenes_slider/')

    def __unicode__(self):
        return u"%s" % self.imagenes


class Colore(models.Model):
    color = models.CharField(max_length=15)

    def __unicode__(self):
        return u"%s" % self.color


class Categoria(models.Model):
    categoria = models.CharField(max_length=20)

    def __unicode__(self):
        return u"%s" % self.categoria


class Producto(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(help_text='Descripcion del producto', default='')
    categoria = models.ForeignKey(Categoria)
    colores = models.ManyToManyField(Colore)
    imagen_principal = models.ImageField(upload_to='imagenes_productos/', null=True)
    imagen_dos = models.ImageField(upload_to='imagenes_productos/', null=True)
    imagen_tres = models.ImageField(upload_to='imagenes_productos/', null=True)
    imagen_cuatro = models.ImageField(upload_to='imagenes_productos/', null=True)
    es_promocion = models.BooleanField(default=False)
    es_recomendado = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%s" % self.nombre
