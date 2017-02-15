from django.contrib import admin

##default
from .models import Estado_Pedido, Pedido, Detalle_Pedido
admin.site.register(Estado_Pedido)
admin.site.register(Pedido)
admin.site.register(Detalle_Pedido)
