import json
from django.core import serializers
from django.shortcuts import render
from django.views.generic import TemplateView
from apps.categorias.models import Marca, SubCategoria
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from apps.productos.models import Tipo_Presentacion, Presentacion

class BuscaMarcaAjax(TemplateView):

	def post(self, request):
		marca = str(request.POST["buscar"])
		dat = {}
		try:
			marca = Marca.objects.get(nombre__contains=marca)
			dat["marca"] = marca.nombre+"-E"
		except ObjectDoesNotExist:
			dat["marca"] = marca+"-N"
		data=json.dumps(dat)
		return HttpResponse(data, content_type='application/json')

class SelecCategriaAjax(TemplateView):
	
	def get(self, request):
		categoria = request.GET["categoria"]
		subCategoria = SubCategoria.objects.filter(categoria_id=categoria)
		print(subCategoria[0].tipo_presentacion	)
		data = serializers.serialize('json', subCategoria,
                            fields=('id', 'nombre', 'tipo_presentacion'))
		return HttpResponse(data, content_type='application/json')

class SelecSubCategriaAjax(TemplateView):

	def get(self, request):
		ctx = {}
		lista=[]
		c = str(request.GET["subCategoria"])
		codigo = c.split("-")
		ctx["t_p_id"] = codigo[1]
		objeto = Tipo_Presentacion.objects.all()
		objeto2 = Presentacion.objects.filter(tipo_presentacion_id=codigo[1])
		for i in objeto:
			tp = {}
			tp["id"] = i.id
			tp["nombre"] = i.nombre
			lista.append(tp)
		ctx["tipo_presentacion"] = lista
		lista=[]
		for i in objeto2:
			tp = {}
			tp["id"] = i.id
			tp["capacidad"] = i.capacidad
			lista.append(tp)
		ctx["presentacion"] = lista
		data=json.dumps(ctx)
		print(data)
		return HttpResponse(data, content_type='application/json')


class SelecTipo_PresentacionAjax(TemplateView):
	def get(self, request):
		tipo_id = request.GET["tipo"]
		presentacion = Presentacion.objects.filter(tipo_presentacion_id=tipo_id)
		data = serializers.serialize('json', presentacion,
                            fields=('id', 'capacidad'))
		return HttpResponse(data, content_type='application/json')