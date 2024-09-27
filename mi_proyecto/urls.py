from django.contrib import admin
from django.urls import include, path
from CatedraAdultoMayor import views  # Importa las vistas de tu aplicación

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),  # Apunta a la vista del dashboard en la raíz
    path('tareas/', include('mi_aplicacion.urls')),
    path('ancianos/', include('CatedraAdultoMayor.urls')),
]
