# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.VistaSolicitudes.as_view(), name='solicitudes'),
	url(r'^solicitud/$', views.VistaSolicitud.as_view(), name='solicitud'),	
	url(r'^solicitud/activar/$', views.VistaActivar.as_view(), name='activar'),
	url(r'^solicitud/asociar/$', views.VistaAsociar.as_view(), name='asociar'),
	url(r'^solicitud/ignorar/$', views.VistaIgnorar.as_view(), name='ignorar'),
]
