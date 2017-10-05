from django import forms
from apps.pedidos.models import Pedido, Detalle_Pedido

class PedidoForm(forms.ModelForm):

	class Meta:
		model = Pedido
		
		fields = [
			
			"fecha_envio",
			"fecha_recepcion",
			"estado_p"
		]

		exclude = [
			"socio",
			"estado"
		
		]

		labels = {

		"fecha_envio" : "Fecha de Envio",
		"fecha_recepcion" : "Fecha de Recepción",
		"estado_p" : "Estado"
		
		}

		widgets = {

			'fecha_envio':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_recepcion':forms.TextInput(attrs={'class':'form-control'}),
			'estado_p':forms.TextInput(attrs={'class':'form-control'}),

		}












class Detalle_PedidoForm(forms.ModelForm):

	class Meta:
		model = Detalle_Pedido
		fields = [
		
				"producto_distribuidora",
				"precio_unitario",
				"cantidad"

]

		labels = {
			"producto_distribuidora":"Producto",
			"precio_unitario":"Precio Unitario",
			"cantidad":"Cantidad"		
		}

		widgets = {
	
			"producto_distribuidora" : forms.TextInput(attrs={'class':'form-control'}),
			"precio_unitario":forms.NumberInput(attrs={"class":"form-control", "min":"0", "required":"True", "errors":"hide"}),
			"cantidad": forms.NumberInput(attrs={"class":"form-control", "min":"0","max":"500000", "required":"True"})


		}

		exclude = [
	
					"pedido",
			"estado"
	]


class TodoPedidoForm(forms.Form):

	


	producto_distribuidora = forms.ChoiceField(	label="Seleccione Un Producto",
								widget=forms.Select(attrs={"class":"form-control", "required":"True"}))

	cantidad = forms.IntegerField(	label="Ingrese La cantidad", 
									widget=forms.NumberInput(attrs={"class":"form-control", "min":"0","max":"500000", "required":"True"}))
	
	



