import json
from django.http import HttpResponse, HttpResponseRedirect
from apps.categorias.models import SubCategoria
from apps.distribuidoras.models import MarcaXSubcategoria_Distribuidora, Producto_Distribudora
from django.views.generic import TemplateView
from django.shortcuts import render
from .formsProducto import Producto_DistribudoraForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, UpdateView


class VistaProducto(TemplateView):

	template_name = 'producto.html'

	def get(self, request):
		context = {}
		id = int(request.GET["dist"])
		p = MarcaXSubcategoria_Distribuidora.objects.filter(distribuidora__id=id)
		s = set()
		for i in p:
			s.add(i.marcaSubCategoria.subCategoria.categoria)
		context["dist"] = id
		context["categorias"] = list(s)
		return render(request, self.template_name, context)


class Select_SubCategoria_Ajax(TemplateView):

	def get(self, request):
		codigo = str(request.GET["categoria_dist"]).split("&")
		categoria = codigo[0]
		dist = codigo[1]
		s_c = SubCategoria.objects.filter(categoria_id=categoria)

		lista = []
		for i in s_c:
			ctx = {}
			codigo = str(i.id) + "&" + dist
			ctx["id"] = codigo
			ctx["nombre"] = i.nombre
			lista.append(ctx)
		data = json.dumps(lista)
		return HttpResponse(data, content_type='application/json')

class Select_Marca_SubCategoria_Ajax(TemplateView):

	def get(self, request):
		codigo = str(request.GET["subCategorias_dist"]).split("&")
		subCategoria = codigo[0]
		dist = codigo[1]
		lista = []
		m_x_sc = MarcaXSubcategoria_Distribuidora.objects.filter( distribuidora__id=dist,
																  marcaSubCategoria__subCategoria__id=subCategoria
																)
		for i in m_x_sc:
			codigo = str(i.id) + "&" + dist
			ctx = {}
			ctx["id"] = codigo
			ctx["nombre"] = i.marcaSubCategoria.marca.nombre
			lista.append(ctx)
		data = json.dumps(lista)
		return HttpResponse(data, content_type='application/json')


class Select_Marca_SubCategoria_Dist_Ajax(TemplateView):
	
	def get(self, request):
		codigo = str(request.GET["m_x_sc_d"]).split("&")
		m_x_sc_d_id = codigo[0]
		dist = codigo[1]
		p_d = Producto_Distribudora.objects.filter(distribuidora__id=dist,
													marcaXSubcategoriaDistribuidora_id=m_x_sc_d_id)
		s = set()
		for i in p_d:
			s.add(i.producto)
		lista = list(s)
		lista2 = []
		for i in lista:
			codigo = str(i.id) + "&landa=" + dist
			ctx = {}
			ctx["id"] = codigo
			ctx["nombre"] = i.nombre
			lista2.append(ctx)
		data = json.dumps(lista2)
		return HttpResponse(data, content_type='application/json')

class Lista_Productos(ListView):
	model = Producto_Distribudora
	template_name = "lista_productos.html"

	def get(self, request, *args, **kwargs):
		ctx = {}
		id = request.GET["lalo"]
		p_d = Producto_Distribudora.objects.filter(producto_id=id)
		ctx['p_d'] = p_d
		ctx['producto'] = p_d[0].producto
		return render(request, self.template_name, ctx)


class Actualizar_Producto(UpdateView):
	model = Producto_Distribudora
	template_name = 'actualizar_producto.html'
	form_class = Producto_DistribudoraForm

	def post(self, request, *args, **kwargs):
		p = Producto_Distribudora.objects.get(id=kwargs['pk'])
		formP = self.form_class(request.POST, instance=p)
		if formP.is_valid():
			formP.save()
			return HttpResponseRedirect('/distribuidoras/lista_productos?lalo='+str(p.producto.id)+"&landa="+str(p.distribuidora.id) )
		else:
			return HttpResponseRedirect('/distribuidoras/lista_productos?lalo='+str(p.producto.id)+"&landa="+str(p.distribuidora.id))
		
