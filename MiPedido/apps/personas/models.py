from django.db import models
from django.contrib.auth.models import User
from apps.localidades.models import Localidad


class Persona (models.Model):
	usuario = models.OneToOneField(User)
	dni = models.BigIntegerField()
	telefono = models.BigIntegerField()
	celular = models.BigIntegerField()
	localidad = models.ForeignKey(Localidad)
	direccion = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)