from django.db import models
from apps.categorias.models import Marca_SubCategoria

class Presentacion (models.Model):
	capacidad = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)


class Producto (models.Model):
	marcaSubCategoria = models.ForeignKey(Marca_SubCategoria)
	nombre = models.CharField(max_length=50)
	descripsiom = models.TextField()
	presentacion = models.ForeignKey(Presentacion)
	precio_unitario = models.FloatField()
	estado = models.BooleanField(default=True)

