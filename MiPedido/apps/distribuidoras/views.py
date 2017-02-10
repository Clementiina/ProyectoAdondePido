import datetime
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from apps.distribuidoras.models import Distribuidora, Usuario_Distribuidora
from apps.distribuidoras.models import Anuncio



class FormatoFecha():

    def __init__(self):
        super(FormatoFecha, self).__init__()

    def trasforma(self, a=None):
        vec = a.split("-")
        fecha = str(vec[2]) + '-' + str(vec[1]) + '-' + str(vec[0])
        return fecha


class ListaAnuncios(ListView):
    template_name = "listar_anuncios.html"
    queryset = Anuncio.objects.all().order_by('-fecha_creacion')
    context_object_name = 'lista_de_anuncios'


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

