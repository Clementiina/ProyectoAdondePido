from django.contrib import admin
from .models import Producto, Presentacion, Tipo_Presentacion

class PresentacionAdmin(admin.ModelAdmin):
	list_display = ("capacidad", )

class Tipo_PresentacionAdmin(admin.ModelAdmin):
	list_display = ("id", "nombre",)


admin.site.register(Producto)
admin.site.register(Tipo_Presentacion, Tipo_PresentacionAdmin)
admin.site.register(Presentacion, PresentacionAdmin)
