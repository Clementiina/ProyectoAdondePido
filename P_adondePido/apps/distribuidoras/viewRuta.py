from .models import Ruta , DiasType
from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms

class CrearRuta(CreateView):
	template_name = 'adm_ruta.html'
	model = Ruta
	form_class = forms.RutaForm
	
	def get(self, request ):
		contexto = {}
		contexto['dist'] = request.GET['dist']
		contexto['DiasType'] = DiasType
		return render(request, 'adm_ruta.html', contexto)

	def post(self, request):
		formR = self.form_class(request.POST)
		ok = formR.is_valid()
		contexto = formR.cleaned_data
		if ok:
			r = formR.save(commit=False)
			r.distribuidora_id = request.GET['dist'] 		
			r.estado = True  # activa
			r.save()
			return HttpResponseRedirect('/distribuidoras/rutas?dist='+request.GET['dist'] )
		contexto['form'] = formR
		contexto['dist'] = request.GET['dist']
		contexto['DiasType'] = DiasType
		return render(request, self.template_name, contexto)
		
class DetalleRuta(DetailView):
	model = Ruta
	context_object_name = 'ruta'
	template_name = "detalle_ruta.html"
	def get(self, request):
		contexto = {}
		r = Ruta.objects.get(id=request.GET['ruta'] )
		contexto['dist'] = request.GET['dist']
		contexto['ruta'] = r
		for x,y in DiasType:
			if x == r.dia:
				contexto['dia'] = y
				break
		return render(request, 'detalle_ruta.html', contexto)

class VistaRuta(ListView):
	model = Ruta
	template_name = 'rutas.html'
	context_object_name = 'rutas'
	def get(self, request):
		contexto = {}
		contexto['dist'] = request.GET['dist']
		contexto['rutas'] = Ruta.objects.filter(distribuidora__id=request.GET['dist'])
		return render(request, 'rutas.html', contexto)

class EliminaRuta(ListView):
	model = Ruta
	template_name = 'rutas.html'
	context_object_name = 'rutas'
	
	def get(self, request):
		contexto = {}
		r = Ruta.objects.get(id=request.GET['ruta'])
		r.estado = False
		r.save()
		contexto['dist'] = request.GET['dist']
		contexto['ruta'] = request.GET['ruta']
		contexto['rutas'] = Ruta.objects.filter(distribuidora__id=request.GET['dist'])
		return HttpResponseRedirect('/distribuidoras/rutas/?dist='+request.GET['dist'])

class ActualizarRuta(TemplateView):
	template_name = 'adm_ruta.html'
	model = Ruta
	form_class = forms.RutaForm
	
	def get(self, request ):
		contexto = {}
		contexto['DiasType'] = DiasType
		contexto['dist'] = request.GET['dist']
		contexto['edit'] = True
		r = Ruta.objects.get(id=request.GET['ruta'])		
		contexto['nombre'] = r.nombre
		contexto['recorrido'] = r.recorrido
		contexto['dia'] = r.dia
		contexto['estado'] = r.estado
		contexto["ruta"] = request.GET["ruta"]
		return render(request, 'adm_ruta.html', contexto)

	def post(self, request):
		print(request.GET)
		r = Ruta.objects.get(id=request.GET['ruta'])
		formR = self.form_class(request.POST, instance=r)
		ok = formR.is_valid()
		contexto = formR.cleaned_data
		if ok:
			formR.save()
			return HttpResponseRedirect('/distribuidoras/rutas?dist='+request.GET['dist'] )
		contexto['edit'] = True
		contexto['form'] = formR
		contexto['DiasType'] = DiasType
		contexto['dist'] = request.GET['dist']		
		return render(request, self.template_name, contexto)
