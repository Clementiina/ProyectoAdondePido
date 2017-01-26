from django.db import models
from django.contrib.auth.models import User
from Apps.Localidades.models import Localidad
from Apps.Productos.models import Producto
from Apps.Productos.models import Tipo_Producto
from Apps.Kioskos.models import Kiosko

class Distribudora (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    numero_contacto = models.PositiveIntegerField()
    id_localidad = models.ForeignKey(Localidad)
    direccion = models.CharField(max_length=50)
    persona_cargo = models.ForeignKey(User)

class Permiso_Distribudora (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class Usuario_Distribudora (models.Model):
    id_distribudora = models.ForeignKey(Distribudora)
    id_usuario = models.ForeignKey(User)
    id_permiso = models.ForeignKey(Permiso_Distribudora)
    estado = models.BooleanField()

class TipoProducto_Distribudora (models.Model):
    id_distribudora = models.ForeignKey(Distribudora)
    id_tipoProducto= models.ForeignKey(Tipo_Producto)
    fecha_ini = models.DateTimeField()

class Producto_Distribudora (models.Model):
    id_distribudora = models.ForeignKey(Distribudora)
    id_producto = models.ForeignKey(Producto)
    stock = models.PositiveIntegerField()

class Ruta (models.Model):
    id_distribudora = models.ForeignKey(Distribudora)
    nombre = models.CharField(max_length=50)
    recorrido = models.TextField()
    dia = models.CharField(max_length=1)

class Kiosko_Distribudora (models.Model): #Socio
    id_ruta = models.ForeignKey(Ruta)
    id_kiosko = models.ForeignKey(Kiosko)
    alias_distribudora = models.CharField(max_length=50)
    alias_kiosko = models.CharField(max_length=50)

class Anuncio (models.Model):
    id_distribudora = models.ForeignKey(Distribudora)
    imagen = models.ImageField()
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_ini = models.DateTimeField()
    fecha_end = models.DateTimeField()
    estado = models.BooleanField()

