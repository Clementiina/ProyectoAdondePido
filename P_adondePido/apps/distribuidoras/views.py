from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Distribuidora, Usuario_Distribuidora
from apps.negocios.models import Usuario_Negocio
from apps.solicitudes.models import Distribuidora, Distribuidora_Solicitud

class VistaDistribuidora(TemplateView):
	template_name = 'distribuidora.html'

	def get(self, request):
		contexto = dict()
		contexto['distribuidoras'] = Usuario_Distribuidora.objects.filter(usuario = self.request.user.id)
		contexto['negocios'] = Usuario_Negocio.objects.filter(usuario = self.request.user.id)
		contexto['dist'] = Distribuidora.objects.get(id=request.GET['dist'])
		contexto['s_cant'] = len(Distribuidora_Solicitud.objects.filter(distribuidora=request.GET['dist']))
		return render(request, 'distribuidora.html', contexto)

from . import viewAnuncio, viewRuta

