import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'j_futbol.settings')
django.setup()

from equipos.models import Partido, Jugador

def debug_partido(partido_id):
    partido = Partido.objects.get(pk=partido_id)
    jugadores_local = Jugador.objects.filter(equipo=partido.equipo_local)
    jugadores_visitante = Jugador.objects.filter(equipo=partido.equipo_visitante)

    print(f"Partido: {partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre}")
    print(f"Fecha: {partido.fecha}")
    print(f"Competencia: {partido.competencia.nombre}")
    print(f"Temporada: {partido.temporada.anio}")
    print(f"Estadio: {partido.estadio.nombre if partido.estadio else 'N/A'}")
    print(f"Goles Local: {partido.goles_local}")
    print(f"Goles Visitante: {partido.goles_visitante}")

    print("\nGoles del equipo local:")
    for jugador_id, goles in partido.goles_jugadores_local.items():
        jugador_id = int(jugador_id)  # Asegurarse de que el ID sea un entero
        jugador = jugadores_local.filter(pk=jugador_id).first()
        if jugador:
            print(f"{jugador.nombre}: {goles} goles")
        else:
            print(f"Jugador con ID {jugador_id} no encontrado en el equipo local")

    print("\nGoles del equipo visitante:")
    for jugador_id, goles in partido.goles_jugadores_visitante.items():
        jugador_id = int(jugador_id)  # Asegurarse de que el ID sea un entero
        jugador = jugadores_visitante.filter(pk=jugador_id).first()
        if jugador:
            print(f"{jugador.nombre}: {goles} goles")
        else:
            print(f"Jugador con ID {jugador_id} no encontrado en el equipo visitante")

    print("\nAsistencias del equipo local:")
    for jugador_id, asistencias in partido.asistencias_jugadores_local.items():
        jugador_id = int(jugador_id)  # Asegurarse de que el ID sea un entero
        jugador = jugadores_local.filter(pk=jugador_id).first()
        if jugador:
            print(f"{jugador.nombre}: {asistencias} asistencias")
        else:
            print(f"Jugador con ID {jugador_id} no encontrado en el equipo local")

    print("\nAsistencias del equipo visitante:")
    for jugador_id, asistencias in partido.asistencias_jugadores_visitante.items():
        jugador_id = int(jugador_id)  # Asegurarse de que el ID sea un entero
        jugador = jugadores_visitante.filter(pk=jugador_id).first()
        if jugador:
            print(f"{jugador.nombre}: {asistencias} asistencias")
        else:
            print(f"Jugador con ID {jugador_id} no encontrado en el equipo visitante")

if __name__ == "__main__":
    partido_id = 2  # Cambia esto al ID del partido que quieres depurar
    debug_partido(partido_id)