from django.db import models
from apps.categorias.models import Marca_SubCategoria

class Presentacion (models.Model):
	capacidad = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return self.capacidad


class Producto (models.Model):
	marcaSubCategoria = models.ForeignKey(Marca_SubCategoria)
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()
	estado = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre

class Producto_Presentacion(models.Model):
	producto = models.ForeignKey(Producto)
	presentacion = models.ForeignKey(Presentacion)
	precio_unitario = models.FloatField()
	estado = models.BooleanField(default=True)

	class Meta:
		unique_together = ('producto', 'presentacion')

	def __str__(self):
		return '%s en una presentacion de: %s ' % (self.producto, self.presentacion)

