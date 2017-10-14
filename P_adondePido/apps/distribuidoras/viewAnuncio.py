from .models import Anuncio
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.solicitudes.models import Distribuidora, Distribuidora_Solicitud

class FormatoFecha():

	def __init__(self):
		super(FormatoFecha, self).__init__()

	def trasforma(self, a=None):
		vec = a.split("/")
		fecha = str(vec[2]) + '-' + str(vec[1]) + '-' + str(vec[0])
		return fecha

class CrearAnuncio(TemplateView):
	template_name = "crear_anuncio.html"

	def get(self, request):
		uname = request.user.username
		dist = (request.GET["dist"])
		distribuidora = Distribuidora.objects.get(id=dist)
		return render(request, self.template_name, {'dist': distribuidora})

	def post(self, request):
		a = FormatoFecha()
		distribuidora = request.POST['distribuidora']
		u = Anuncio()
		u.distribuidora_id = distribuidora
		if request.FILES:
			u.imagen = request.FILES['img']
		u.titulo = request.POST['titulo']
		u.descripcion = request.POST['descripcion']
		u.fecha_creacion = datetime.datetime.now()
		u.fecha_inicio = a.trasforma(request.POST['fecha_inicio'])
		u.fecha_fin = a.trasforma(request.POST['fecha_fin'])
		u.estado = True
		u.save()
		return HttpResponseRedirect("/distribuidoras/anuncios/?dist="+request.GET['dist']+"&pag=1")

class ActualizarAnuncio(TemplateView):
	template_name = "actualizar_anuncio.html"

	def get(self, request):
		#contexto = {}
		#contexto['dist'] = Distribuidora.objects.get(id=request.GET['dist'])
		#contexto['s_cant'] = len(Distribuidora_Solicitud.objects.filter(distribuidora=request.GET['dist'],solicitud__es_distribuidora=False))
		anuncio = Anuncio.objects.get(id=request.GET["anuncio"])
		ctx = {"dist":request.GET["dist"],"anuncio":anuncio}
		print(ctx)
		return render(request,self.template_name, ctx)

	def post(self, request, *args, **kwargs):
		a = FormatoFecha()
		anuncio = Anuncio.objects.get(id=request.POST['id'])
		anuncio.titulo = request.POST["titulo"]
		anuncio.fecha_inicio = a.trasforma(request.POST['fecha_inicio'])
		anuncio.fecha_fin = a.trasforma(request.POST["fecha_fin"])
		anuncio.descripcion = request.POST["descripcion"]
		anuncio.estado = True
		if request.FILES:
			anuncio.imagen = request.FILES['img']
		anuncio.save()
		return HttpResponseRedirect("/distribuidoras/anuncios/?dist="+request.GET['dist']+"&pag=1")

class EliminarAnuncio(TemplateView):
	template_name = "eliminar_anuncio.html"
	def get(self, request):
		contexto = {}
		contexto['dist'] = Distribuidora.objects.get(id=request.GET['dist'])
		contexto['s_cant'] = len(Distribuidora_Solicitud.objects.filter(distribuidora=request.GET['dist'],solicitud__es_distribuidora=False))
		anuncio = Anuncio.objects.get(id=request.GET["anuncio"])
		ctx = {"dist":request.GET["dist"],"anuncio":anuncio}
		return render(request,self.template_name, ctx)

	def post(self, request, *args, **kwargs):
		anuncio = Anuncio.objects.get(id=request.POST['id'])
		anuncio.estado = False
		anuncio.save()
		return HttpResponseRedirect("/distribuidoras/anuncios/?dist="+request.GET['dist']+"&pag=1")

class VistaAnuncio(ListView):
	model = Anuncio
	template_name = 'anuncios.html'
	context_object_name = "anuncios"
	def get(self, request):
		print(request.GET)
		uname = request.user.username
		dist = request.GET['dist']
		print(dist)
		listado = Anuncio.objects.filter(distribuidora__id=dist, estado=True)
		print(listado)
		paginador = Paginator(listado, 5)
		pagina = request.GET['pag']
		try:
			anuncios = paginador.page(pagina)
		except PageNotAnInteger:
			anuncios = paginador.page(1)
		except EmptyPage:
			anuncios = paginador.page(paginador.num_pages)

		contexto = {}
		contexto['anuncios'] = anuncios
		contexto['dist'] = Distribuidora.objects.get(id=request.GET['dist'])
		contexto['s_cant'] = len(Distribuidora_Solicitud.objects.filter(distribuidora=request.GET['dist'],solicitud__es_distribuidora=False))
		return render(request, 'anuncios.html', contexto)
