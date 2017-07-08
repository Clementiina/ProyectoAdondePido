from django import forms 
from apps.distribuidoras.models import Producto_Distribudora
 

class Producto_DistribudoraForm(forms.ModelForm):

    class Meta:
        model = Producto_Distribudora
        fields = ["presentacion", "precio_unitario", "stock", "estado"]
        
    def __init__(self, *args, **kwargs):
    	super(Producto_DistribudoraForm, self).__init__(*args, **kwargs)
    	for field in iter(self.fields):
    		print(field)
    		if field != 'estado':
    			self.fields[field].widget.attrs.update({'class': 'form-control'})
