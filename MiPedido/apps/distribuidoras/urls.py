# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import CrearAnuncio, ListaAnuncios, DetalleAnuncio

urlpatterns = patterns('',

    url(r'^crear_anuncio/$', CrearAnuncio.as_view(), name="crear_anuncio"),
    url(r'^listar_anuncios/$', ListaAnuncios.as_view(), name="lista_anuncio"),
    url(r'^detalle_anuncio/(?P<pk>\d+)/$', DetalleAnuncio.as_view(),
                                            name='detalle'),

    )

 #url(r'^$', Home.as_view(), name='home')