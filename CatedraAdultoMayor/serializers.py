from rest_framework import serializers
from .models import Anciano, ContactoEmergencia, Enfermedad ,User, Role, Menu, RoleAccess

# Definimos una clase llamada EnfermedadSerializer que hereda de serializers.ModelSerializer
class EnfermedadSerializer(serializers.ModelSerializer):
    anciano = serializers.PrimaryKeyRelatedField(queryset=Anciano.objects.all())  # Permitir establecer el anciano

    class Meta:
        model = Enfermedad
        fields = ['id', 'nombre_enfermedad', 'fecha_diagnostico', 'descripcion', 'medicamento']  # Incluye los nuevos campos

class AncianoSerializer(serializers.ModelSerializer):
    enfermedades = EnfermedadSerializer(many=True, read_only=True)  # Campo anidado para enfermedades

    class Meta:  # Agrega la clase Meta aquí
        model = Anciano
        fields = '__all__'  # O define los campos que quieras exponer
class ContactoEmergenciaSerializer(serializers.ModelSerializer):
    anciano_nombre = serializers.CharField(source='anciano.nombre', read_only=True)  # Agrega el nombre del anciano

    class Meta:
        model = ContactoEmergencia
        fields = ['id', 'nombre_familiar', 'numero_telefono', 'relacion', 'direccion', 'genero', 'anciano', 'anciano_nombre']  # Incluye el nuevo campo


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