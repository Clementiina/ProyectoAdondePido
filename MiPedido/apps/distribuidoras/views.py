import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from .models import Distribuidora, Usuario_Distribuidora, Anuncio, Ruta , DiasType
from apps.negocios.models import Usuario_Negocio
from apps.solicitudes.models import Distribuidora_Solicitud

class VistaDistribuidora(TemplateView):
	template_name = 'distribuidora.html'

	def get(self, request):
		contexto = dict()
		contexto['distribuidoras'] = Usuario_Distribuidora.objects.filter(usuario = self.request.user.id)
		contexto['negocios'] = Usuario_Negocio.objects.filter(usuario = self.request.user.id)
		contexto['dist'] = Distribuidora.objects.get(id=request.GET['dist'])
		contexto['s_cant'] = len(Distribuidora_Solicitud.objects.filter(distribuidora=request.GET['dist']))
		return render(request, 'distribuidora.html', contexto)

class FormatoFecha():

	def __init__(self):
		super(FormatoFecha, self).__init__()

<<<<<<< HEAD
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
        u.id_distribuidora_id = distribuidora
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
        contexto = {}
        contexto["dist"] = request.GET["dist"]
        anuncio = Anuncio.objects.get(id=request.GET["anuncio"])
        ctx = {"dist":request.GET["dist"],"anuncio":anuncio}
        print (ctx)
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
        contexto["dist"] = request.GET["dist"]
        anuncio = Anuncio.objects.get(id=request.GET["anuncio"])
        ctx = {"dist":request.GET["dist"],"anuncio":anuncio}
        print (ctx)
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
        uname = request.user.username
        dist = request.GET['dist']
        print(dist)
        print(uname)
        listado = Anuncio.objects.filter(id_distribuidora__persona_cargo__username=uname, id_distribuidora__id=dist, estado=True)
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
        contexto['dist'] = dist
        return render(request, 'anuncios.html', contexto)


class CrearRuta(TemplateView):
    template_name = 'adm_ruta.html'
    def get(self, request ):
        contexto = {}
        contexto['dist'] = request.GET['dist']
        contexto['DiasType'] = DiasType
        return render(request, 'adm_ruta.html', contexto)

    def post(self, request):
        r = Ruta()
        r.id_distribuidora_id = request.GET['dist']
        r.nombre = request.POST['nombre']
        r.recorrido = request.POST['recorrido']
        r.dia = request.POST['dia']
        r.estado = True  # activa
        r.save()
        return HttpResponseRedirect('/distribuidoras/rutas?dist='+request.GET['dist'] )

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
        contexto['rutas'] = Ruta.objects.filter(id_distribuidora__id=request.GET['dist'])
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
        contexto['rutas'] = Ruta.objects.filter(id_distribuidora__id=request.GET['dist'])
        return HttpResponseRedirect('/distribuidoras/rutas/?dist='+request.GET['dist'])


class ActualizarRuta(TemplateView):
    template_name = 'adm_ruta.html'
    def get(self, request ):
        contexto = {}
        contexto['dist'] = request.GET['dist']
        contexto['ruta'] = Ruta.objects.get(id=request.GET['ruta'])
        contexto['DiasType'] = DiasType
        return render(request, 'adm_ruta.html', contexto)

    def post(self, request):
        r = Ruta.objects.get(id=request.GET['ruta'] )
        r.id_distribuidora_id = request.GET['dist']
        r.nombre = request.POST['nombre']
        r.recorrido = request.POST['recorrido']
        r.dia = request.POST['dia']
        r.estado = request.POST['estado']
        r.save()
        return HttpResponseRedirect('/distribuidoras/rutas?dist='+request.GET['dist'])
=======
	def trasforma(self, a=None):
		vec = a.split("-")
		fecha = str(vec[2]) + '-' + str(vec[1]) + '-' + str(vec[0])
		return fecha

class DetalleAnuncio(DetailView):
	model = Anuncio
	context_object_name = 'anuncio'
	template_name = "detalle_anuncio.html"

	def get_context_data(self, **kwargs):
		context = super(DetalleAnuncio, self).get_context_data(**kwargs)
		return context


class CrearAnuncio(TemplateView):
	template_name = "crear_anuncio.html"

	def post(self, request):
		a = FormatoFecha()
		p = (Usuario_Distribuidora.objects.get(
												id_usuario=request.user.id,
												estado=True)
											   )
		u = Anuncio()
		u.id_distribuidora_id = p.id_distribuidora.id
		u.imagen = request.FILES['img']
		u.titulo = request.POST['titulo']
		u.descripcion = request.POST['descripcion']
		u.fecha_creacion = datetime.datetime.now()
		u.fecha_inicio = a.trasforma(request.POST['fecha_inicio'])
		u.fecha_fin = a.trasforma(request.POST['fecha_fin'])
		u.estado = "l"
		u.save()
		return HttpResponseRedirect("/distribuidora/listar_anuncios")

class VistaAnuncio(ListView):
	model = Anuncio
	template_name = 'anuncios.html'
	context_object_name = "anuncios"
	def get(self, request):
		uname = request.user.username
		dist = request.GET['dist']
		listado = Anuncio.objects.filter(id_distribuidora__id=dist)
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
		contexto['dist'] = dist
		return render(request, 'anuncios.html', contexto)


class CrearRuta(TemplateView):
	template_name = 'adm_ruta.html'
	def get(self, request ):
		contexto = {}
		contexto['dist'] = request.GET['dist']
		contexto['DiasType'] = DiasType
		return render(request, 'adm_ruta.html', contexto)

	def post(self, request):
		r = Ruta()
		r.id_distribuidora_id = request.GET['dist']
		r.nombre = request.POST['nombre']
		r.recorrido = request.POST['recorrido']
		r.dia = request.POST['dia']
		r.estado = True  # activa
		r.save()
		return HttpResponseRedirect('/distribuidoras/rutas?dist='+request.GET['dist'] )

class DetalleRuta(DetailView):
	model = Ruta
	context_object_name = 'ruta'
	template_name = "detalle_ruta.html"
	def get(self, request):
		contexto = {}
		contexto['dist'] = request.GET['dist']
		contexto['ruta'] = Ruta.objects.get(id=request.GET['ruta'] )
		return render(request, 'detalle_ruta.html', contexto)

class VistaRuta(ListView):
	model = Ruta
	template_name = 'rutas.html'
	context_object_name = 'rutas'
	def get(self, request):
		contexto = {}
		contexto['dist'] = request.GET['dist']
		contexto['rutas'] = Ruta.objects.filter(id_distribuidora__id=request.GET['dist'])
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
		return HttpResponseRedirect('/distribuidoras/rutas/?dist='+request.GET['dist'])


class ActualizarRuta(TemplateView):
	template_name = 'adm_ruta.html'
	def get(self, request ):
		contexto = {}
		contexto['dist'] = request.GET['dist']
		contexto['ruta'] = Ruta.objects.get(id=request.GET['ruta'])
		contexto['DiasType'] = DiasType
		return render(request, 'adm_ruta.html', contexto)

	def post(self, request):
		r = Ruta.objects.get(id=request.GET['ruta'] )
		r.id_distribuidora_id = request.GET['dist']
		r.nombre = request.POST['nombre']
		r.recorrido = request.POST['recorrido']
		r.dia = request.POST['dia']
		r.estado = request.POST['estado']
		r.save()
		return HttpResponseRedirect('/distribuidoras/rutas?dist='+request.GET['dist'])

>>>>>>> origin/master
