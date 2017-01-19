from django.db import models
from django.contrib.auth.models import User
from Apps.Localidades.models import Localidad

class Permiso_Kiosko (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class Kiosko (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    numero_contacto = models.PositiveIntegerField()
    id_localidad = models.ForeignKey(Localidad)
    direccion = models.CharField(max_length=50)
    persona_cargo = models.ForeignKey(User)

class Usuario_Kiosko (models.Model):
    id_kiosko= models.ForeignKey(Kiosko)
    id_usuario = models.ForeignKey(User)
    id_permiso = models.ForeignKey(Permiso_Kiosko)
    estado = models.BooleanField()

