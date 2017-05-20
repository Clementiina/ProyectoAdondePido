from django.db import models


class Provincia (models.Model):
	nombre = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre


class Departamento (models.Model):
	nombre = models.CharField(max_length=50)
	provincia = models.ForeignKey(Provincia, verbose_name="Provincia")
	estado = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre


class Localidad (models.Model):
	nombre = models.CharField(max_length=50)
	codigo_postal = models.CharField(max_length=10, verbose_name="Codigo postal")
	departamento = models.ForeignKey(Departamento, verbose_name="Departamento")
	estado = models.BooleanField(default=True)

	def __str__(self):
		return "%s codigo postal N° %s" %(self.nombre, self.codigo_postal)