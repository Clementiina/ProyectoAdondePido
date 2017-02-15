from django.contrib import admin

from .models import Permiso_Kiosko  # ,Usuario_Kiosko, Kiosko


class  Permiso_KioskoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")


#class KioskoAdmin (admin.ModelAdmin):
    #list_display = ("nombre", "numero_contacto", "direccion")


#class Usuario_KioskoAdmin (admin.ModelAdmin):
    #list_display = ('id_kiosko', 'id_usuario', 'id_permiso')


admin.site.register(Permiso_Kiosko, Permiso_KioskoAdmin)
#admin.site.register(Kiosko, KioskoAdmin)
#admin.site.register(Usuario_Kiosko, Usuario_KioskoAdmin)

# Register your models here.


##default
from .models import Kiosko, Usuario_Kiosko
admin.site.register(Kiosko)
admin.site.register(Usuario_Kiosko)
