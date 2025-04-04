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
    path('partidos/<int:pk>/registrar_resultado/', views.registrar_resultado, name='registrar_resultado'),
    path('alineacion/crear/', views.crear_alineacion, name='crear_alineacion'),
    path('alineacion/crear/<int:equipo_id>/<int:partido_id>/', views.crear_alineacion_preseleccionada, name='crear_alineacion_preseleccionada'),
    path('alineacion/<int:pk>/', views.alineacion_detail, name='alineacion_detail'),
    path('alineacion/<int:pk>/editar/', views.editar_alineacion, name='editar_alineacion'),
    path('api/equipos/<int:equipo_id>/jugadores/', views.get_jugadores_equipo, name='api_jugadores_equipo'),
]