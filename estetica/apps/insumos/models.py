from django.db import models

# Create your models here.

class insumo(models.Model):
    nombre = models.CharField(max_length=30)
    cantidad = models.CharField(max_length=3)
    precioCosto = models.CharField(max_length=4)
    precioVenta = models.CharField(max_length=4)
    codigo = models.CharField(max_length=13)
    tipo = models.CharField(max_length=10)
    tamaño = models.CharField(max_length=7, default=None)
