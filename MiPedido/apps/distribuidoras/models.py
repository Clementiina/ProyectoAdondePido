# -*- conding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from apps.localidades.models import Localidad
from apps.productos.models import Producto
from apps.productos.models import Tipo_Producto
from apps.negocios.models import Negocio
from apps.personas.models import Persona

DiasType = (
    ("lu","Lunes" ),
    ("ma","Martes"),
    ("mi","Miercoles"),
    ("ju","Jueves" ),
    ("vi","Viernes"),
    ("sa","Sabado"),
    ("do","Domingo")
)

EstadoType = (
    ("l","Listo" ),
    ("v","vigente"),
    ("f","finalizado")
)

class Distribuidora (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(verbose_name=u"Descripcion")
    numero_contacto = models.PositiveIntegerField(verbose_name=u"Numero de contacto")
    localidad = models.ForeignKey(Localidad, verbose_name=u"Localidad")
    direccion = models.CharField(max_length=50, verbose_name=u"Direccion")
    persona_cargo = models.ForeignKey(Persona, verbose_name=u"Persona a cargo")
    estado = models.BooleanField(default=True)


class Permiso_Distribuidora (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)


class Usuario_Distribuidora (models.Model):
    distribuidora = models.ForeignKey(Distribuidora, verbose_name=u"Distribuidora")
    usuario = models.ForeignKey(User, verbose_name=u"Usuario")
    permiso = models.ForeignKey(Permiso_Distribuidora, verbose_name=u"Permiso", blank=True) #por ahora no se manejan permisos
    estado = models.BooleanField(default=True)


class TipoProducto_Distribuidora (models.Model):
    distribuidora = models.ForeignKey(Distribuidora)
    tipoProducto = models.ForeignKey(Tipo_Producto)
    estado = models.BooleanField(default=True)


class Producto_Distribudora (models.Model):
    distribudora = models.ForeignKey(Distribuidora)
    producto = models.ForeignKey(Producto)
    stock = models.PositiveIntegerField()
    estado = models.BooleanField(default=True)

    
class Ruta (models.Model):
    distribuidora = models.ForeignKey(Distribuidora)
    nombre = models.CharField(max_length=50)
    recorrido = models.TextField()
    dia = models.CharField(max_length=2, choices=(DiasType))
    estado = models.BooleanField(default=True)

    
class Negocio_Distribuidora (models.Model):  # Socio    
    negocio = models.ForeignKey(Negocio)
    distribuidora = models.ForeignKey(Distribuidora)
    ruta = models.ForeignKey(Ruta, null=True, blank=True)
    alias_distribuidora = models.CharField(max_length=50, blank=True)
    alias_negocio = models.CharField(max_length=50, blank=True)
    estado = models.BooleanField(default=True)
    class Meta:
        unique_together = ("negocio", "distribuidora")


class Anuncio (models.Model):
    distribuidora = models.ForeignKey(Distribuidora)
    imagen = models.ImageField()
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=1, choices=(EstadoType))
    
    def __str__(self):
        return self.titulo
    
