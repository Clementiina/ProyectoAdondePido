# -*- conding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from apps.localidades.models import Localidad
from apps.productos.models import Producto, Presentacion
from apps.negocios.models import Negocio
from apps.personas.models import Persona
from apps.categorias.models import Marca_SubCategoria
from multiselectfield import MultiSelectField


DiasType = (
	("lu","Lunes" ),
	("ma","Martes"),
	("mi","Miercoles"),
	("ju","Jueves" ),
	("vi","Viernes"),
	("sa","Sabado"),
	("do","Domingo")
)



class Tipo_Distribuidora (models.Model):
	nombre = models.CharField(max_length=50)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre

	
class Distribuidora (models.Model):

	def url(self,nombreArchivo):
		ruta = "imagenesDistribuidoras/%s/%s" %(self.nombre,str(nombreArchivo))
		return ruta

	cuit = models.PositiveIntegerField()
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(verbose_name=u"Descripcion")
	numero_contacto = models.PositiveIntegerField(verbose_name=u"Numero de contacto")
	localidad = models.ForeignKey(Localidad, verbose_name=u"Localidad")
	direccion = models.CharField(max_length=50, verbose_name=u"Direccion")
	imagen = models.ImageField(upload_to=url, blank=True, null=True)
	persona_cargo = models.ForeignKey(Persona, verbose_name=u"Persona a cargo")
	estado = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre

	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(verbose_name=u"Descripcion")
	numero_contacto = models.PositiveIntegerField(verbose_name=u"Numero de contacto")
	localidad = models.ForeignKey(Localidad, verbose_name=u"Localidad")
	direccion = models.CharField(max_length=50, verbose_name=u"Direccion")
	persona_cargo = models.ForeignKey(Persona, verbose_name=u"Persona a cargo")
	estado = models.BooleanField(default=True)	
	def __str__(self):
		return self.nombre
	
	
class Categoria_Distribuidora (models.Model):
	distribuidora = models.ForeignKey(Distribuidora)
	tipo_distribuidora = models.ForeignKey(Tipo_Distribuidora)
	estado = models.BooleanField(default=True)

	class Meta:

		unique_together = ('distribuidora', 'tipo_distribuidora')

	def __str__(self):
		return "Distribuidora: %s Tipo %s " %(self.distribuidora, self.tipo_distribuidora)


class Permiso_Distribuidora (models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()
	estado = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre


class Usuario_Distribuidora (models.Model):
	distribuidora = models.ForeignKey(Distribuidora, verbose_name=u"Distribuidora")
	usuario = models.ForeignKey(User, verbose_name=u"Usuario")
	permiso = models.ForeignKey(Permiso_Distribuidora, verbose_name=u"Permiso", blank=True) #por ahora no se manejan permisos
	estado = models.BooleanField(default=True)

	class Meta:

		unique_together = ("distribuidora", "usuario", "permiso")
					
	def __str__(self):
		return "%s %s con permiso de %s" %(self.distribuidora, self.usuario, self.permiso)



class MarcaXSubcategoria_Distribuidora (models.Model):
	distribuidora = models.ForeignKey(Distribuidora)
	marcaSubCategoria = models.ForeignKey(Marca_SubCategoria)
	estado = models.BooleanField(default=True)

	class Meta:

		unique_together = ("distribuidora", "marcaSubCategoria")

	def __str__(self):
		return "%s %s" %(self.distribuidora, self.marcaSubCategoria)


class Producto_Distribudora (models.Model):
	distribuidora = models.ForeignKey(Distribuidora)
	marcaXSubcategoriaDistribuidora = models.ForeignKey(MarcaXSubcategoria_Distribuidora)
	producto = models.ForeignKey(Producto)
	presentacion = models.ForeignKey(Presentacion)
	precio_unitario = models.FloatField()
	stock = models.PositiveIntegerField()
	estado = models.BooleanField(default=True)

	class Meta:

		unique_together = ('distribuidora', 'marcaXSubcategoriaDistribuidora', 'producto', 'presentacion')

	def __str__(self):

		return "Producto %s - presentacion: %s" %(self.producto, self.presentacion)


class Ruta (models.Model):
	distribuidora = models.ForeignKey(Distribuidora)
	nombre = models.CharField(max_length=50)
	recorrido = models.TextField()
	dia = MultiSelectField(choices=DiasType, max_choices=7)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return "%s  --  %s" %(self.nombre, self.distribuidora)


class Negocio_Distribuidora (models.Model):  # Socio
	negocio = models.ForeignKey(Negocio)
	distribuidora = models.ForeignKey(Distribuidora)
	ruta = models.ForeignKey(Ruta, null=True, blank=True)
	alias_distribuidora = models.CharField(max_length=50, blank=True)
	alias_negocio = models.CharField(max_length=50, blank=True)
	estado = models.BooleanField(default=True)
	
	class Meta:
		unique_together = ("negocio", "distribuidora")
		
	def __str__(self):
		return "%s - %s" %(self.distribuidora.nombre, self.negocio.nombre)

class Anuncio (models.Model):

	def url(self,nombreArchivo):
		ruta = "imagenesAunicios/%s/%s" %(self.distribuidora.nombre,str(nombreArchivo))
		return ruta

	distribuidora = models.ForeignKey(Distribuidora)
	imagen = models.ImageField(upload_to=url, blank=True, null=True)
	titulo = models.CharField(max_length=50)
	descripcion = models.TextField()
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_inicio = models.DateField()
	fecha_fin = models.DateField()
	estado = models.BooleanField(default=True)

	def __str__(self):
		return "%s" %(self.titulo)
