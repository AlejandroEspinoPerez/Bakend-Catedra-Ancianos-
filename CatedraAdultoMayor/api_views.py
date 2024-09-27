# hogar/api_views.py

from rest_framework import viewsets
from .models import Anciano, ContactoEmergencia, Enfermedad
from .serializers import AncianoSerializer, ContactoEmergenciaSerializer, EnfermedadSerializer

class AncianoViewSet(viewsets.ModelViewSet):
    queryset = Anciano.objects.all()
    serializer_class = AncianoSerializer

class ContactoEmergenciaViewSet(viewsets.ModelViewSet):
    queryset = ContactoEmergencia.objects.all()
    serializer_class = ContactoEmergenciaSerializer

class EnfermedadViewSet(viewsets.ModelViewSet):
    queryset = Enfermedad.objects.all()
    serializer_class = EnfermedadSerializer
