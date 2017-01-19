from django.db import models
from Apps.Distribudoras.models import Kiosko_Distribudora #socio
from Apps.Productos.models import Producto

class Estado_Pedido (models.Model):
    nombre = models.CharField(max_length=10)

class Pedido (models.Model):
    id_socio = models.ForeignKey(Kiosko_Distribudora)
    fecha_envio = models.DateTimeField()
    fecha_recepcion = models.DateTimeField()
    id_estado = models.ForeignKey(Estado_Pedido)

class Detalle_Pedido (models.Model):
    id_pedido = models.ForeignKey(Pedido)
    id_producto = models.ForeignKey(Producto)
    precio_unitario = models.FloatField()
    cantidad =  models.PositiveIntegerField()
