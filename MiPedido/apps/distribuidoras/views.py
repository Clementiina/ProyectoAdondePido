from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from apps.distribuidoras.models import Distribuidora, Usuario_Distribuidora 
from apps.distribuidoras.models import Anuncio
import datetime

class FormatoFecha():

    def __init__(self):
        super(FormatoFecha, self).__init__()

    def trasforma(self, a=None):
        vec = a.split("-")
        fecha = str(vec[2]) + '-' + str(vec[1]) + '-' + str(vec[0])
        return fecha

class CrearAnuncio(TemplateView):

    template_name = "crear_anuncio.html"

    def post(self, request):
        a = FormatoFecha()
        p = (Usuario_Distribuidora.objects.get(id_usuario=request.user.id, estado=True))
        u = Anuncio()
        u.id_distribuidora_id = p.id_distribuidora.id
        u.imagen = request.FILES['img']
        u.titulo = request.POST['titulo']
        u.descripcion = request.POST['descripcion']
        u.fecha_creacion = datetime.datetime.now()
        u.fecha_inicio = a.trasforma(request.POST['fecha_inicio'])
        u.fecha_fin = a.trasforma(request.POST['fecha_fin'])
        u.estado = "l"  # vigente, listo, finalizado
        u.save()
        return HttpResponseRedirect("/distribuidora/crear_anuncio")

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