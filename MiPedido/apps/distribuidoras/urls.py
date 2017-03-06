# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.VistaDistribuidora.as_view(), name='distribuidora'),
    url(r'^(?P<pk>\d+)/anuncios/$', views.VistaAnuncio.as_view(), name='anuncios'),
    url(r'^crear_anuncio/$', views.CrearAnuncio.as_view(), name="crear_anuncio"),
    url(r'^detalle_anuncio/(?P<pk>\d+)/$', views.DetalleAnuncio.as_view(), name='detalle'),
	url(r'^rutas/$', views.VistaRuta.as_view(), name='rutas'),
	url(r'^rutas/crear_ruta/$', views.CrearRuta.as_view(), name="crear_ruta"),
	url(r'^rutas/detalle_ruta/$', views.DetalleRuta.as_view(), name='detalle_ruta'),
	url(r'^rutas/actualizar_ruta/$', views.ActualizarRuta.as_view(), name='actualizar_ruta'),
	url(r'^rutas_eliminar/$', views.EliminaRuta.as_view(), name='eliminar_ruta'),	
]

