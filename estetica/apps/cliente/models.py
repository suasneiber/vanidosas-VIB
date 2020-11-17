from django.db import models

# Create your models here.

class cliente(models.Model):
    nombreApellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    tratamiento = models.CharField(max_length=30)
    fecha = models.DateField(auto_now=False, auto_now_add=False)