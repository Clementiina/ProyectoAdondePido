from django.db import models
from apps.categorias.models import Marca_SubCategoria

class Tipo_Presentacion(models.Model):
	nombre = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre


class Presentacion (models.Model):
	capacidad = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)
	tipo_presentacion = models.ForeignKey(Tipo_Presentacion, blank=True)

	def __str__(self):
		return self.capacidad


class Producto (models.Model):
	marcaSubCategoria = models.ForeignKey(Marca_SubCategoria)
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()
	tipo_presentacion = models.ForeignKey(Tipo_Presentacion, blank=True)
	estado = models.BooleanField(default=True)
	
	def __str__(self):
		return self.nombre

