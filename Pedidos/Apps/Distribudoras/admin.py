from django.contrib import admin
from .models import Anuncio, Permiso_Distribudora


class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha_ini', 'fecha_end')
    search_fields = ['titulo']


class Permiso_DistribuidoraAdmin(admin.ModelAdmin):
    list_display = ("nombre", 'descripcion')


admin.site.register(Anuncio, AnuncioAdmin)
admin.site.register(Permiso_Distribudora, Permiso_DistribuidoraAdmin)
# Register your models here.
