# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',

    url(r'^crear_anuncio/$', views.CrearAnuncio.as_view(), name="crear_anuncio"),
	url(r'^crear_ruta/$', views.CrearRuta.as_view(), name="crear_ruta"),

    )

 #url(r'^$', Home.as_view(), name='home')