from django.contrib import admin
from .models import Anuncio, Permiso_Distribuidora, Distribuidora, Usuario_Distribuidora


class AnuncioAdmin(admin.ModelAdmin):
	list_display = ('id', 'titulo', 'fecha_creacion', 'fecha_inicio', 'fecha_fin')
	search_fields = ['titulo']
	raw_fields = ['distribuidora']


class Permiso_DistribuidoraAdmin(admin.ModelAdmin):
	list_display = ("nombre", 'descripcion')


class DistribuidoraAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'descripcion', 'numero_contacto', 'localidad', 'direccion', 'persona_cargo', 'estado']
	ordering = ['nombre']
	search_fields = ['nombre']
	raw_fields = ['localidad', 'persona_cargo']

class Usuario_DistribuidoraAdmin(admin.ModelAdmin):
	list_display = ['distribuidora', 'usuario', 'permiso', 'estado']
	search_fields = ['usuario', 'distribuidora']
	raw_fields = ['distribuidora', 'usuario']

admin.site.register(Anuncio, AnuncioAdmin)
admin.site.register(Permiso_Distribuidora, Permiso_DistribuidoraAdmin)
admin.site.register(Distribuidora, DistribuidoraAdmin)
admin.site.register(Usuario_Distribuidora, Usuario_DistribuidoraAdmin)

from .models import TipoProducto_Distribuidora,Producto_Distribudora, Ruta, Negocio_Distribuidora
admin.site.register(TipoProducto_Distribuidora)
admin.site.register(Producto_Distribudora)
admin.site.register(Ruta)
admin.site.register(Negocio_Distribuidora)

