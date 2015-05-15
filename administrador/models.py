from django.db import models

class Colore(models.Model):
	color = models.CharField(max_length=15)

class Categoria(models.Model):
	categoria = models.CharField(max_length=20)

class Producto(models.Model):
	nombre = models.CharField(max_length=20)

