from django.db import models
from django.contrib.auth.models import User
from apps.localidades.models import Localidad
from apps.productos.models import Producto
from apps.productos.models import Tipo_Producto
from apps.kioskos.models import Kiosko

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
    descripcion = models.TextField()
    numero_contacto = models.PositiveIntegerField()
    id_localidad = models.ForeignKey(Localidad)
    direccion = models.CharField(max_length=50)
    persona_cargo = models.ForeignKey(User)
    estado = models.BooleanField(default=True)


class Permiso_Distribuidora (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)


class Usuario_Distribuidora (models.Model):
    id_distribuidora = models.ForeignKey(Distribuidora)
    id_usuario = models.ForeignKey(User)
    id_permiso = models.ForeignKey(Permiso_Distribuidora)
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
	dia = models.CharField(max_length=2, choices=(DiasType))
	estado = models.BooleanField(default=True)

	
class Kiosko_Distribuidora (models.Model):  # Socio
    id_ruta = models.ForeignKey(Ruta)
    id_kiosko = models.ForeignKey(Kiosko)
    alias_distribuidora = models.CharField(max_length=50)
    alias_kiosko = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)


class Anuncio (models.Model):

    def url(self, filename):
        ruta = "ImagenesAnuncios/%s" % (str(filename))
        return ruta

    id_distribuidora = models.ForeignKey(Distribuidora)
    imagen = models.ImageField(blank=True, null=True, upload_to=url)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=1, choices=(EstadoType))