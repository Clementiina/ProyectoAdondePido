"""adondePido URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import Index, Login, Salir, Logout, SinActivar
from apps.distribuidoras import views
from django.conf import settings

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^salir/', Salir.as_view(), name='salir'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^distribuidoras/', include('apps.distribuidoras.urls')),
	url(r'^negocios/', include('apps.negocios.urls', namespace='negocio')),
    url(r'^productos/', include('apps.productos.urls')),
	url(r'^solicitudes/', include('apps.solicitudes.urls')),
	url(r'^sin_activar/', SinActivar.as_view(), name='sin_activar'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT, }), # Es el servidor de medios,
       #sirve para que las imegenes de muestren. Cogote ... no lo borres :-(
]
