from django.db import models


class Colore(models.Model):
    color = models.CharField(max_length=15)

    def __unicode__(self):
        return u"%s" % self.color


class Categoria(models.Model):
    categoria = models.CharField(max_length=20)

    def __unicode__(self):
        return u"%s" % self.categoria


class Producto(models.Model):
    nombre = models.CharField(max_length=20)

    def __unicode__(self):
        return u"%s" % self.nombre
