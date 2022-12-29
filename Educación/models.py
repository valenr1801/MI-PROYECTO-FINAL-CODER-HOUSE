from django.db import models
#CARRERAS
class Carreras(models.Model):
    nombre = models.CharField(max_length=100)
    facultad = models.CharField(max_length=200)
    duracion = models.CharField(max_length=200)
def __str__(self):
    return f"{self.nombre}, {self.facultad}, {self.duracion}"

#ALUMNOS
class Alumnos(models.Model):
    nombre = models.CharField(max_length=100)
    facultad = models.CharField(max_length=200)
    edad = models.CharField(max_length=200)
def __str__(self):
    return f"{self.nombre}, {self.facultad}, {self.edad}"

#PROFESORES
class Profesores(models.Model):
    nombre = models.CharField(max_length=100)
    facultad = models.CharField(max_length=200)
    tiempo = models.CharField(max_length=200)
def __str__(self):
    return f"{self.nombre}, {self.facultad}, {self.tiempo}"