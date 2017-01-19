from django.db import models

class Provincia (models.Model):
    nombre = models.CharField(max_length=50)

class Departamento (models.Model):
    nombre = models.CharField(max_length=50)
    id_provincia = models.ForeignKey(Provincia)

class Localidad (models.Model):
    nombre = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)
    id_departamento = models.ForeignKey(Departamento)
