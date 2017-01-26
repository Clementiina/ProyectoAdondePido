from django.db import models

class Categoria (models.Model):
    nombre = models.CharField(max_length=50)

class SubCategoria (models.Model):
    nombre = models.CharField(max_length=50)
    id_categoria = models.ForeignKey(Categoria)

class Marca (models.Model):
    nombre = models.CharField(max_length=50)

class Marca_SubCategoria (models.Model):
    id_subCategoria = models.ForeignKey(SubCategoria)
    id_marca = models.ForeignKey(Marca)

