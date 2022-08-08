from django.db import models

class Familiares(models.Model):
    nombre = models.CharField (max_length=20)
    apellido = models.CharField (max_length=20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateTimeField()
    