from django.db import models
from django.contrib.auth.models import User
from apps.localidades.models import Localidad
from apps.distribuidoras.models import Distribuidora
from django.core.validators import RegexValidator

EstadoType = (
	("p","Pendiente" ),
	("a","Activo")
)

class Solicitud (models.Model):
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	usuario = models.ForeignKey(User)
	code = models.CharField(max_length=50)
	dni = models.BigIntegerField()
	telefono = models.BigIntegerField(blank=True)
	celular = models.BigIntegerField(blank=True)
	localidad = models.ForeignKey(Localidad, default =3935) #Salta   
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()
	numero_contacto = models.BigIntegerField()
	direccion = models.CharField(max_length=50)
	estado = models.CharField(max_length=1, choices=(EstadoType))

class Distribuidora_Solicitud (models.Model):
	solicitud = models.ForeignKey(Solicitud)
	distribuidora = models.ForeignKey(Distribuidora)