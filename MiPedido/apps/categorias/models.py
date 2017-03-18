from django.db import models

class Categoria (models.Model):
	nombre = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)

class SubCategoria (models.Model):
	nombre = models.CharField(max_length=50)
	categoria = models.ForeignKey(Categoria)
	estado = models.BooleanField(default=True)


class Marca (models.Model):
	nombre = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)


class Marca_SubCategoria (models.Model):
	subCategoria = models.ForeignKey(SubCategoria)
	marca = models.ForeignKey(Marca)
	estado = models.BooleanField(default=True)
