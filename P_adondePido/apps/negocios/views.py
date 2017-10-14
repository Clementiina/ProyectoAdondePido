# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.negocios.models import Usuario_Negocio
from apps.distribuidoras.models import Negocio_Distribuidora, Anuncio
import random

class Vista_Negocio(TemplateView):
	template_name = 'negocio.html'

	def get (self, request, *args, **kwargs):
		ctx = {}
		aux = []
		aux2 = []
		css = [	"grid-item",
				"grid-item grid-item--height2",
				"grid-item grid-item--height3",
				"grid-item grid-item--height4"]
		n_d = Negocio_Distribuidora.objects.filter(negocio_id=request.GET["dist"])
		for d in n_d:
			anuncio = Anuncio.objects.filter(distribuidora_id=d.distribuidora.id)
			for a in anuncio:
				c = {}
				c["anuncio"] = a
				aux2.append(c)
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
			a.append(c)
		ctx["n_d"] = a
		ctx["anuncio"] = aux2
		print("-----")
		print(ctx)
		return render(request, self.template_name, ctx)
