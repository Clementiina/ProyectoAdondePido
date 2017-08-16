from django.db import models

class Categoria (models.Model):
	nombre = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return "Marca: %s" %(self.nombre)

class SubCategoria (models.Model):
	nombre = models.CharField(max_length=50)
	categoria = models.ForeignKey(Categoria)
	tipo_presentacion = models.ForeignKey("productos.Tipo_Presentacion", blank=True)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return "SubCategoria: %s" %(self.nombre)

class Marca (models.Model):
	nombre = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return "Marca: %s" %(self.nombre)


class Marca_SubCategoria (models.Model):
	subCategoria = models.ForeignKey(SubCategoria)
	marca = models.ForeignKey(Marca)
	estado = models.BooleanField(default=True)

	
	def __str__(self):

		return "SubCategoria: %s Marca: %s" %(self.subCategoria, self.marca)


