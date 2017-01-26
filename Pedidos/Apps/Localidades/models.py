from django.db import models

class Provincia (models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def __str__(self):
    	return self.nombre

class Departamento (models.Model):
    nombre = models.CharField(max_length=50)
    id_provincia = models.ForeignKey(Provincia)
    estado = models.BooleanField(default=True)

    def __str__(self):
    	return self.nombre

class Localidad (models.Model):
    nombre = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)
    id_departamento = models.ForeignKey(Departamento)
    estado = models.BooleanField(default=True)

    def __str__(self):
    	return self.nombre