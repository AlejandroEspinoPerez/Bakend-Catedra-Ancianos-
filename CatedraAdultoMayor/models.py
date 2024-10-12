# CatedraadultoMayor/models.py

from django.db import models

class Anciano(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=255)
    genero = models.CharField(max_length=10)
    numero_telefono = models.CharField(max_length=15)  # Nuevo campo

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

class ContactoEmergencia(models.Model):
    anciano = models.ForeignKey(Anciano, on_delete=models.CASCADE, related_name='contactos')
    nombre_familiar = models.CharField(max_length=100)
    relacion = models.CharField(max_length=50)
    numero_telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)  # Nuevo campo
    genero = models.CharField(max_length=10)  # Nuevo campo

    def __str__(self):
        return f'{self.nombre_familiar} ({self.relacion}) - {self.numero_telefono}'
    
# CatedraadultoMayor/models.py

class Enfermedad(models.Model):
    anciano = models.ForeignKey(Anciano, on_delete=models.CASCADE, related_name='enfermedades')
    nombre_enfermedad = models.CharField(max_length=255)
    fecha_diagnostico = models.DateField()
    descripcion = models.TextField()  # Nuevo campo
    medicamento = models.CharField(max_length=255)  # Nuevo campo

    def __str__(self):
        return f'{self.nombre_enfermedad} ({self.fecha_diagnostico})'

class User(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    role = models.CharField(max_length=100, blank=True, null=True)
    isactive = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Menu(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RoleAccess(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    haveedit = models.BooleanField(default=False)
    haveadd = models.BooleanField(default=False)
    havedelete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.role} - {self.menu}"