# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import CrearAnuncio, CrearRuta

urlpatterns = patterns('',

    url(r'^crear_anuncio/$', CrearAnuncio.as_view(), name="crear_anuncio"),
	url(r'^crear_ruta/$', CrearRuta.as_view(), name="crear_ruta"),

    )

 #url(r'^$', Home.as_view(), name='home')