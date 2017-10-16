# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.negocios.models import Usuario_Negocio
from apps.distribuidoras.models import Negocio_Distribuidora, Anuncio
import random

class Vista_Negocio(TemplateView):
	template_name = 'negocio.html'

	def get (self, request):
		ctx = {}
		aux = []
		css = [	"grid-item",
				"grid-item grid-item--height2",
				"grid-item grid-item--height3",
				"grid-item grid-item--height4"]
		n_d = Negocio_Distribuidora.objects.filter(negocio_id=request.GET["dist"])
		for d in n_d:
			anuncio = Anuncio.objects.filter(distribuidora_id=d.distribuidora.id)
			for a in anuncio:
				c = {}
				c["id"] = a.id
				c["codigo"] = "?img="+str(a.id)+"&n_d="+str(d.id)
				c["imagen"] = a.imagen
				c["descripcion"] = a.descripcion
				aux.append(c)
		
		a = []
		for i in n_d:
			c = {}
			c["n_d"] = i
			c["css"] = css[random.randint(0, 3)]
			a.append(c)
		ctx["n_d"] = a
		ctx["anuncio"] = aux
		print("-----")
		print(ctx)
		return render(request, self.template_name, ctx)


