from pyexpat import model
from re import M
from django.db import models

# Create your models here.

class Prueba(models.Model):
    nombre = models.CharField(max_length=20)
