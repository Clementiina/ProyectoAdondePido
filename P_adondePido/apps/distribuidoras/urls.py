# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views, viewAnuncio, viewRuta, viewSocio

urlpatterns = [
    url(r'^$', views.VistaDistribuidora.as_view(), name='distribuidora'),
    url(r'^anuncios/$', viewAnuncio.VistaAnuncio.as_view(), name='anuncios'),
    url(r'^crear_anuncio/$', viewAnuncio.CrearAnuncio.as_view(), name="crear_anuncio"),
    url(r'^actualizar_anuncio/$', viewAnuncio.ActualizarAnuncio.as_view(), name='actualizar_anuncio'),
    url(r'^eliminar_anuncio/$', viewAnuncio.EliminarAnuncio.as_view(), name="eliminar_anuncio"),
	url(r'^rutas/$', viewRuta.VistaRuta.as_view(), name='rutas'),
	url(r'^rutas/crear_ruta/$', viewRuta.CrearRuta.as_view(), name="crear_ruta"),
	url(r'^rutas/detalle_ruta/$', viewRuta.DetalleRuta.as_view(), name='detalle_ruta'),
	url(r'^rutas/actualizar_ruta/$', viewRuta.ActualizarRuta.as_view(), name='actualizar_ruta'),
	url(r'^rutas_eliminar/$', viewRuta.EliminaRuta.as_view(), name='eliminar_ruta'),
	url(r'^socios/$', viewSocio.Socios.as_view(), name='socios'),
	url(r'^socios/detalle_socio/$', viewSocio.verSocio.as_view(), name='detalle_socio'),
	url(r'^socios_desasociar/$', viewSocio.Desasociar.as_view(), name='desasociar'),	
]
