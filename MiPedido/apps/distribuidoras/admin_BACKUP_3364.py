from django.contrib import admin
from .models import Anuncio, Permiso_Distribuidora, Ruta
from .models import Anuncio, Permiso_Distribuidora, Distribuidora, Usuario_Distribuidora




class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha_creacion', 'fecha_inicio', 'fecha_fin', 'estado')
    search_fields = ['titulo']
    raw_id_fields = ['id_distribuidora']


class Permiso_DistribuidoraAdmin(admin.ModelAdmin):
    list_display = ("nombre", 'descripcion')


class RutaAdmin(admin.ModelAdmin):
    #id_distribudora
    #nombre
    #recorrido
    #dia
    list_display = ('id_distribudora', 'nombre', 'recorrido', 'dia' )
    search_fields = ('id_distribudora', 'nombre', 'recorrido', 'dia' )

admin.site.register(Anuncio, AnuncioAdmin)
admin.site.register(Permiso_Distribudora, Permiso_DistribuidoraAdmin)
admin.site.register(Ruta, RutaAdmin)
class DistribuidoraAdmin(admin.ModelAdmin):
    list_display = ("nombre", 'descripcion')

admin.site.register(Anuncio, AnuncioAdmin)
admin.site.register(Permiso_Distribuidora, Permiso_DistribuidoraAdmin)
admin.site.register(Distribuidora, DistribuidoraAdmin)
admin.site.register(Usuario_Distribuidora)
