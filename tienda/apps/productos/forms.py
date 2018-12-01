from django import forms
from apps.productos.models import producto

class ProdForm(forms.ModelForm):
	class Meta:
		model = producto
		fields = [
			#Aqui van los nombres de las variables de nuestra bd
			'nombreProd',
			'descripcion',
			'costo',
			'disponible',
			'categoria',
			'existencias',
		]
		labels = {
			'nombreProd': 'Nombre del producto',
			'descripcion': 'Descripción del producto',
			'costo': 'Costo',
			'disponible' : 'Disponibilidad',
			'categoria' : 'Categoría',
			'existencias': 'Productos en existencia'

		}

		widgets = {
			'nombreProd': forms.TextInput(attrs={'class' : 'form-control'}),
			'descripcion': forms.TextInput(attrs={'class' : 'form-control'}),
			'costo': forms.TextInput(attrs={'class' : 'form-control'}),
			'disponible': forms.TextInput(attrs={'class' : 'form-control'}),
			'categoria': forms.TextInput(attrs={'class' : 'form-control'}),
			'existencias' : forms.TextInput(attrs={'class' : 'form-control'}),
		}
