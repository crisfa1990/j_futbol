import random

def calcular_probabilidad_gol(jugador):
    habilidad_ofensiva = jugador.remate + jugador.desmarques
    probabilidad = habilidad_ofensiva / 100
    return random.random() < probabilidad

def simular_partido(equipo_local, equipo_visitante):
    goles_local = 0
    goles_visitante = 0

    for jugador in equipo_local.jugadores.all():
        if calcular_probabilidad_gol(jugador):
            goles_local += 1

    for jugador in equipo_visitante.jugadores.all():
        if calcular_probabilidad_gol(jugador):
            goles_visitante += 1

    return goles_local, goles_visitante