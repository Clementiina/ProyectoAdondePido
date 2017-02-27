# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.VistaDistribuidora.as_view(), name='distribuidora'),
    url(r'^anuncios/$', views.VistaAnuncio.as_view(), name='anuncios'),
    url(r'^crear_anuncio/$', views.CrearAnuncio.as_view(), name="crear_anuncio"),
    url(r'^detalle_anuncio/(?P<pk>\d+)/$', views.DetalleAnuncio.as_view(), name='detalle'),
	url(r'^crear_ruta/$', views.CrearRuta.as_view(), name="crear_ruta"),
]

