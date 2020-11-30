from django.db import models

# Create your models here.
class CursoModels(models.Model):
     nombre = models.CharField(max_length=15)
     CargaHoraria = models.IntegerField(max_length=2)
     costo = models.IntegerField(max_length=3)