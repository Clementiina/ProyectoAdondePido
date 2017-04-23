from django.db import models
from apps.distribuidoras.models import Negocio_Distribuidora  # socio
from apps.productos.models import Producto

EstadoType = (
	("e","Enviado"),
	("p","En Proseso"),
	("r","Recivido"),
)

class Pedido (models.Model):
	socio = models.ForeignKey(Negocio_Distribuidora)
	fecha_envio = models.DateTimeField()
	fecha_recepcion = models.DateTimeField()
	estado_p = models.CharField(max_length=1, choices=(EstadoType))
	estado = models.BooleanField(default=True)

class Detalle_Pedido (models.Model):
	pedido = models.ForeignKey(Pedido)
	producto = models.ForeignKey(Producto)
	precio_unitario = models.FloatField()
	cantidad = models.PositiveIntegerField()
	estado = models.BooleanField(default=True)