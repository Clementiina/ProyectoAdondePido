from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from apps.distribuidoras.models import Usuario_Distribuidora, Distribuidora
from apps.solicitudes.models import Distribuidora_Solicitud
from apps.negocios.models import Usuario_Negocio, Negocio
from apps.solicitudes.models import Solicitud
from adondePido.forms import UserForm  


class CtrLogin(object):
	@classmethod
	def as_view(cls, **initkwargs):
		view = super(CtrLogin, cls).as_view(**initkwargs)
		return login_required(view, login_url="/")

class Index(CtrLogin, TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		contexto = super(Index, self).get_context_data(**kwargs)
		contexto['distribuidoras'] = Usuario_Distribuidora.objects.filter(usuario = self.request.user.id)
		contexto['negocios'] = Usuario_Negocio.objects.filter(usuario = self.request.user.id)
		contexto['sds'] = Solicitud.objects.filter(es_distribuidora=True)
		contexto['sd_cant'] = len(contexto['sds'])
		return contexto

class SinActivar(TemplateView):

	template_name = 'sin_activar.html'

	def get(self, request):
		s = Solicitud.objects.get(user=self.request.user.id)
		contexto={}
		contexto['s']= s
		return render(request, self.template_name, contexto)

class Salir(CtrLogin, TemplateView):

	def get(self, request):
		logout(request)
		return HttpResponseRedirect('/')

class Principal(TemplateView):
	template_name="principal.html"
 

class Login(TemplateView):
    template_name = 'login.html'
    form_class = UserForm	

    def get_context_data(self, **kwargs):
    	ctx = super(Login, self).get_context_data(**kwargs)
    	ctx["form"] = UserForm() #self.form_class()
    	return ctx

    def post(self, request):
    	formulario = self.form_class(request.POST)
    	if formulario.is_valid():
    		usuario = formulario.cleaned_data["usuario"]
    		clave = formulario.cleaned_data["clave"]
    		user = authenticate(username=usuario, password=clave)
    		if user is not None:
    			if user.is_active:
    				login(request,user)
    				return HttpResponseRedirect("/index")
    			else:
    				return HttpResponseRedirect('/sin_activar')			
    		else:
    			contexto = {'error': True}
    			return render(request, self.template_name, contexto)
    	else:
    		return HttpResponseRedirect("/principal")
