from django import forms
from apps.productos.models import producto
class VentaProductoForm(forms.ModelForm):

	class Meta:
		model = producto
		fields = [
			'nombreProd',
			'costo',
			'disponible',
			'existencias', 	 
		]
		labels = {
			'nombreProd' : 'Nombre',
			'costo' : 'Costo',
			'disponible' : 'Disponible',  
			'existencias' : 'Existencias',
		}
		widgets = {
			'nombreProd':forms.TextInput(attrs = {'class':'form-control','id':'nombreProd'}),
			'costo':forms.TextInput(attrs = {'class':'form-control','id':'costo','disabled':'true'}),
			'disponible':forms.TextInput(attrs = {'class':'form-control','id':'disponible','disabled':'true'}),
			'existencias':forms.TextInput(attrs = {'class':'form-control','id':'existencias','disabled':'true'}),
		}