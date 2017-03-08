import datetime
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Solicitud
from django.contrib.auth import login

class VistaSolicitud(TemplateView):
    template_name = 'solicitud.html'

    def post(self, request):
        s = Solicitud()
        s.fecha = datetime.datetime.now()
        s.usuario = request.POST['unico']
        s.contraseña = request.POST['contraseña']
        s.email = request.POST['email']
        s.apellido = request.POST['apellido']
        s.nombre = request.POST['nombre']
        s.dni = request.POST['DNI']
        s.telefono = request.POST['telefono']
        s.celular = request.POST['celular']
        #s.id_localidad = 20254 #int(request.POST['localidad'])
        s.direccion = request.POST['direccion']
        s.estado = 'p' #Pendiente
        s.save()
        u = User()
        u.username = s.usuario
        u.set_password(s.contraseña)
        u.save()
        login(request, u) #auto login
        return HttpResponseRedirect('/')
