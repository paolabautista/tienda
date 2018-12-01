from django import forms
from apps.productos.models import categoria

class CatForm(forms.ModelForm): 
	class Meta:
		model = categoria
		fields = [
			#Aqui van los nombres de las variables de nuestra bd
			'nombreC',
		]
		labels = {
			
			'nombreC' : 'Nombre de la Categoría',
		}

		widgets = {
			'nombreC': forms.TextInput(attrs={'class' : 'form-control'}),
		}