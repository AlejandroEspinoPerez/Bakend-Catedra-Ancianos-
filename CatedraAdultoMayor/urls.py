# hogar/urls.py

from django.urls import path
from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import AncianoViewSet, ContactoEmergenciaViewSet, EnfermedadViewSet,UserViewSet, RoleViewSet, MenuViewSet, RoleAccessViewSet

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
     # URL para agregar enfermedad a un anciano
    path('api/ancianos/<int:pk>/agregar_enfermedad/', EnfermedadViewSet.as_view({'post': 'agregar_enfermedad'})),
    path('api/ancianos/<int:pk>/agregar-contacto/', AncianoViewSet.as_view({'post': 'agregar_contacto'})),

    path('', views.lista_ancianos, name='lista_ancianos'),
    path('crear/', views.crear_anciano, name='crear_anciano'),
    path('editar/<int:id>/', views.editar_anciano, name='editar_anciano'),
    path('eliminar/<int:id>/', views.eliminar_anciano, name='eliminar_anciano'),
    path('ancianos/', views.lista_ancianos, name='lista_ancianos'),
    path('contactos/', views.lista_contactos_todos, name='lista_contactos_todos'),
    path('ancianos/<int:anciano_id>/contactos/', views.lista_contactos, name='lista_contactos'),
    path('ancianos/<int:anciano_id>/contactos/crear/', views.crear_contacto, name='crear_contacto'),
    path('contactos/editar/<int:id>/', views.editar_contacto, name='editar_contacto'),
    path('contactos/eliminar/<int:id>/', views.eliminar_contacto, name='eliminar_contacto'),
    # Rutas para enfermedades
    path('enfermedades/', views.lista_enfermedades_todas, name='lista_enfermedades_todas'),
    path('ancianos/<int:anciano_id>/enfermedad/crear/', views.crear_enfermedad, name='crear_enfermedad'),
    path('ancianos/<int:anciano_id>/enfermedades/', views.lista_enfermedades, name='lista_enfermedades'),
    path('ancianos/<int:anciano_id>/enfermedades/crear/', views.crear_enfermedad, name='crear_enfermedad'),
    path('enfermedades/editar/<int:id>/', views.editar_enfermedad, name='editar_enfermedad'),
    path('enfermedades/eliminar/<int:id>/', views.eliminar_enfermedad, name='eliminar_enfermedad'),
]
