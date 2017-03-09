import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView
from django.http import HttpResponseRedirect
from .models import Distribuidora, Usuario_Distribuidora, Anuncio, EstadoType

class VistaDistribuidora(TemplateView):
    template_name = 'distribuidora.html'

    def get(self, request):
        uname = request.user.username
        dist = request.GET['dist']
        distribuidora = Distribuidora.objects.get(persona_cargo__username=uname, id=dist)
        return render(request, 'distribuidora.html', {'dist': distribuidora})

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
        u.id_distribuidora_id = distribuidora
        if request.FILES:
            u.imagen = request.FILES['img']
        u.titulo = request.POST['titulo']
        u.descripcion = request.POST['descripcion']
        u.fecha_creacion = datetime.datetime.now()
        u.fecha_inicio = a.trasforma(request.POST['fecha_inicio'])
        u.fecha_fin = a.trasforma(request.POST['fecha_fin'])
        u.estado = "Listo"
        u.save()
        return HttpResponseRedirect("/distribuidoras/anuncios/?dist="+request.GET['dist']+"&pag=1")

class ActualizarAnuncio(TemplateView):
    template_name = "actualizar_anuncio.html"

    def get(self, request):
        contexto = {}
        contexto["dist"] = request.GET["dist"]
        anuncio = Anuncio.objects.get(id=request.GET["anuncio"])
        print (anuncio.get_estado_display())
        print (contexto)
        contexto["estado"] = EstadoType
        ctx = {"dist":request.GET["dist"],"anuncio":anuncio, "estado":EstadoType }
        print (ctx)
        return render(request,self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        if request.GET['anuncio'] == request.POST['id']:  # Una validacion, de seguridad,por si acaso alguien el valor de un metodo
            a = FormatoFecha()
            anuncio = Anuncio.objects.get(id=request.POST['id'])
            anuncio.titulo = request.POST["titulo"]
            anuncio.fecha_inicio = a.trasforma(request.POST['fecha_inicio'])
            anuncio.fecha_fin = a.trasforma(request.POST["fecha_fin"])
            anuncio.descripcion = request.POST["descripcion"]
            anuncio.estado = request.POST["estado"]
            if request.FILES:
                anuncio.imagen = request.FILES['img']
            anuncio.save()
            return HttpResponseRedirect("/distribuidoras/anuncios/?dist="+request.GET['dist']+"&pag=1")
        else:
            print ('ERROR DE SEGURIDAD')


class VistaAnuncio(ListView):
    model = Anuncio
    template_name = 'anuncios.html'
    context_object_name = "anuncios"

    def get(self, request):
        uname = request.user.username
        dist = request.GET['dist']
        listado = Anuncio.objects.filter(id_distribuidora__persona_cargo__username=uname, id_distribuidora__id=dist)
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

    template_name = "crear_ruta.html"

    def post(self, request):
        p = (Usuario_Distribuidora.objects.get(id_usuario=request.user.id, estado=True))
        r = Ruta()
        r.id_distribuidora_id = p.id_distribuidora.id
        r.nombre = request.POST['nombre']
        r.recorrido = request.POST['recorrido']
        r.dia = request.POST['dia']
        r.estado = True  # activa
        r.save()
        return HttpResponseRedirect("/distribuidora/crear_ruta")
