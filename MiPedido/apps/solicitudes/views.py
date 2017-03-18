import datetime
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Solicitud, Distribuidora_Solicitud
from apps.distribuidoras.models import Distribuidora, Negocio_Distribuidora
from django.contrib.auth import login
from apps.negocios.models import Negocio, Usuario_Negocio
from apps.personas.models import Persona
import hashlib, random

class VistaSolicitud(TemplateView):
    template_name = 'solicitud.html'
    
    def get(self, request):
        contexto={}
        contexto['distribuidoras'] = Distribuidora.objects.all()        
        return render(request, self.template_name, contexto)

    def validar(user):
        return HttpResponseRedirect('/sin_activar/')
    
    def post(self, request):
        try:
                nu = User.objects.get(username = request.POST['user'])
        except User.DoesNotExist:
                nu = None               
        if nu is None :
            u = User()
            u.username = request.POST['user']
            u.set_password(request.POST['contraseña'])
            u.email = request.POST['email']
            u.last_name = request.POST['apellido']
            u.first_name = request.POST['nombre']   
            u.save()
            login(request, u) #auto login
            
            s = Solicitud()
            s.fecha = datetime.datetime.now()
            s.usuario_id = u.id
            s.code = (str(hashlib.sha256(str(random.random()).encode('utf-8')).hexdigest())[:20])
            s.dni = request.POST['DNI']
            s.telefono = request.POST['telefono']
            s.celular = request.POST['celular']
            s.id_localidad = 3935 #int(request.POST['localidad']) #ya esta por defecto
            s.nombre = request.POST['n_nombre']
            s.descripcion = request.POST['n_descripcion']
            s.numero_contacto = request.POST['n_contacto']
            s.direccion = request.POST['n_direccion']
            s.estado = 'p' #Pendiente
            s.save()        
            distribuidoras = request.POST.getlist('lista')        
            for dist in distribuidoras:
                ds = Distribuidora_Solicitud()
                ds.solicitud_id = s.id
                ds.distribuidora_id = dist
                ds.save()
                return HttpResponseRedirect('/sin_activar/')
        contexto = {}
        contexto['error'] = 'El usuario ya existe'
        contexto['user'] = request.POST['user']
        contexto['email'] = request.POST['email']
        contexto['apellido'] = request.POST['apellido']
        contexto['nombre'] = request.POST['nombre']
        contexto['DNI'] = request.POST['DNI']
        contexto['telefono'] = request.POST['telefono']
        contexto['celular'] = request.POST['celular']
        contexto['localidad'] = request.POST['localidad']
        contexto['n_nombre'] = request.POST['n_nombre']
        contexto['n_descripcion'] = request.POST['n_descripcion']
        contexto['n_contacto'] = request.POST['n_contacto']
        contexto['n_direccion'] = request.POST['n_direccion']       
        contexto['distribuidoras'] = Distribuidora.objects.all()
        return render(request, self.template_name, contexto)

class VistaSolicitudes(TemplateView):
    template_name = 'solicitudes.html'
    
    def get(self, request):
        contexto={}
        solicitudes = Distribuidora_Solicitud.objects.filter(distribuidora_id=request.GET['dist'])
        contexto['dist'] = request.GET['dist']
        contexto['solicitudes'] = solicitudes
        contexto['s_cant'] = len(solicitudes)
        return render(request, self.template_name, contexto)

class VistaActivar(TemplateView):
    template_name = 'activar.html'
    
    def get(self, request):
        contexto={}
        s = Solicitud.objects.get(usuario_id=request.GET['user'] )
        contexto['dist'] = request.GET['dist']
        contexto['solicitud'] = s
        return render(request, self.template_name, contexto)
        
    def post(self, request):
        s = Solicitud.objects.get(usuario_id=request.GET['user'] )
        if (request.POST['code'] == s.code ):
            s.estado = 'a'
            s.save()
            p = Persona()
            p.usuario_id = request.GET['user']
            p.dni = s.dni
            p.telefono = s.telefono
            p.celular = s.celular
            p.localidad_id = s.localidad_id
            p.direccion = s.direccion
            p.estado = True
            p.save()
            n = Negocio()
            n.nombre = s.nombre
            n.descripcion = s.descripcion
            n.numero_contacto = s.numero_contacto
            n.localidad_id = s.localidad_id
            n.direccion = s.direccion
            n.persona_cargo_id = p.id
            n.save()
            u = Usuario_Negocio()
            u.permiso_id = 1 # PERMISO DE ADMINISTRADOR
            u.negocio_id = n.id
            u.usuario_id = request.GET['user']
            u.estado = True
            u.save()
            return HttpResponseRedirect('/solicitudes/?dist='+request.GET['dist'])
        contexto = {}
        contexto['error'] =  'Codigo incorrecto'
        contexto['dist'] = request.GET['dist']
        contexto['solicitud'] = s
        contexto['code'] = request.POST['code']
        return render(request, self.template_name, contexto)
        
class VistaAsociar(TemplateView):
    template_name = 'solicitudes.html'
    
    def get(self, request):
        n = Negocio.objects.get(persona_cargo_id__usuario_id=request.GET['user'] )
        socio = Negocio_Distribuidora()        
        socio.distribuidora_id = request.GET['dist']
        socio.negocio_id = n.id
        socio.save()        
        s = Distribuidora_Solicitud.objects.get(id = request.GET['s_id'])
        s.delete()
        return HttpResponseRedirect('/solicitudes/?dist='+request.GET['dist'])

class VistaIgnorar(TemplateView):
    template_name = 'solicitudes.html'
    
    def get(self, request):
        s = Distribuidora_Solicitud.objects.get(id = request.GET['s_id'])
        s.delete()
        return HttpResponseRedirect('/solicitudes/?dist='+request.GET['dist'])
