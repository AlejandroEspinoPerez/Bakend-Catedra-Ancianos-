# CatedraadultoMayor/models.py

from django.db import models

class Anciano(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=255)
    genero = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'


class ContactoEmergencia(models.Model):
    anciano = models.ForeignKey(Anciano, on_delete=models.CASCADE, related_name='contactos')
    nombre_familiar = models.CharField(max_length=100)
    relacion = models.CharField(max_length=50)
    numero_telefono = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nombre_familiar} ({self.relacion}) - {self.numero_telefono}'
    
# CatedraadultoMayor/models.py

class Enfermedad(models.Model):
    anciano = models.ForeignKey(Anciano, on_delete=models.CASCADE, related_name='enfermedades')
    nombre_enfermedad = models.CharField(max_length=255)
    fecha_diagnostico = models.DateField()

    def __str__(self):
        return f'{self.nombre_enfermedad} ({self.fecha_diagnostico})'
