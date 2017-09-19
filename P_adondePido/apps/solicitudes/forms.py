# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
from .models import Solicitud 

class SolicitudNForm(forms.ModelForm):
	class Meta:
		model = Solicitud
		
		fields = [
			"usuario",
			"email",
			"nombre",
			"apellido",
			"dni",
			"telefono",
			"celular",
			"localidad",
			"n_nombre",
			"descripcion",
			"numero_contacto",
			"direccion"
		]
		
class SolicitudDForm(forms.ModelForm):
	class Meta:
		model = Solicitud
		
		fields = [
			"usuario",
			"email",
			"nombre",
			"apellido",
			"dni",
			"telefono",
			"celular",
			"localidad",
			"cuit",
			"n_nombre",
			"descripcion",
			"numero_contacto",
			"direccion"
		]