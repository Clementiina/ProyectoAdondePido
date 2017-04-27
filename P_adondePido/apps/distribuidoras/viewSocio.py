from .models import Negocio_Distribuidora
from apps.negocios.models import Negocio
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.http import HttpResponseRedirect

class Socios(ListView):
	model = Negocio_Distribuidora
	template_name = 'socios.html'
	context_object_name = 'socios'
	def get(self, request):
		contexto = {}
		contexto['dist'] = request.GET['dist']
		contexto['socios'] = Negocio_Distribuidora.objects.filter(distribuidora__id=request.GET['dist'])
		return render(request, 'socios.html', contexto)

class verSocio(DetailView):
	model = Negocio_Distribuidora
	context_object_name = 'socio'
	template_name = "detalle_socio.html"
	def get(self, request):
		contexto = {}
		s = Negocio.objects.get(id=request.GET['s_id'] )
		contexto['dist'] = request.GET['dist']
		contexto['socio'] = s
		return render(request, 'detalle_socio.html', contexto)

class Desasociar(TemplateView):
	template_name = 'solicitudes.html'
	
	def get(self, request):
		n = Negocio_Distribuidora.objects.get(negocio_id = request.GET['s_id'])
		n.delete()
		contexto = {}
		contexto['dist'] = request.GET['dist']
		contexto['ruta'] = request.GET['ruta']
		contexto['rutas'] = Ruta.objects.filter(distribuidora__id=request.GET['dist'])
		return HttpResponseRedirect('/distribuidoras/socios/?dist='+request.GET['dist'])
