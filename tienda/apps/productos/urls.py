from django.urls import path
from apps.productos.views import index, infProd, infCat, viewProductos, viewCategorias, nuevoRegistro, editarRegistro
from apps.productos.views import eliminarRegistro, nuevoRegistroC, editarRegistroC, eliminarRegistroC, ventas, viewVentas
from apps.productos.views import agregarCarrito, pagar

app_name= 'productos'
urlpatterns = [
	path('', viewProductos.as_view()),
	path('index', viewProductos.as_view()),
	# path('infProd', infProd),
	# path('infCat', infCat),
	path('infProd', viewProductos.as_view(), name= "listaProductos"),
	path('nuevoRegistro', nuevoRegistro, name= "nuevoRegistro"),
    path('editarRegistro/<id>', editarRegistro, name= "editarRegistro"),
    path('eliminarRegistro/<id>', eliminarRegistro, name= "eliminarRegistro"),

	path('infCat', viewCategorias.as_view(), name = 'listaCategorias'),
	path('nuevoRegistroC', nuevoRegistroC, name= "nuevoRegistroC"),
    path('editarRegistroC/<id>', editarRegistroC, name= "editarRegistroC"),
    path('eliminarRegistroC/<id>', eliminarRegistroC, name= "eliminarRegistroC"),
     path('agregarCarrito/<id>', agregarCarrito, name = "agregarCarrito"),
    path('pagar', pagar, name= "pagar"),
    path('ventas' , viewVentas.as_view(), name = "ventas"),
]