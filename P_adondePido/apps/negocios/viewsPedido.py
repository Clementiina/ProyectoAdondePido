from django.shortcuts import render
from django.db import IntegrityError
from django.views.generic import TemplateView, CreateView,ListView, UpdateView
from apps.negocios.models import Usuario_Negocio
from apps.distribuidoras.models import Negocio_Distribuidora, MarcaXSubcategoria_Distribuidora, Producto_Distribudora
from apps.pedidos.models import Pedido, Detalle_Pedido
from django.http import HttpResponseRedirect
from django.db.models import Q
from datetime import datetime, timedelta



class Inicio_Pedido(TemplateView):

	template_name = 'inicio_pedido.html'

	def get (self, request, *args, **kwargs):
		print("LEO COGOTE")
		aux = request.GET["n_d"]
		if "$" in aux:
			nro_pedido="000"
			id = aux[:len(aux)-1]
			opc=True
		else:
			id = aux
			opc=False
		fin = datetime.today()
		inicio = fin + timedelta(days=-10)
		inicioBis = fin + timedelta(days=-3)
		n_d = Negocio_Distribuidora.objects.get(id=id)

		pedido = Pedido.objects.filter(Q(socio_id=id) & Q(fecha_creacion__range=(inicio,fin)) & Q(estado=True))
		pedido_no_enviado = pedido.filter(Q(estado_p__startswith="n") & Q(fecha_creacion__range=(inicioBis, fin)))
		pedido_enviado = pedido.exclude(estado_p__startswith="n").order_by("-fecha_creacion")

		if len(pedido_no_enviado)==0:
			nro_pedido="00"
			pedido_no_enviado=""
		else:
			pedido_no_enviado=pedido_no_enviado[0]
			nro_pedido=pedido_no_enviado.id

		ms_d = MarcaXSubcategoria_Distribuidora.objects.filter(distribuidora_id=n_d.distribuidora.id)

		ctx = {}
		ctx["socio"] = n_d
		ctx["ms_d"] = ms_d
		ctx["pedido_no_enviado"] = pedido_no_enviado
		ctx["pedido_enviado"] = pedido_enviado
		ctx["nro_pedido"] = nro_pedido
		ctx["opc"] = opc
		return render(request, self.template_name, ctx)



class Lista_Productos(ListView):
#	model = Producto_Distribudora
	template_name= "p_lista_productos.html"

	def get (self, request, *args, **kwargs):
		if request.GET["p"] == "000":
			fin = datetime.today()
			inicio= fin + timedelta(days=-3)
			pedido = Pedido.objects.filter(Q(socio_id=request.GET["n_d"])
				& Q(fecha_creacion__range=(inicio,fin))
				& Q(estado_p__startswith="n")).order_by("-fecha_creacion")
			nro = pedido[0].id
		else:
			nro = request.GET["p"]
		ctx = {}
		lista=[]
		j = 0
		p_d = Producto_Distribudora.objects.filter(marcaXSubcategoriaDistribuidora_id=request.GET["ms_d"]).order_by("precio_unitario")
		ctx["producto"] = p_d[0]
		for i in p_d:
			p = {}
			p["id"] = i.id
			p["producto"] = i.producto
			p["presentacion"] = i.presentacion
			p["precio_unitario"] = i.precio_unitario
			p["nameText"] = "form-"+str(j)+"-name"
			p["nameHidden"] = "form-"+str(j)+"-id"
			p["namePrecio"] =  "form-"+str(j)+"-precio"
			lista.append(p)
			j+=1
		ctx["p_d"] = lista
		ctx["msd"] = request.GET["ms_d"]
		ctx["n_d"] = request.GET["n_d"]
		ctx["nro_pedido"] = request.GET['p']
		ctx["nro"] = nro
		return render(request, self.template_name,ctx)

	def post(self, request, *args, **kwargs):
		socio = request.GET["n_d"]
		nro_pedido = request.GET["p"]
		k = 1
		j=-1
		if nro_pedido == "00":
			pedido = Pedido()
			pedido.socio_id = socio
			pedido.estado_p = "n"
			pedido.save()
			nro_pedido = pedido.id
		else:
			nro_pedido = request.POST["nro"]
		band = ((len(request.POST) - 2)//3)
		while True:
			j+=1
			if request.POST.get("form-"+str(j)+"-id","leo cogote")!="leo cogote":
				if request.POST.get("form-"+str(j)+"-name","") != "":
					band = True
					d_pedido = Detalle_Pedido()
					d_pedido.pedido_id = int(nro_pedido)
					d_pedido.producto_distribuidora_id = request.POST.get("form-"+str(j)+"-id","")
					d_pedido.precio_unitario = (float(str(request.POST.get("form-"+str(j)+"-precio","")).replace(",",".")))
					d_pedido.cantidad = request.POST.get("form-"+str(j)+"-name","")
					try:
						d_pedido.save()
					except IntegrityError:
						if k==band:
							return HttpResponseRedirect("/negocios/inicio_pedido/?n_d="+request.GET['n_d']+"$")
						else:
							k+=1
				else:
					pass
			else:
				break
		return HttpResponseRedirect("/negocios/inicio_pedido/?n_d="+request.GET['n_d'])
		

class Detalle_De_Pedido(TemplateView):

	template_name = "p_detalle_pedido.html"

	def get(self, request):
		nro_pedido = int(request.GET["p"])
		detalle_pedido = Detalle_Pedido.objects.filter(pedido_id=nro_pedido).order_by("producto_distribuidora")
		ctx={}
		ctx["pedido"] = detalle_pedido[0].pedido
		lista = []
		t = 0 
		for i in detalle_pedido:
			una_linea = {}
			una_linea["producto"] = i 
			una_linea["suma"] = i.cantidad * i.precio_unitario
			t = t + i.cantidad * i.precio_unitario
			lista.append(una_linea)
		ctx["detalle_pedido"] = lista
		ctx["total"] = t
		return render(request, self.template_name, ctx)


class Actualizar_Pedido(TemplateView):

	template_name="p_actualizar_pedido.html"

	def get(self, request):
		nro_pedido = int(request.GET["p"])
		lista=[]
		d_p = Detalle_Pedido.objects.filter(pedido_id=nro_pedido) #d_p: detalle pedido
		pedido = d_p[0].pedido
		j=0
		for i in d_p:
			p = {}
			p["id"] = i.id
			p["producto"] = i.producto_distribuidora
			p["cantidad"] = i.cantidad
			p["precio_unitario"] = i.precio_unitario
			p["nameNombre"] = "form-"+str(j)+"-name"
			p["nameId"] = "form-"+str(j)+"-id"
			p["nameCantidad"] =  "form-"+str(j)+"-cantidad"
			lista.append(p)
			j+=1
		ctx={}
		ctx["detalle_pedido"]= lista
		ctx["pedido"] = pedido
		return render(request, self.template_name, ctx)

	def post(self, request):
		j=-1
		while True:
			j+=1
			if request.POST.get("form-"+str(j)+"-id","leo cogote") != "leo cogote":
				id=request.POST.get("form-"+str(j)+"-id","leo cogote")
				d_p = Detalle_Pedido.objects.get(id=id)
				d_p.cantidad = request.POST.get("form-"+str(j)+"-cantidad","")
				d_p.save()
			else:
				break
		return HttpResponseRedirect("/negocios/inicio_pedido/?n_d="+request.POST['s'])


class Eliminar_Pedido(TemplateView):
	
	template_name = "eliminar_pedido.html"

	def get(self, request, *args,**kwargs):
		p = Pedido.objects.get(id=kwargs.get("pk"))
		p.estado = False
		p.save()
		return HttpResponseRedirect("/negocios/inicio_pedido/?n_d="+str(p.socio.id))
		
class Enviar_Pedido(TemplateView):
	
	template_name = "enviar_pedido.html"

	def get(self, request, *args,**kwargs):
		p = Pedido.objects.get(id=kwargs.get("pk"))
		p.estado_p = "e"
		p.save()
		return HttpResponseRedirect("/negocios/inicio_pedido/?n_d="+str(p.socio.id))
		
