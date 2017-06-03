import json
from django.core import serializers
from django.http import HttpResponse
from .models import Producto

from apps.categorias.models import Marca_SubCategoria
from apps.distribuidoras.models import MarcaXSubcategoria_Distribuidora
from django.views.generic import TemplateView
from django.shortcuts import render


class VistaProducto(TemplateView):

	template_name = 'producto.html'

	def get(self, request):
		context = {}
		id = int(request.GET["dist"])
		#print(id)
		context["m_x_s_d"] = MarcaXSubcategoria_Distribuidora.objects.filter(distribuidora__id=id)
		return render(request, self.template_name, context) 



	
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



		