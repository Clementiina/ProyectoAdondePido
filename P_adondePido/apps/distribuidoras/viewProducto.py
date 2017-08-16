import json
from django.http import HttpResponse, HttpResponseRedirect
from apps.categorias.models import SubCategoria, Marca, Marca_SubCategoria
from apps.distribuidoras.models import MarcaXSubcategoria_Distribuidora, Producto_Distribudora
from apps.productos.models import Producto
from django.views.generic import TemplateView
from django.shortcuts import render
from .formsProducto import Producto_DistribudoraForm, NuevoProductoForm
from django.views.generic import ListView, UpdateView, CreateView
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist


class  VistaProducto(TemplateView):

	template_name = 'productos.html'

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
		ctx['un_p_d'] = p_d[0]#.producto
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

		
class Crear_Producto(CreateView):
	model = Producto_Distribudora
	template_name = "crear_producto.html"
	form_class = Producto_DistribudoraForm

	def get(self, request):
		ctx = {}
		ctx["o"] = request.GET["o"]
		ctx["p_d"] = request.GET["p_d"]
		ctx["form"] = self.form_class
		return render(request, self.template_name, ctx)

	def post(self, request, *args, **kwargs):
		opc = int(request.GET['o'])
		p_d_nuevo = Producto_Distribudora()
		p_d = Producto_Distribudora.objects.get(id=request.GET["p_d"])
		if opc == 1:
			formP = self.form_class(request.POST)
			if formP.is_valid():
				p_d_nuevo.distribuidora_id = p_d.distribuidora.id
				p_d_nuevo.marcaXSubcategoriaDistribuidora_id = p_d.marcaXSubcategoriaDistribuidora.id
				p_d_nuevo.producto_id = p_d.producto.id
				p_d_nuevo.presentacion = formP.cleaned_data["presentacion"]
				p_d_nuevo.precio_unitario = formP.cleaned_data["precio_unitario"]
				p_d_nuevo.stock = formP.cleaned_data["stock"]
				p_d_nuevo.estado = formP.cleaned_data["estado"]
				try:
					p_d_nuevo.save()
					return HttpResponseRedirect('/distribuidoras/lista_productos?lalo='+str(p_d.producto.id)+"&landa="+str(p_d.distribuidora.id))
				except IntegrityError as e:
					return HttpResponseRedirect('/distribuidoras/lista_productos?lalo='+str(p_d.producto.id)+"&landa="+str(p_d.distribuidora.id))
			else:
				pass



class Crear_Producto_Nuevo(TemplateView):
	template_name = "crear_producto_nuevo.html"

	def get(self, request):
		context={}
		context["form"] = NuevoProductoForm()
		context["dist"] = request.GET["dist"]
		return render(request, self.template_name, context)

	def post(self, request):
		dist = request.GET["dist"]
		marca = (request.POST["marca"]).upper()
		nombre_producto = (request.POST["nombre_producto"]).upper()
		id = (request.POST["subCategoria"]).split("-")
		descripcion = request.POST["descripcion"]
		tipo_presentacion = int(request.POST["tipo_presentacion"])
		presentacion = int(request.POST["presentacion"])
		subCategoria = SubCategoria.objects.get(id=id[0])

		m_x_sc_d = MarcaXSubcategoria_Distribuidora()
		
		
		

		try:
			marca = Marca.objects.get(nombre__contains=marca)
		except ObjectDoesNotExist:
			marca = Marca()
			marca.nombre = (request.POST["marca"]).upper()
			marca.save()	

		m_sc_nueva = Marca_SubCategoria.objects.filter(subCategoria_id=subCategoria.id, marca_id=marca.id)

		if len(m_sc_nueva) == 0:
			m_sc = Marca_SubCategoria()
			m_sc.marca_id = marca.id
			m_sc.subCategoria_id =  subCategoria.id
			m_sc.save()
			b=True
		else:
			b=False

		m_x_sc_d.distribuidora_id = dist

		if b:
			m_x_sc_d.marcaSubCategoria_id = m_sc.id
			aux = m_sc.id
		else:
			m_x_sc_d.marcaSubCategoria_id = m_sc_nueva[0].id
			aux = m_sc_nueva[0].id

		try:
			m_x_sc_d.save()
			aux = m_x_sc_d
		except IntegrityError as e:
			m_x_sc_d_2 = MarcaXSubcategoria_Distribuidora.objects.get(marcaSubCategoria_id=aux)
			aux = m_x_sc_d_2

		try:
			p = Producto.objects.get(	nombre__contains=nombre_producto,
										marcaSubCategoria_id=aux.marcaSubCategoria.id,
										tipo_presentacion_id=tipo_presentacion)
		except ObjectDoesNotExist:
			p = Producto()
			p.nombre = nombre_producto
			p.descripcion = descripcion
			p.marcaSubCategoria_id = aux.marcaSubCategoria.id
			p.tipo_presentacion_id = request.POST["tipo_presentacion"]
			p.save()
		try:
			p_d = Producto_Distribudora.objects.get(	distribuidora_id=request.GET["dist"],
														marcaXSubcategoriaDistribuidora_id= aux.id,
														producto_id = p.id,
														presentacion_id = presentacion)
			return HttpResponseRedirect('/distribuidoras/lista_productos?lalo='+str(p_d.producto.id)+"&landa="+str(p_d.distribuidora.id))

		except ObjectDoesNotExist:
			p_d = Producto_Distribudora()
			p_d.distribuidora_id = request.GET["dist"]
			p_d.marcaXSubcategoriaDistribuidora_id = aux.id
			p_d.producto_id = p.id
			p_d.presentacion_id = request.POST["presentacion"]
			p_d.precio_unitario = float(request.POST["precio"])
			p_d.stock = request.POST["stock"]
			p_d.save()
			return HttpResponseRedirect('/distribuidoras/lista_productos?lalo='+str(p_d.producto.id)+"&landa="+str(p_d.distribuidora.id))
