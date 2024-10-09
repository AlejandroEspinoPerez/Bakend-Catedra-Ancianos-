# hogar/api_views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Anciano, ContactoEmergencia, Enfermedad ,User, Role, Menu, RoleAccess
from .serializers import AncianoSerializer, ContactoEmergenciaSerializer, EnfermedadSerializer,UserSerializer, RoleSerializer, MenuSerializer, RoleAccessSerializer
from rest_framework.decorators import action

class AncianoViewSet(viewsets.ModelViewSet):
    queryset = Anciano.objects.all()
    serializer_class = AncianoSerializer

    @action(detail=True, methods=['post'], url_path='agregar-enfermedad')
    def agregar_enfermedad(self, request, pk=None):
        anciano = self.get_object()  # Obtiene el anciano a través de la URL
        serializer = EnfermedadSerializer(data=request.data)
        if serializer.is_valid():
            # Asignamos el anciano al campo correspondiente en Enfermedad
            serializer.save(anciano=anciano)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], url_path='agregar-contacto')
    def agregar_contacto(self, request, pk=None):
        anciano = self.get_object()  # Obtiene el anciano desde la URL
        serializer = ContactoEmergenciaSerializer(data=request.data)
        if serializer.is_valid():
            # Asignamos el anciano al contacto
            serializer.save(anciano=anciano)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactoEmergenciaViewSet(viewsets.ModelViewSet):
    queryset = ContactoEmergencia.objects.all()
    serializer_class = ContactoEmergenciaSerializer

class EnfermedadViewSet(viewsets.ModelViewSet):
    queryset = Enfermedad.objects.all()
    serializer_class = EnfermedadSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class RoleAccessViewSet(viewsets.ModelViewSet):
    queryset = RoleAccess.objects.all()  # Aquí defines el queryset
    serializer_class = RoleAccessSerializer

    def get_queryset(self):
        role = self.request.query_params.get('role', None)
        menu = self.request.query_params.get('menu', None)
        
        queryset = super().get_queryset()  # Llama al queryset definido arriba
        
        if role is not None and menu is not None:
            queryset = queryset.filter(role=role, menu=menu)
        
        return queryset