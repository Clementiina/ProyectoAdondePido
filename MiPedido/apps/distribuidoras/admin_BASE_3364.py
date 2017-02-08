from django.contrib import admin
from .models import Anuncio, Permiso_Distribuidora


class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha_creacion', 'fecha_inicio', 'fecha_fin')
    search_fields = ['titulo']
    raw_id_fields = ['id_distribuidora']


class Permiso_DistribuidoraAdmin(admin.ModelAdmin):
    list_display = ("nombre", 'descripcion')


admin.site.register(Anuncio, AnuncioAdmin)
admin.site.register(Permiso_Distribuidora, Permiso_DistribuidoraAdmin)
# Register your models here.
