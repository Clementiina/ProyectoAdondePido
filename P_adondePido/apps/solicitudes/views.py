from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Solicitud, Distribuidora_Solicitud
from apps.distribuidoras.models import Distribuidora, Negocio_Distribuidora, Usuario_Distribuidora
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
		
# NEGOCIOS

class VistaSolicitudN(CreateView):
	template_name = 'solicitud_n.html'
	model = Solicitud
	form_class = forms.SolicitudNForm
	
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
		
class VistaSolicitudesN(TemplateView):
	template_name = 'solicitudes_n.html'
	
	def get(self, request):
		contexto={}
		solicitudes = Distribuidora_Solicitud.objects.filter(distribuidora_id=request.GET['dist'])
		contexto['dist'] = Distribuidora.objects.get(id=request.GET['dist'])
		contexto['solicitudes'] = solicitudes
		contexto['s_cant'] = len(solicitudes)
		return render(request, self.template_name, contexto)
		
class VistaActivarN(TemplateView):
	template_name = 'activar_n.html'
	
	def get(self, request):
		contexto={}
		s = Solicitud.objects.get(user=request.GET['user'] )
		contexto['dist'] = Distribuidora.objects.get(id=request.GET['dist'])
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
			un = Usuario_Negocio()
			un.permiso_id = 1 # PERMISO DE ADMINISTRADOR
			un.negocio_id = n.id
			un.usuario_id = request.GET['user']
			un.estado = True
			un.save()
			return HttpResponseRedirect('/solicitudes/n?dist='+request.GET['dist'])
		contexto = {}
		contexto['error'] =  'Codigo incorrecto'
		contexto['dist'] = Distribuidora.objects.get(id=request.GET['dist'])
		contexto['solicitud'] = s
		contexto['code'] = request.POST['code']
		return render(request, self.template_name, contexto)
		
class VistaAsociarN(TemplateView):
	template_name = 'solicitudes_n.html'
	
	def get(self, request):
		n = Negocio.objects.get(persona_cargo_id__usuario_id=request.GET['user'] )
		socio = Negocio_Distribuidora()        
		socio.distribuidora_id = request.GET['dist']
		socio.negocio_id = n.id
		socio.save()        
		s = Distribuidora_Solicitud.objects.get(id = request.GET['s_id'])
		s.delete()
		return HttpResponseRedirect('/solicitudes/n?dist='+request.GET['dist'])

class VistaIgnorarN(TemplateView):
	template_name = 'solicitudes_n.html'
	
	def get(self, request):
		s = Distribuidora_Solicitud.objects.get(id = request.GET['s_id'])
		s.delete()
		return HttpResponseRedirect('/solicitudes/n?dist='+request.GET['dist'])

# DISTRIBUIDORAS

class VistaSolicitudD(CreateView):
	template_name = 'solicitud_d.html'
	model = Solicitud
	form_class = forms.SolicitudDForm
	
	def get(self, request):
		contexto={}
		return render(request, self.template_name, contexto)
	
	def post(self, request):
		formS = self.form_class(request.POST)
		ok = formS.is_valid()
		contexto = formS.cleaned_data
		contexto['error'] = []
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
			s.es_distribuidora = True
			u = User.objects.create_user(formS.cleaned_data["usuario"],formS.cleaned_data["email"],request.POST["password"])
			u.last_name = formS.cleaned_data["apellido"]
			u.first_name = formS.cleaned_data["nombre"]
			u.is_active = False
			u.save()
			s.user_id=u.id
			s.save()
			#auto login		
			u = authenticate(username=u.username, password=request.POST["password"])
			login(request, u)
			return HttpResponseRedirect('/sin_activar/') 
		#reporta errores
		contexto['form'] = formS
		return render(request, self.template_name, contexto)

class VistaSolicitudesD(TemplateView):
	template_name = 'solicitudes_d.html'
	
	def get(self, request):
		contexto={}
		solicitudes = Solicitud.objects.filter(es_distribuidora=True)
		contexto['solicitudes'] = solicitudes
		contexto['s_cant'] = len(solicitudes)
		return render(request, self.template_name, contexto)
		
class VistaActivarD(TemplateView):
	template_name = 'activar_d.html'
	
	def get(self, request):
		contexto={}
		s = Solicitud.objects.get(user=request.GET['user'] )
		contexto['solicitud'] = s
		return render(request, self.template_name, contexto)
	
	def post(self, request):
		s = Solicitud.objects.get(id = request.GET['s_id'])
		u = User.objects.get(username=s.usuario)
		u.is_active = True
		u.save()
		p = Persona()
		p.usuario_id = u.id
		p.dni = s.dni
		p.telefono = s.telefono
		p.celular = s.celular
		p.localidad_id = s.localidad_id
		p.direccion = s.direccion
		p.estado = True
		p.save()
		d = Distribuidora()
		d.cuit = s.cuit
		d.nombre = s.n_nombre
		d.descripcion = s.descripcion
		d.numero_contacto = s.numero_contacto
		d.localidad_id = s.localidad_id
		d.direccion = s.direccion
		d.persona_cargo_id = p.id
		d.save()
		ud = Usuario_Distribuidora()
		ud.permiso_id = 1 # PERMISO DE ADMINISTRADOR
		ud.distribuidora_id = d.id
		ud.usuario_id = u.id
		ud.estado = True
		ud.save()
		s.delete()
		return HttpResponseRedirect('/')

class VistaIgnorarD(TemplateView):
	template_name = 'solicitudes_d.html'
	
	def get(self, request):
		s = Solicitud.objects.get(id = request.GET['s_id'])
		u = User.objects.get(id = s.user_id)
		u.delete()
		s.delete()
		return HttpResponseRedirect('/')
