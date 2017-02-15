from django.contrib import admin
from .models import Anuncio, Permiso_Distribuidora

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha_creacion', 'fecha_inicio', 'fecha_fin')
    search_fields = ['titulo']
    raw_id_fields = ['id_distribuidora']

class Permiso_DistribuidoraAdmin(admin.ModelAdmin):
    list_display = ("nombre", 'descripcion')

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
