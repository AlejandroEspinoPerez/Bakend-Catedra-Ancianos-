from django.contrib import admin
from django.urls import include, path
from CatedraAdultoMayor import views  # Importa las vistas de tu aplicación

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from CatedraAdultoMayor.api_views import AncianoViewSet, ContactoEmergenciaViewSet, EnfermedadViewSet,UserViewSet, RoleViewSet, MenuViewSet, RoleAccessViewSet


router = DefaultRouter()
router.register(r'ancianos', AncianoViewSet)
router.register(r'contactos', ContactoEmergenciaViewSet)
router.register(r'enfermedades', EnfermedadViewSet)
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'roleaccess', RoleAccessViewSet)

urlpatterns = [
    # Rutas de la API
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),  # Apunta a la vista del dashboard en la raíz
    path('tareas/', include('mi_aplicacion.urls')),
    path('ancianos/', include('CatedraAdultoMayor.urls')),
]
