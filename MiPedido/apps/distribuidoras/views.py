from django.shortcuts import render
from django.views.generic import ListView

from .models import Anuncio

class Anuncios(ListView):
	model = Anuncio
	template_name = 'anuncios.html'
	context_object_name = "anuncios"
