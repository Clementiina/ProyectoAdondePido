import json
from django.core import serializers
from django.http import HttpResponse
from .models import Producto

from apps.categorias.models import Marca_SubCategoria
from django.views.generic import TemplateView
from django.shortcuts import render


class VistaProducto(TemplateView):
	template_name = 'producto.html'

	
"""
class SelectProducto(TemplateView):
	
	def get(self, request):
		pass

class SelectMarca(TemplateView):

	def get(self, request):
		pass


class SelectDescripcion(TemplateView):
	
	def get(self, request):
		pass
class SelectPresentacion(TemplateView):
	
	def get(self, request):
		pass
"""



		