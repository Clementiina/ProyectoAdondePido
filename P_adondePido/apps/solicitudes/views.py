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

def validar(user):
	try:
		u = User.objects.get(username=user)
		return False
	except User.DoesNotExist:
		return True

class VistaSolicitud(CreateView):
	template_name = 'solicitud.html'
	model = Solicitud
	form_class = forms.SolicitudForm
	
	def get(self, request):
		contexto={}
		contexto['distribuidoras'] = Distribuidora.objects.all()        
		return render(request, self.template_name, contexto)

	
	def post(self, request):
		formS = self.form_class(request.POST)
		distribuidoras = request.POST.getlist('lista')
		ok = formS.is_valid()
		contexto = formS.cleaned_data
		contexto['error'] = []
		if len(distribuidoras)==0 :
			contexto['error'].append('d')
			ok = False
		if not validar(request.POST["usuario"]):			
			contexto['error'].append('usuario')
			#formS.add_error('usuario')
			ok = False
		if len(request.POST["password"])==0 or len(request.POST["r_password"])==0 :
			contexto['error'].append('password')
			ok = False		
		if ok:
			s = formS.save(commit=False)
			s.fecha = datetime.datetime.now()
			s.code = (str(hashlib.sha256(str(random.random()).encode('utf-8')).hexdigest())[:8])
			u = User.objects.create_user(formS.cleaned_data["usuario"],formS.cleaned_data["email"],request.POST["password"])
			u.last_name = formS.cleaned_data["apellido"]
			u.first_name = formS.cleaned_data["nombre"]
			u.is_active = False
			u.save()
			s.user_id=u.id
			s.save()
			for dist in distribuidoras:
				ds = Distribuidora_Solicitud()
				ds.solicitud_id = s.id
				ds.distribuidora_id = dist
				ds.save()
			#auto login		
			u = authenticate(username=u.username, password=request.POST["password"])
			login(request, u)
			return HttpResponseRedirect('/sin_activar/') 
		#reporta errores
		contexto['form'] = formS
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
		s = Solicitud.objects.get(user=request.GET['user'] )
		contexto['dist'] = request.GET['dist']
		contexto['solicitud'] = s
		return render(request, self.template_name, contexto)
		
	def post(self, request):
		s = Solicitud.objects.get(user_id=request.GET['user'] )
		if (request.POST['code'] == s.code ):
			u = User.objects.get(id=request.GET['user'] )
			u.is_active = True
			u.save()
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
			n.nombre = s.n_nombre
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
