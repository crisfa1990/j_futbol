from django.urls import path
from . import views

urlpatterns = [
    path('jugadores/', views.jugadores_list, name='jugadores_list'),
    path('jugadores/<int:pk>/', views.jugador_detail, name='jugador_detail'),
    path('estadios/', views.estadios_list, name='estadios_list'),
    path('estadios/<int:pk>/', views.estadio_detail, name='estadio_detail'),
]