from django.contrib.auth.models import User
from django import forms

class UserForm(forms.Form):
	usuario = forms.CharField(label="Usuario" ,widget=forms.TextInput(attrs={"class":"form-control", "required":"True"}))
	clave = forms.CharField(label="Contraseña" ,widget=forms.PasswordInput(attrs={"class":"form-control", "required":"True"}))
