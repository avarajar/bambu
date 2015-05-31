from django.db import models
from django.template.defaultfilters import slugify
# from colorfield.fields import ColorField


class SliderPrincipal(models.Model):
    nombre = models.CharField(max_length=30, blank=True)
    imagenes = models.ImageField(upload_to='imagenes_slider/')

    def __unicode__(self):
        return u"%s" % self.imagenes


class Colore(models.Model):
    nombre = models.CharField(max_length=15)
    # color = ColorField(default='ffffff')

    def __unicode__(self):
        return u"%s" % self.nombre


class Categoria(models.Model):
    categoria = models.CharField(max_length=20)
    imagen_icono = models.ImageField(upload_to='imagenes_categorias/', null=True)
    imagen_principal = models.ImageField(upload_to='imagenes_categorias/', null=True)
    slug = models.SlugField(max_length=250, blank=True, default='')

    def __unicode__(self):
        return u"%s" % self.categoria

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.categoria)
        super(Categoria, self).save(*args, **kwargs)


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
    slug = models.SlugField(max_length=250, blank=True, default='')

    def __unicode__(self):
        return u"%s" % self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super(Producto, self).save(*args, **kwargs)


class ImagenesMenu(models.Model):
    """docstring for ImagenesMenu"""
    nombre = models.CharField(max_length=50, blank=True)
    icono = models.ImageField(upload_to='imagenes_menu/', null=True, blank=True)
    imagen_principal = models.ImageField(upload_to='imagenes_menu/', null=True, blank=True)
    slug = models.SlugField(max_length=250, blank=True, default='')

    def __unicode__(self):
        return u"%s" % self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super(ImagenesMenu, self).save(*args, **kwargs)
