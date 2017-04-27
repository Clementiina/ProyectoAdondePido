from django.db import models
from django.contrib.auth.models import User
from apps.localidades.models import Localidad
from apps.distribuidoras.models import Distribuidora

class Solicitud (models.Model):
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	usuario = models.CharField(max_length=20)
	user = models.ForeignKey(User)
	email = models.EmailField(max_length=70)
	code = models.CharField(max_length=8)
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	dni = models.BigIntegerField()
	telefono = models.BigIntegerField(blank=True)
	celular = models.BigIntegerField(blank=True)
	localidad = models.ForeignKey(Localidad, default =3935) #Salta   
	n_nombre = models.CharField(max_length=50)
	descripcion = models.TextField()
	numero_contacto = models.BigIntegerField()
	direccion = models.CharField(max_length=50)

class Distribuidora_Solicitud (models.Model):
	solicitud = models.ForeignKey(Solicitud)
	distribuidora = models.ForeignKey(Distribuidora)