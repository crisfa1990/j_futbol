from django.shortcuts import get_object_or_404, render
from .models import *

# JUGADORES
def jugadores_list(request):
    jugadores = Jugador.objects.all()
    return render(request, 'equipos/jugadores_list.html', {'jugadores': jugadores})

def jugador_detail(request, pk):
    jugador = Jugador.objects.get(pk=pk)
    return render(request, 'equipos/jugador_detail.html', {'jugador': jugador})

# ESTADIOS
def estadios_list(request):
    estadios = Estadio.objects.all()
    return render(request, 'equipos/estadios_list.html', {'estadios': estadios})

def estadio_detail(request, pk):
    estadio = get_object_or_404(Estadio, pk=pk)
    return render(request, 'equipos/estadio_detail.html', {'estadio': estadio})

# EQUIPOS
def equipos_list(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos/equipos_list.html', {'equipos': equipos})

def equipo_detail(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    return render(request, 'equipos/equipo_detail.html', {'equipo': equipo})

# ENTRENADORES
def entrenadores_list(request):
    entrenadores = Entrenador.objects.all()
    return render(request, 'equipos/entrenadores_list.html', {'entrenadores': entrenadores})

def entrenador_detail(request, pk):
    entrenador = get_object_or_404(Entrenador, pk=pk)
    return render(request, 'equipos/entrenador_detail.html', {'entrenador': entrenador})

# PARTIDOS
def partidos_list(request):
    partidos = Partido.objects.all()
    return render(request, 'equipos/partidos_list.html', {'partidos': partidos})

def partido_detail(request, pk):
    partido = get_object_or_404(Partido, pk=pk)
    return render(request, 'equipos/partido_detail.html', {'partido': partido})