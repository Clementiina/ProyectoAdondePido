from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from apps.distribuidoras.models import Distribuidora
from apps.kioskos.models import Kiosko

class CtrLogin(object):
	@classmethod
	def as_view(cls, **initkwargs):
		view = super(CtrLogin, cls).as_view(**initkwargs)
		return login_required(view, login_url="/login/")

class Index(CtrLogin, TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		contexto = super(Index, self).get_context_data(**kwargs)
		contexto['distribuidoras'] = Distribuidora.objects.filter(persona_cargo__username = self.request.user.username)
		contexto['kioskos'] = Kiosko.objects.filter(persona_cargo__username = self.request.user.username)
		return contexto

class Login(TemplateView):
	template_name = 'login.html'

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			contexto = {'error': True}
			return render(request, self.template_name, contexto)

class Salir(CtrLogin, TemplateView):

	def get(self, request):
		logout(request)
		return HttpResponseRedirect('/logout/')


class Logout(TemplateView):
	template_name = 'logout.html'