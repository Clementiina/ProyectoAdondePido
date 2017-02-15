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
<<<<<<< HEAD

##default
from .models import Localidad
admin.site.register(Localidad)

=======
admin.site.register(Localidad, LocalidadAdmin)
>>>>>>> 35c32d9841b2e6924b54e278ece608412a98d504
