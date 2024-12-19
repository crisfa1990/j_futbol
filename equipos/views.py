from django.shortcuts import get_object_or_404, render
from .models import Jugador, Estadio

def jugadores_list(request):
    jugadores = Jugador.objects.all()
    return render(request, 'equipos/jugadores_list.html', {'jugadores': jugadores})

def jugador_detail(request, pk):
    jugador = Jugador.objects.get(pk=pk)
    return render(request, 'equipos/jugador_detail.html', {'jugador': jugador})

def estadios_list(request):
    estadios = Estadio.objects.all()
    return render(request, 'estadios_list.html', {'estadios': estadios})

def estadio_detail(request, pk):
    estadio = get_object_or_404(Estadio, pk=pk)
    return render(request, 'estadio_detail.html', {'estadio': estadio})