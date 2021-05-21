from django.db import models


class Paciente(models.Model):

    nombre = models.CharField(max_length= 40)
    telefono = models.BigIntegerField()
    sintomas = models.CharField(max_length= 1000)
