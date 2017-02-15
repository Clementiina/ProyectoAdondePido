from django.contrib import admin
from .models import Anuncio, Permiso_Distribuidora, Distribuidora, Usuario_Distribuidora

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha_creacion', 'fecha_inicio', 'fecha_fin')
    search_fields = ['titulo']
    raw_id_fields = ['id_distribuidora']

class Permiso_DistribuidoraAdmin(admin.ModelAdmin):
    list_display = ("nombre", 'descripcion')

<<<<<<< HEAD
admin.site.register(Anuncio)
admin.site.register(Permiso_Distribuidora, Permiso_DistribuidoraAdmin)

##default
from .models import Distribuidora, Usuario_Distribuidora, TipoProducto_Distribuidora, Producto_Distribudora, Ruta, Kiosko_Distribuidora
admin.site.register(Distribuidora)
admin.site.register(Usuario_Distribuidora)
admin.site.register(TipoProducto_Distribuidora)
admin.site.register(Producto_Distribudora)
admin.site.register(Ruta)
admin.site.register(Kiosko_Distribuidora)
=======

class DistribuidoraAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'descripcion', 'numero_contacto', 'id_localidad', 'direccion', 'persona_cargo', 'estado']
	ordering = ['nombre']
	search_fields = ['nombre']
	raw_id_fields = ['id_localidad', 'persona_cargo']

class Usuario_DistribuidoraAdmin(admin.ModelAdmin):
	list_display = ['id_distribuidora', 'id_usuario', 'id_permiso', 'estado']
	search_fields = ['id_usuario', 'id_distribuidora']
	raw_id_fields = ['id_distribuidora', 'id_usuario']

admin.site.register(Anuncio, AnuncioAdmin)
admin.site.register(Permiso_Distribuidora, Permiso_DistribuidoraAdmin)
admin.site.register(Distribuidora, DistribuidoraAdmin)
admin.site.register(Usuario_Distribuidora, Usuario_DistribuidoraAdmin)
>>>>>>> 35c32d9841b2e6924b54e278ece608412a98d504
