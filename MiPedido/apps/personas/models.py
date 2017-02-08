from django.db import models
from django.contrib.auth.models import User
from apps.localidades.models import Localidad


class Persona (models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    usuario = models.OneToOneField(User)
    dni = models.PositiveIntegerField()
    telefono = models.PositiveIntegerField()
    celular = models.PositiveIntegerField()
    id_localidad = models.ForeignKey(Localidad)
    direccion = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
