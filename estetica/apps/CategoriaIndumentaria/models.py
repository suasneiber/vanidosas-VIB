from django.db import models

# Create your models here.

class CategoriaIndumentaria(models.Model):
    categoria = models.CharField(max_length=20)