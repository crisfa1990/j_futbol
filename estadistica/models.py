from django.db import models
from equipos.models import Equipo, Jugador


class Temporada(models.Model):
    anio = models.IntegerField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return str(self.anio)

class EstadisticaPorTemporada(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name="estadisticas")
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE, related_name="estadisticas")
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="estadisticas")
    goles = models.IntegerField(default=0)
    asistencias = models.IntegerField(default=0)
    partidos = models.IntegerField(default=0)

    class Meta:
        unique_together = ("jugador", "temporada", "equipo")

    def __str__(self):
        return f"{self.jugador.nombre} - {self.temporada.anio}"
    


