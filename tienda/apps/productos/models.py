from django.db import models

# Create your models here.
class categoria(models.Model):
	nombreC=models.CharField(max_length=40)

class producto(models.Model):
	nombreProd = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=70)
	costo = models.CharField(max_length=15)
	disponible = models.BooleanField(default=False)
	existencias = models.IntegerField(default = 0)
	categoria = models.ForeignKey(categoria, null= True, blank = True, on_delete = models.CASCADE)



