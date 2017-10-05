# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views, viewsPedido

urlpatterns = [
    url(r'^$', views.Vista_Negocio.as_view(), name='negocio'),
    url(r'^inicio_pedido/$', viewsPedido.Inicio_Pedido.as_view(), name='inicio_pedido'),
    url(r'^p_lista_productos/$', viewsPedido.Lista_Productos.as_view(), name='lista_productos'),
    url(r'^p_detalle_pedido/$', viewsPedido.Detalle_De_Pedido.as_view(), name='detalle_pedido'),
    url(r'^p_actualizar_pedido/$', viewsPedido.Actualizar_Pedido.as_view(), name='actualizar_pedido'),
    url(r'^p_eliminar_pedido/(?P<pk>.+)/$', viewsPedido.Eliminar_Pedido.as_view(), name='eliminar_pedido'),
    url(r'^p_enviar_pedido/(?P<pk>.+)/$', viewsPedido.Enviar_Pedido.as_view(), name='enviar_pedido'),
    #url(r'^actualizar_producto/(?P<pk>.+)/$', viewProducto.Actualizar_Producto.as_view(), name='actualizar_producto'),
	
]
