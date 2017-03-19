from django.contrib import admin

from .models import Permiso_Negocio, Usuario_Negocio, Negocio


class  Permiso_NegocioAdmin(admin.ModelAdmin):
	list_display = ("nombre", "descripcion")


class NegocioAdmin (admin.ModelAdmin):
	list_display = ("nombre", "numero_contacto", "direccion")


class Usuario_NegocioAdmin (admin.ModelAdmin):
	list_display = ('negocio', 'usuario', 'permiso')


admin.site.register(Permiso_Negocio, Permiso_NegocioAdmin)
admin.site.register(Negocio, NegocioAdmin)
admin.site.register(Usuario_Negocio, Usuario_NegocioAdmin)
