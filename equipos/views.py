from django.shortcuts import get_object_or_404, render, redirect
from .models import *

# JUGADORES
def jugadores_list(request):
    jugadores = Jugador.objects.all()
    return render(request, 'equipos/jugadores_list.html', {'jugadores': jugadores})

def jugador_detail(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    estadisticas = EstadisticaPorTemporada.objects.filter(jugador=jugador)
    return render(request, 'equipos/jugador_detail.html', {'jugador': jugador, 'estadisticas': estadisticas})

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
    jugadores = Jugador.objects.filter(equipo=equipo)
    return render(request, 'equipos/equipo_detail.html', {'equipo': equipo, 'jugadores': jugadores})

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
    jugadores_ids = (
        list(partido.goles_jugadores_local.keys()) +
        list(partido.goles_jugadores_visitante.keys()) +
        list(partido.asistencias_jugadores_local.keys()) +
        list(partido.asistencias_jugadores_visitante.keys())
    )
    jugadores = Jugador.objects.filter(pk__in=jugadores_ids)
    jugadores_dict = {str(jugador.pk): jugador for jugador in jugadores}

    return render(request, 'equipos/partido_detail.html', {
        'partido': partido,
        'jugadores_dict': jugadores_dict
    })

# REGISTRAR GOLES, ASISTENCIAS Y PARTIDOS

def registrar_resultado(request, pk):
    partido = get_object_or_404(Partido, pk=pk)
    if request.method == 'POST':
        goles_local = int(request.POST['goles_local'])
        goles_visitante = int(request.POST['goles_visitante'])
        goles_jugadores = request.POST.getlist('goles_jugadores')
        asistencias_jugadores = request.POST.getlist('asistencias_jugadores')

        partido.goles_local = goles_local
        partido.goles_visitante = goles_visitante
        partido.goles_jugadores = goles_jugadores
        partido.asistencias_jugadores = asistencias_jugadores
        partido.save()

        # Actualizar goles y asistencias de los equipos
        partido.equipo_local.goles_favor += goles_local
        partido.equipo_local.goles_contra += goles_visitante
        partido.equipo_local.partidos_jugados += 1
        partido.equipo_local.save()

        partido.equipo_visitante.goles_favor += goles_visitante
        partido.equipo_visitante.goles_contra += goles_local
        partido.equipo_visitante.partidos_jugados += 1
        partido.equipo_visitante.save()

        # Actualizar goles y asistencias de los jugadores
        for jugador_id in goles_jugadores:
            jugador = Jugador.objects.get(pk=jugador_id)
            jugador.goles_carrera += 1
            jugador.partidos_carrera += 1
            jugador.save()

            estadistica, created = EstadisticaPorTemporada.objects.get_or_create(
                jugador=jugador, temporada=partido.temporada, equipo=jugador.equipo,
                defaults={'goles': 0, 'asistencias': 0, 'partidos': 0}
            )
            estadistica.goles += 1
            estadistica.partidos += 1
            estadistica.save()

        for jugador_id in asistencias_jugadores:
            jugador = Jugador.objects.get(pk=jugador_id)
            jugador.asistencias_carrera += 1
            jugador.partidos_carrera += 1
            jugador.save()

            estadistica, created = EstadisticaPorTemporada.objects.get_or_create(
                jugador=jugador, temporada=partido.temporada, equipo=jugador.equipo,
                defaults={'goles': 0, 'asistencias': 0, 'partidos': 0}
            )
            estadistica.asistencias += 1
            estadistica.partidos += 1
            estadistica.save()

        return redirect('partido_detail', pk=partido.pk)

    return render(request, 'equipos/registrar_resultado.html', {'partido': partido})
