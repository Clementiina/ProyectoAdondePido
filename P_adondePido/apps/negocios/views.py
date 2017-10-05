# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView

from apps.negocios.models import Usuario_Negocio
from apps.distribuidoras.models import Negocio_Distribuidora
import random

class Vista_Negocio(TemplateView):
	template_name = 'negocio.html'

	def get (self, request, *args, **kwargs):
		ctx = {}
		aux = []
		css = ["grid-item","grid-item grid-item--height3",
				"grid-item grid-item--width3",
				"grid-item grid-item--width2 grid-item--height3",
				"grid-item grid-item--width2 grid-item--height2"]
		print (css)
		n_d = Negocio_Distribuidora.objects.all()
		j = 7
		for i in range(j):
			aux.append(n_d[0])
		for i in range(j+1):
			aux.append(n_d[1])
		a = []
		for i in aux:
			c = {}
			c["n_d"] = i
			c["css"] = css[random.randint(0, 3)] 
			print(c)
			a.append(c)

		#n_d = aux
		ctx["n_d"] = a
		return render(request, self.template_name, ctx) 

"""		
		indice = 0
		fin = int(len(n_d))
		f = int(fin)//4
		print(f)
		i = 0
		matriz = []
		while i<f:
			print("algo")
			c = 0
			fila = []
			while c<4:
				fila.append(n_d[indice])
				c += 1
				indice += 1
			i+=1
			matriz.append(fila)
			print(matriz)
			print("-----")

		c = 0
		fila = []
		while indice!=fin:
			fila.append(n_d[indice])
			c += 1
			indice += 1
		matriz.append(fila)
		ctx["matriz"] = matriz
		print(matriz)
"""		




