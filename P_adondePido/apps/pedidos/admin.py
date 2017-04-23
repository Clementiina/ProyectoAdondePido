from django.contrib import admin

#default
from .models import Pedido, Detalle_Pedido
admin.site.register(Pedido)
admin.site.register(Detalle_Pedido)