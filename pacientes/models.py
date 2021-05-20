from django.db import models


class Paciente(models.Model):

    nombre = models.CharField(max_length= 40)
    telefono = models.IntegerField()
    sintomas = models.CharField(max_length= 200)
