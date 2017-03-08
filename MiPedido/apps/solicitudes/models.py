from django.db import models
from django.contrib.auth.models import User
from apps.localidades.models import Localidad
from apps.distribuidoras.models import Distribuidora
from django.core.validators import RegexValidator

EstadoType = (
    ("p","Pendiente" ),
    ("a","Activo")
)

check = [RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Ingrese numero en el siguiente formato: '+999999999'. Hasta 15 digitos.")]

class Solicitud (models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=8)
    contraseña = models.CharField(max_length=20)
    email = models.EmailField(help_text='Ingrese un email valido, por favor.', default='sin@mail.com')
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    dni = models.PositiveIntegerField()
    telefono = models.CharField(max_length=16,validators=check, blank=True)
    celular = models.CharField(max_length=16,validators=check, blank=True)
    id_localidad = models.ForeignKey(Localidad, default =20254)
    direccion = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, choices=(EstadoType))

class Distribuidora_Solicitud (models.Model):
    id_usuario = models.ForeignKey(User)
    id_distribuidora = models.ForeignKey(Distribuidora)