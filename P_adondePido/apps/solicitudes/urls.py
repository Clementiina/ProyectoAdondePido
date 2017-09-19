# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^n$', views.VistaSolicitudesN.as_view(), name='solicitudes_n'),
	url(r'^solicitud_n/$', views.VistaSolicitudN.as_view(), name='solicitud_n'),	
	url(r'^solicitud_n/activar_n/$', views.VistaActivarN.as_view(), name='activar_n'),
	url(r'^solicitud_n/asociar_n/$', views.VistaAsociarN.as_view(), name='asociar_n'),
	url(r'^solicitud_n/ignorar_n/$', views.VistaIgnorarN.as_view(), name='ignorar_n'),
	
	url(r'^d$', views.VistaSolicitudesD.as_view(), name='solicitudes_d'),
	url(r'^solicitud_d/$', views.VistaSolicitudD.as_view(), name='solicitud_d'),	
	url(r'^solicitud_d/activar_d/$', views.VistaActivarD.as_view(), name='activar_d'),
	url(r'^solicitud_d/ignorar_d/$', views.VistaIgnorarD.as_view(), name='ignorar_d'),
	
]
