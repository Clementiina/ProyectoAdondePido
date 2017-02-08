from django.db import models
from apps.distribuidoras.models import Kiosko_Distribuidora  # socio
from apps.productos.models import Producto


class Estado_Pedido(models.Model):
    nombre = models.CharField(max_length=10)
    estado = models.BooleanField(default=True)


class Pedido (models.Model):
    id_socio = models.ForeignKey(Kiosko_Distribuidora)
    fecha_envio = models.DateTimeField()
    fecha_recepcion = models.DateTimeField()
    id_estado = models.ForeignKey(Estado_Pedido)
    estado = models.BooleanField(default=True)


class Detalle_Pedido (models.Model):
    id_pedido = models.ForeignKey(Pedido)
    id_producto = models.ForeignKey(Producto)
    precio_unitario = models.FloatField()
    cantidad = models.PositiveIntegerField()
    estado = models.BooleanField(default=True)