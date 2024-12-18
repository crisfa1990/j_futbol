from django.shortcuts import render
from .models import Jugador

def jugadores_list(request):
    jugadores = Jugador.objects.all()
    return render(request, 'equipos/jugadores_list.html', {'jugadores': jugadores})

def jugador_detail(request, pk):
    jugador = Jugador.objects.get(pk=pk)
    return render(request, 'equipos/jugador_detail.html', {'jugador': jugador})
