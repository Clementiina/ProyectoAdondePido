from django.db import models
from Apps.Categorias.models import Marca_SubCategoria

class Tipo_Producto (models.Model):
    nombre = models.CharField(max_length=50)

class Presentacion (models.Model):
    capacidad = models.CharField(max_length=50)

class Producto (models.Model):
    id_marcaSubCategoria = models.ForeignKey(Marca_SubCategoria)
    id_tipo = models.ForeignKey(Tipo_Producto)
    nombre = models.CharField(max_length=50)
    descripsiom = models.TextField()
    id_presentacion = models.ForeignKey(Presentacion)
    precio_unitario = models.FloatField()

