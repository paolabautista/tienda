from django.shortcuts import render, redirect #aqui importamos redirect
from django.http import HttpResponse
# vamos a importar las listas
from django.views.generic import ListView
from apps.productos.models import producto, categoria
from apps.productos.forms import ProdForm
from apps.productos.forms1 import CatForm
from apps.productos.forms2 import VentaProductoForm

def index(request):
	return HttpResponse("Hola")


def infProd(request):
	contexto = {
		'productos':producto.objects.all()
	}
	return render(request, 'tablas/productos.html', contexto)

def infCat(request):
	contexto = {
		'productos':categoria.objects.all()
	}
	return render(request, 'tablas/categorias.html', contexto)
def ventas(request):
	contexto = {
		'productos':producto.objects.all()
	}
	return render(request, 'tablas/ventas.html', contexto)

def nuevoRegistro(request):
	if request.method == 'POST':
		form = ProdForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect ('productos:listaProductos')
	else:
	#Esto es para generar un nuevo registro
		form = ProdForm()
	return render(request, 'tablas/ProductoFormulario.html', {'form' :form})


def editarRegistro(request, id):
	# traemos el objecto con el id
	Producto = producto.objects.get(id=id)
	if (request.method == 'GET'):
		form = ProdForm(instance = Producto) #creamos formulario a aprtir del objeto
	else:
		form = ProdForm(request.POST, instance = Producto)
		if form.is_valid():
			form.save()
		return redirect('productos:listaProductos')
	return render(request, 'tablas/ProductoFormulario.html', {'form' : form})

def eliminarRegistro(request, id):
	Producto = producto.objects.get(id=id).delete()
	return redirect('productos:listaProductos')

#PARA CATEGORIAS
def nuevoRegistroC(request):
	if request.method == 'POST':
		form = CatForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect ('productos:listaCategorias')
	else:
	#Esto es para generar un nuevo registro
		form = CatForm()
	return render(request, 'tablas/CategoriasFormulario.html', {'form' :form})

def editarRegistroC(request, id):
	# traemos el objecto con el id
	Categoria = categoria.objects.get(id=id)
	if (request.method == 'GET'):
		form = CatForm(instance = Categoria) #creamos formulario a aprtir del objeto
	else:
		form = CatForm(request.POST, instance = Categoria)
		if form.is_valid():
			form.save()
		return redirect('productos:listaCategorias')
	return render(request, 'tablas/CategoriasFormulario.html', {'form' : form})

def eliminarRegistroC(request, id):
	Categoria = categoria.objects.get(id=id).delete()
	return redirect('productos:listaCategorias')

#PARA VENTAS
def agregarCarrito(request, id):
	Producto = producto.objects.get(id=id)
	if (request.method == 'GET'):
		form = VentaProductoForm(instance = Producto)
	return render(request, 'tablas/ventaFormulario.html', {'form': form})

def pagar(request):
	return redirect('productos:ventas')


# Creamos una nueva clase
class viewProductos(ListView):
	model = producto
	template_name = 'tablas/productos.html'

# Otra clase para categorias
class viewCategorias(ListView):
	model = categoria
	#queryset = producto.objects.filter(id= '1')
	template_name = 'tablas/categorias.html'


class viewVentas(ListView):
	model = producto
	template_name = 'tablas/ventas.html'
