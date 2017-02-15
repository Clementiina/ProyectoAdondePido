from django.contrib import admin
from .models import Marca, Categoria

class MarcaAdmin(admin.ModelAdmin):
	list_display = ['nombre']
	search_fields = ['nombre']
	ordering = ['nombre']

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ['nombre']
	search_fields = ['nombre']
	ordering = ['nombre']

admin.site.register(Marca, MarcaAdmin)
admin.site.register(Categoria, CategoriaAdmin)

##default
from .models import SubCategoria,Marca_SubCategoria
admin.site.register(SubCategoria)
admin.site.register(Marca_SubCategoria)
