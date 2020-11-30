from django.db import models
from apps.curso.models import CursoModels
# Create your models here.

class Alumno(models.Model):
    curso = models.ForeignKey(CursoModels, default=None, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=20)
    tel = models.IntegerField(max_length=12)
    dni = models.IntegerField(max_length=8)

