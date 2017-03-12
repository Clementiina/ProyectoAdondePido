from django.db import models
from django.contrib.auth.models import User
from apps.localidades.models import Localidad
from apps.personas.models import Persona


class Permiso_Negocio (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)


class Negocio (models.Model):
    nombre = models.CharField(max_length=50,blank=True)
    descripcion = models.TextField(blank=True)
    numero_contacto = models.PositiveIntegerField(blank=True)
    localidad = models.ForeignKey(Localidad)
    direccion = models.CharField(max_length=50)
    persona_cargo = models.ForeignKey(Persona)
    estado = models.BooleanField(default=True)


class Usuario_Negocio (models.Model):
    negocio = models.ForeignKey(Negocio)
    usuario = models.ForeignKey(User)
    permiso = models.ForeignKey(Permiso_Negocio, blank=True) #por ahora no se manejan permisos
    estado = models.BooleanField(default=True)

