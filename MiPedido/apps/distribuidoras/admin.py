from django.contrib import admin
from .models import Anuncio, Permiso_Distribudora, Ruta


class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha_ini', 'fecha_end')
    search_fields = ['titulo']

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
