# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^anuncios/$', views.Anuncios.as_view(), name='anuncios'),
    url(r'^crear_anuncio/$', views.CrearAnuncio.as_view(), name="crear_anuncio"),
    url(r'^detalle_anuncio/(?P<pk>\d+)/$', views.DetalleAnuncio.as_view(), name='detalle'),
]

