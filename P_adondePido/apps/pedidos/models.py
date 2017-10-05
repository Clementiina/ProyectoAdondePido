from django.db import models
from apps.distribuidoras.models import Negocio_Distribuidora#, Producto_Distribudora # socio
from apps.productos.models import Producto

EstadoType = (
	("n","No Enviado"),
	("e","Enviado"),
	("p","En Proseso"),
	("r","Recivido"),
)

class Pedido (models.Model):
	socio = models.ForeignKey(Negocio_Distribuidora)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_envio = models.DateTimeField(blank=True, null=True)
	fecha_recepcion = models.DateTimeField(blank=True, null=True)
	estado_p = models.CharField(max_length=1, choices=(EstadoType))
	estado = models.BooleanField(default=True)
	

	def __str__(self):
		return "pedido Nro: %s" %(self.id)

class Detalle_Pedido (models.Model):
	pedido = models.ForeignKey(Pedido)
	producto_distribuidora = models.ForeignKey("distribuidoras.Producto_Distribudora")
	precio_unitario = models.FloatField()
	cantidad = models.PositiveIntegerField()
	estado = models.BooleanField(default=True)

	class Meta:

		unique_together = ("pedido", "producto_distribuidora")

	def __str__(self):

		return "Pedido %s - Producto %s" %(self.pedido, self.producto_distribuidora)