from django.db import models

class Categoria (models.Model):
	nombre = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return "Marca: %s" %(self.marca)

class SubCategoria (models.Model):
	nombre = models.CharField(max_length=50)
	categoria = models.ForeignKey(Categoria)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return "SubCategoria: %s" %(self.subCategoria)

class Marca (models.Model):
	nombre = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return "Marca: %s" %(self.marca)


class Marca_SubCategoria (models.Model):
	subCategoria = models.ForeignKey(SubCategoria)
	marca = models.ForeignKey(Marca)
	estado = models.BooleanField(default=True)

	class Meta:

		unique_together = ('subCategoria', 'marca')

	def __str__(self):

		return "SubCategoria: %s Marca: %s" %(self.subCategoria, self.marca)


