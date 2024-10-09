from rest_framework import serializers
from .models import Anciano, ContactoEmergencia, Enfermedad ,User, Role, Menu, RoleAccess

# Definimos una clase llamada EnfermedadSerializer que hereda de serializers.ModelSerializer
class EnfermedadSerializer(serializers.ModelSerializer):
    
    class Meta:
        # Especificamos que este serializer está asociado con el modelo Enfermedad
        model = Enfermedad
        # Definimos los campos que queremos incluir en la representación del serializer
        fields = ['id', 'nombre_enfermedad', 'fecha_diagnostico']

class AncianoSerializer(serializers.ModelSerializer):
    enfermedades = EnfermedadSerializer(many=True, read_only=True)  # Campo anidado para enfermedades

    class Meta:  # Agrega la clase Meta aquí
        model = Anciano
        fields = '__all__'  # O define los campos que quieras exponer

class ContactoEmergenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactoEmergencia
        fields = ['id', 'nombre_familiar', 'numero_telefono', 'relacion']  # Incluye anciano


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class RoleAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleAccess
        fields = '__all__'