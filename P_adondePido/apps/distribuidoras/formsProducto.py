from django import forms 
from apps.distribuidoras.models import Producto_Distribudora
from apps.categorias.models import Categoria


class Producto_DistribudoraForm(forms.ModelForm):

    class Meta:
        model = Producto_Distribudora
        fields = ["presentacion", "precio_unitario", "stock", "estado"]
        
    def __init__(self, *args, **kwargs):
    	super(Producto_DistribudoraForm, self).__init__(*args, **kwargs)
    	for field in iter(self.fields):
    		if field != 'estado':
    			self.fields[field].widget.attrs.update({'class': 'form-control'})


class NuevoProductoForm(forms.Form):

	p = Categoria.objects.all()
	def get_categorias(object=None):
		lista = []
		l = []
		l.insert(0, "")
		l.insert(1,"----------")
		lista.append(tuple(l))
		for i in object:
			l.pop(1)
			l.pop(0)
			l.insert(0, i.id)
			l.insert(1,i.nombre)
			lista.append(tuple(l))		
		tupla = tuple(lista)
		return tupla
	
	marca = forms.CharField(label="Ingrese Nombre de la Marca", 
							widget=forms.TextInput(attrs={"class":"form-control", "required":"True"}))

	precio = forms.FloatField(	#required=True,
								label="Ingrese Precio Unitario", 
								widget=forms.NumberInput(attrs={"class":"form-control", "min":"0", "required":"True"}))

	stock = forms.IntegerField(	label="Ingrese Stock", 
								widget=forms.NumberInput(attrs={"class":"form-control", "min":"0","max":"100", "required":"True"}))

	categoria = forms.ChoiceField(	label="Seleccione la Categoria",
									required=True,
									choices = get_categorias(p),
									widget=forms.Select(attrs={"class":"form-control", "required":"True"}))


	subCategoria = forms.ChoiceField(	label="Seleccione la Subcategoria", 
										widget=forms.Select(attrs={"class":"form-control", "required":"True"}))

	
	nombre_producto = forms.CharField(	label="Ingrese el Nombre del Producto", 
										widget=forms.TextInput(attrs={"class":"form-control", "required":"True"}))

	descripcion = forms.CharField(	label="Ingrese Descripción", 
									widget=forms.Textarea(attrs={	"class":"form-control", "rows":"2", 
																 	"placeholder":"Ingrese Descripción del Producto",
																 	"required":"True"}))

	tipo_presentacion = forms.ChoiceField(	label="Seleccione la el tipo de Presentación", 
											widget=forms.Select(attrs={"class":"form-control", "required":"True"}))

	presentacion = forms.ChoiceField(	label="Seleccione la Presentación", 
										widget=forms.Select(attrs={"class":"form-control", "required":"True"}))
