from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

class CtrLogin(object):
	@classmethod
	def as_view(cls, **initkwargs):
		view = super(CtrLogin, cls).as_view(**initkwargs)
		return login_required(view, login_url="/login/")

class Index(CtrLogin, TemplateView):
	template_name = 'index.html'


class Login(TemplateView):
	template_name = 'login.html'

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/')
		return HttpResponseRedirect('/login/')

class Salir(CtrLogin, TemplateView):

	def get(self, request):
		logout(request)
		return HttpResponseRedirect('/logout/')


class Logout(TemplateView):
	template_name = 'logout.html'