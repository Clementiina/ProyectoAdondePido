# -*- coding: utf-8 -*-

from django import forms
from .models import Ruta 

class RutaForm(forms.ModelForm):
	class Meta:
		model = Ruta
		
		fields = [
			"nombre",
			"recorrido",
			"dia",
			"estado"
		]