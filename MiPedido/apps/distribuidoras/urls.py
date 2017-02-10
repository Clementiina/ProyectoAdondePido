from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^anuncios/$', views.Anuncios.as_view(), name='anuncios'),
]