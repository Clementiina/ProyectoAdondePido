from django.contrib import admin
from .models import Provincia, Departamento, Localidad

class ProvinciaAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'estado']
	ordering = ['nombre']
	search_fields = ['nombre']

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'id_provincia', 'estado']
	ordering = ['nombre', 'id_provincia']
	search_fields = ['nombre']
	raw_id_fields = ['id_provincia']

class LocalidadAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'codigo_postal', 'id_departamento', 'estado']
	ordering = ['nombre']
	search_fields = ['nombre']
	raw_id_fields = ['id_departamento']

admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Localidad, LocalidadAdmin)
