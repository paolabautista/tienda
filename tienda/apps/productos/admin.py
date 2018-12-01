from django.contrib import admin
from apps.productos.models import producto, categoria
##IMPORTAMOS PRIMERO LAS CLASES Y POSTERIORMENTE
###LAS REGISTRAMOS
admin.site.register(producto)
admin.site.register(categoria)
