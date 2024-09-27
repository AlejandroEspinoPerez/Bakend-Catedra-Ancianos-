# hogar/serializers.py

from rest_framework import serializers
from .models import Anciano, ContactoEmergencia, Enfermedad

class AncianoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anciano
        fields = '__all__'  # O define los campos que quieras exponer

class ContactoEmergenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactoEmergencia
        fields = '__all__'

class EnfermedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermedad
        fields = '__all__'
