from django.urls import path
from . import views

urlpatterns = [
    path('jugadores/', views.jugadores_list, name='jugadores_list'),
    path('jugadores/<int:pk>/', views.jugador_detail, name='jugador_detail'),
]