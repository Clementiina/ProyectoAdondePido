from django.contrib import admin
from .models import Presentacion

class PresentacionAdmin(admin.ModelAdmin):
	list_display = ("capacidad", )

admin.site.register(Presentacion, PresentacionAdmin)

#default
from .models import Tipo_Producto, Producto
admin.site.register(Tipo_Producto)
admin.site.register(Producto)