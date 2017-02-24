import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from .models import Distribuidora, Usuario_Distribuidora, Anuncio

class VistaDistribuidora(TemplateView):
    template_name = 'distribuidora.html'

    def get_context_data(self, **kwargs):
        contexto = super(VistaDistribuidora, self).get_context_data(**kwargs)
        contexto['distribuidora'] = Distribuidora.objects.get(id=kwargs['pk'])
        return contexto

class FormatoFecha():

    def __init__(self):
        super(FormatoFecha, self).__init__()

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
        listado = Anuncio.objects.all()
        paginador = Paginator(listado, 5) # 5 problemas x pagina
        pagina = request.GET.get('pag')
        try:
            anuncios = paginador.page(pagina)
        except PageNotAnInteger:
            anuncios = paginador.page(1)
        except EmptyPage:
            anuncios = paginador.page(paginador.num_pages)

        contexto = {'anuncios', anuncios}
        return render(request, "anuncios.html", contexto)


