from django.db import models
from apps.distribuidoras.models import Negocio_Distribuidora  # socio
from apps.productos.models import Producto


class Estado_Pedido(models.Model):
	nombre = models.CharField(max_length=10)
	estado = models.BooleanField(default=True)


class Pedido (models.Model):
	socio = models.ForeignKey(Negocio_Distribuidora)
	fecha_envio = models.DateTimeField()
	fecha_recepcion = models.DateTimeField()
	estado = models.ForeignKey(Estado_Pedido)
	estado = models.BooleanField(default=True)


class Detalle_Pedido (models.Model):
	pedido = models.ForeignKey(Pedido)
	producto = models.ForeignKey(Producto)
	precio_unitario = models.FloatField()
	cantidad = models.PositiveIntegerField()
	estado = models.BooleanField(default=True)