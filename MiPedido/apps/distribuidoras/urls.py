# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import CrearAnuncio

urlpatterns = patterns('',

    url(r'^crear_anuncio/$', CrearAnuncio.as_view(), name="crear_anuncio"),

    )

 #url(r'^$', Home.as_view(), name='home')