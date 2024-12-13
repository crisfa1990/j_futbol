from django.db import models
from competiciones.models import Competencia, Temporada
from equipos.models import Jugador
from selecciones.models import Nacionalidad


class Convocatoria(models.Model):
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE, related_name="convocatorias")
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name="convocatorias")
    equipo_nacional = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE, related_name="convocatorias")

    class Meta:
        unique_together = ("competencia", "jugador")

    def __str__(self):
        return f"{self.jugador.nombre} - {self.competencia.nombre}"
    
class Nacionalidad(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre