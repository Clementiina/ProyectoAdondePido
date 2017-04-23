from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Solicitud, Distribuidora_Solicitud
from apps.distribuidoras.models import Distribuidora, Negocio_Distribuidora
from django.contrib.auth import authenticate, login
from apps.negocios.models import Negocio, Usuario_Negocio
from apps.personas.models import Persona
from django.views.generic import CreateView
from . import forms
import hashlib, random, datetime

class VistaSolicitud(CreateView):
	template_name = 'solicitud.html'
	model = User
	form_class = forms.UserForm
	form_class2 = forms.SolicitudForm
	
	def get(self, request):
		contexto={}
		contexto['distribuidoras'] = Distribuidora.objects.all()        
		return render(request, self.template_name, contexto)

	def validar(user):
		return HttpResponseRedirect('/sin_activar/')
	
	def post(self, request):
		formU = self.form_class(request.POST)
		formS = self.form_class2(request.POST)
		formS.is_valid() #crea cleaned_data
		formS.cleaned_data['fecha'] = datetime.datetime.now()
		formS.cleaned_data['usuario'] = 1 #para que acepte
		formS.cleaned_data['code'] = (str(hashlib.sha256(str(random.random()).encode('utf-8')).hexdigest())[:8])
		formS.cleaned_data['estado'] = 'p'
		print ("\n"+str (formU.is_valid()) +"\n" + str( formS.is_valid() ) + "\n")
		if formU.is_valid() and formS.is_valid():
			u = User.objects.create_user(formU.cleaned_data["username"],formU.cleaned_data["email"],formU.cleaned_data["password"])
			u.last_name = formU.cleaned_data["last_name"]
			u.first_name = formU.cleaned_data["first_name"]
			u.save()
			#login(request, u) #auto login
			formS.cleaned_data['usuario_id'] = u.id		
			formS.save()				
			
			distribuidoras = request.POST.getlist('lista')        
			for dist in distribuidoras:
				ds = Distribuidora_Solicitud()
				ds.solicitud_id = s.id
				ds.distribuidora_id = dist
				ds.save()
			return HttpResponseRedirect('/sin_activar/')
		contexto = {}
		contexto['error'] = 'El usuario ya existe'
		contexto['username'] = request.POST['username']
		contexto['email'] = request.POST['email']
		contexto['last_name'] = request.POST['last_name']
		contexto['first_name'] = request.POST['first_name']
		contexto['dni'] = request.POST['dni']
		contexto['telefono'] = request.POST['telefono']
		contexto['celular'] = request.POST['celular']
		contexto['localidad'] = request.POST['localidad']
		contexto['nombre'] = request.POST['nombre']
		contexto['descripcion'] = request.POST['descripcion']
		contexto['numero_contacto'] = request.POST['numero_contacto']
		contexto['direccion'] = request.POST['direccion']       
		contexto['distribuidoras'] = Distribuidora.objects.all()
		return render(request, self.template_name, contexto)

class VistaSolicitudes(TemplateView):
	template_name = 'solicitudes.html'
	
	def get(self, request):
		contexto={}
		solicitudes = Distribuidora_Solicitud.objects.filter(distribuidora_id=request.GET['dist'])
		contexto['dist'] = request.GET['dist']
		contexto['solicitudes'] = solicitudes
		contexto['s_cant'] = len(solicitudes)
		return render(request, self.template_name, contexto)

class VistaActivar(TemplateView):
	template_name = 'activar.html'
	
	def get(self, request):
		contexto={}
		s = Solicitud.objects.get(usuario_id=request.GET['user'] )
		contexto['dist'] = request.GET['dist']
		contexto['solicitud'] = s
		return render(request, self.template_name, contexto)
		
	def post(self, request):
		s = Solicitud.objects.get(usuario_id=request.GET['user'] )
		if (request.POST['code'] == s.code ):
			s.estado = 'a'
			s.save()
			p = Persona()
			p.usuario_id = request.GET['user']
			p.dni = s.dni
			p.telefono = s.telefono
			p.celular = s.celular
			p.localidad_id = s.localidad_id
			p.direccion = s.direccion
			p.estado = True
			p.save()
			n = Negocio()
			n.nombre = s.nombre
			n.descripcion = s.descripcion
			n.numero_contacto = s.numero_contacto
			n.localidad_id = s.localidad_id
			n.direccion = s.direccion
			n.persona_cargo_id = p.id
			n.save()
			u = Usuario_Negocio()
			u.permiso_id = 1 # PERMISO DE ADMINISTRADOR
			u.negocio_id = n.id
			u.usuario_id = request.GET['user']
			u.estado = True
			u.save()
			return HttpResponseRedirect('/solicitudes/?dist='+request.GET['dist'])
		contexto = {}
		contexto['error'] =  'Codigo incorrecto'
		contexto['dist'] = request.GET['dist']
		contexto['solicitud'] = s
		contexto['code'] = request.POST['code']
		return render(request, self.template_name, contexto)
		
class VistaAsociar(TemplateView):
	template_name = 'solicitudes.html'
	
	def get(self, request):
		n = Negocio.objects.get(persona_cargo_id__usuario_id=request.GET['user'] )
		socio = Negocio_Distribuidora()        
		socio.distribuidora_id = request.GET['dist']
		socio.negocio_id = n.id
		socio.save()        
		s = Distribuidora_Solicitud.objects.get(id = request.GET['s_id'])
		s.delete()
		return HttpResponseRedirect('/solicitudes/?dist='+request.GET['dist'])

class VistaIgnorar(TemplateView):
	template_name = 'solicitudes.html'
	
	def get(self, request):
		s = Distribuidora_Solicitud.objects.get(id = request.GET['s_id'])
		s.delete()
		return HttpResponseRedirect('/solicitudes/?dist='+request.GET['dist'])
