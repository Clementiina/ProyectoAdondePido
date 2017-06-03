from django import forms 
 
class FormularioProductos(forms.Form): 
	marcaSubCategoria = forms.ForeignKey(Marca_SubCategoria)
	nombre = forms.CharField(max_length=50)
	descripcion = forms.CharField(widget=forms.Textarea)
	estado = forms.BooleanField(default=True)
 

