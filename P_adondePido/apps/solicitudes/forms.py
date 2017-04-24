# -*- coding: utf-8 -*-

from django import forms
from .models import Solicitud 

class SolicitudForm(forms.ModelForm):
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