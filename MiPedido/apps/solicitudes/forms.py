# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from .models import Solicitud 


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		
		fields = [
			"username",
			"password",
			"email",
			"last_name",
			"first_name"
		]

class SolicitudForm(forms.ModelForm):
	class Meta:
		model = Solicitud
		
		fields = [
			"dni",
			"telefono",
			"celular",
			"localidad",
			"nombre",
			"descripcion",
			"numero_contacto",
			"direccion"
		]