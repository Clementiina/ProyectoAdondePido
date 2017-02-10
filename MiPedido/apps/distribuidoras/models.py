# -*- conding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from apps.localidades.models import Localidad
from apps.productos.models import Producto
from apps.productos.models import Tipo_Producto
from apps.kioskos.models import Kiosko


class Distribuidora (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(verbose_name=u"Descripcion")
    numero_contacto = models.PositiveIntegerField(verbose_name=u"Numero de contacto")
    id_localidad = models.ForeignKey(Localidad, verbose_name=u"Localidad")
    direccion = models.CharField(max_length=50, verbose_name=u"Direccion")
    persona_cargo = models.ForeignKey(User, verbose_name=u"Persona a cargo")
    estado = models.BooleanField(default=True)


class Permiso_Distribuidora (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)


class Usuario_Distribuidora (models.Model):
    id_distribuidora = models.ForeignKey(Distribuidora, verbose_name=u"Distribuidora")
    id_usuario = models.ForeignKey(User, verbose_name=u"Usuario")
    id_permiso = models.ForeignKey(Permiso_Distribuidora, verbose_name=u"Permiso")
    estado = models.BooleanField(default=True)


class TipoProducto_Distribuidora (models.Model):
    id_distribuidora = models.ForeignKey(Distribuidora)
    id_tipoProducto = models.ForeignKey(Tipo_Producto)
    estado = models.BooleanField(default=True)


class Producto_Distribudora (models.Model):
    id_distribudora = models.ForeignKey(Distribuidora)
    id_producto = models.ForeignKey(Producto)
    stock = models.PositiveIntegerField()
    estado = models.BooleanField(default=True)


class Ruta (models.Model):
    id_distribuidora = models.ForeignKey(Distribuidora)
    nombre = models.CharField(max_length=50)
    recorrido = models.TextField()
    dia = models.CharField(max_length=1)
    estado = models.BooleanField(default=True)


class Kiosko_Distribuidora (models.Model):  # Socio
    id_ruta = models.ForeignKey(Ruta)
    id_kiosko = models.ForeignKey(Kiosko)
    alias_distribuidora = models.CharField(max_length=50)
    alias_kiosko = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)


class Anuncio (models.Model):
    id_distribuidora = models.ForeignKey(Distribuidora)
    imagen = models.ImageField()
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=1, choices=(
                            ("l", "Listo"),
                            ("v", "vigente"),
                            ("f", "finalizado")))

    def __str__(self):
        return self.titulo