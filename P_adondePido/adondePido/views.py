from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from apps.distribuidoras.models import Usuario_Distribuidora, Distribuidora
from apps.negocios.models import Usuario_Negocio, Negocio
from apps.solicitudes.models import Solicitud

class CtrLogin(object):
	@classmethod
	def as_view(cls, **initkwargs):
		view = super(CtrLogin, cls).as_view(**initkwargs)
		return login_required(view, login_url="/login/")

class Index(CtrLogin, TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		contexto = super(Index, self).get_context_data(**kwargs)
		contexto['distribuidoras'] = Usuario_Distribuidora.objects.filter(usuario = self.request.user.id)
		contexto['negocios'] = Usuario_Negocio.objects.filter(usuario = self.request.user.id)
		print(contexto)
		return contexto

class Login(TemplateView):

	template_name = 'login.html'

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			if user.is_active:
				return HttpResponseRedirect('/')
			return HttpResponseRedirect('/sin_activar')			
		else:
			contexto = {'error': True}
			return render(request, self.template_name, contexto)

class SinActivar(TemplateView):

	template_name = 'sin_activar.html'

	def get(self, request):
		print(request)
		s = Solicitud.objects.get(user=self.request.user.id)
		contexto={}
		contexto['codigo']= s.code
		return render(request, self.template_name, contexto)

class Salir(CtrLogin, TemplateView):

	def get(self, request):
		logout(request)
		return HttpResponseRedirect('/logout/')


class Logout(TemplateView):
	template_name = 'logout.html'
