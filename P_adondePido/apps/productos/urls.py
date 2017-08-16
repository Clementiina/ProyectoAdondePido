# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^buscaMarcaAjax/$', views.BuscaMarcaAjax.as_view()),
	url(r'^selecCategriaAjax/$', views.SelecCategriaAjax.as_view()),
	url(r'^selecSubCategriaAjax/$', views.SelecSubCategriaAjax.as_view()),
	url(r'^selecTipo_PresentacionAjax/$', views.SelecTipo_PresentacionAjax.as_view()),
]
