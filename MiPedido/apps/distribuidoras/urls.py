# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.VistaDistribuidora.as_view(), name='distribuidora'),
    url(r'^anuncios/$', views.VistaAnuncio.as_view(), name='anuncios'),
    url(r'^crear_anuncio/$', views.CrearAnuncio.as_view(), name="crear_anuncio"),
     url(r'^actualizar_anuncio/$', views.ActualizarAnuncio.as_view(),
                             name='actualizar_anuncio'),
	url(r'^crear_ruta/$', views.CrearRuta.as_view(), name="crear_ruta"),
]
