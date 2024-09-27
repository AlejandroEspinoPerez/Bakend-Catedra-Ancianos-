from django.contrib import admin
from django.urls import include, path
from CatedraAdultoMayor import views  # Importa las vistas de tu aplicación

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from CatedraAdultoMayor.api_views import AncianoViewSet, ContactoEmergenciaViewSet, EnfermedadViewSet


router = DefaultRouter()
router.register(r'ancianos', AncianoViewSet)
router.register(r'contactos', ContactoEmergenciaViewSet)
router.register(r'enfermedades', EnfermedadViewSet)

urlpatterns = [
    # Rutas de la API
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),  # Apunta a la vista del dashboard en la raíz
    path('tareas/', include('mi_aplicacion.urls')),
    path('ancianos/', include('CatedraAdultoMayor.urls')),
]
