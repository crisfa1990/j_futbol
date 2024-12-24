from django.urls import path
from . import views

urlpatterns = [
    path('jugadores/', views.jugadores_list, name='jugadores_list'),
    path('jugadores/<int:pk>/', views.jugador_detail, name='jugador_detail'),
    path('estadios/', views.estadios_list, name='estadios_list'),
    path('estadios/<int:pk>/', views.estadio_detail, name='estadio_detail'),
    path('equipos/', views.equipos_list, name='equipos_list'),
    path('equipos/<int:pk>/', views.equipo_detail, name='equipo_detail'),
    path('entrenadores/', views.entrenadores_list, name='entrenadores_list'),
    path('entrenadores/<int:pk>/', views.entrenador_detail, name='entrenador_detail'),
    path('partidos/', views.partidos_list, name='partidos_list'),
    path('partidos/<int:pk>/', views.partido_detail, name='partido_detail'),
]