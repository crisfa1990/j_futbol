from django.db import models
from django.core.exceptions import ValidationError
from selecciones.models import Nacionalidad
from competiciones.models import Competencia

class Patrocinador(models.Model):
    nombre = models.CharField(max_length=255)
    presupuesto = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Equipo(models.Model):
    nombre = models.CharField(max_length=255)
    fundacion = models.DateField()
    presupuesto = models.DecimalField(max_digits=15, decimal_places=2)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.SET_NULL, null=True, related_name="equipos")
    patrocinador = models.ForeignKey(Patrocinador, on_delete=models.SET_NULL, null=True, related_name="equipos")
    competencias = models.ManyToManyField(Competencia)
    goles_favor = models.IntegerField(default=0)
    goles_contra = models.IntegerField(default=0)
    asistencias = models.IntegerField(default=0)
    partidos_jugados = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Estadio(models.Model):
    nombre = models.CharField(max_length=255)
    nivel = models.IntegerField()  # Por ejemplo, 1 a 5
    capacidad = models.IntegerField()
    equipo = models.OneToOneField('Equipo', on_delete=models.CASCADE, related_name="estadio")

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    habilidades = models.JSONField()
    moral = models.IntegerField()
    salario = models.DecimalField(max_digits=15, decimal_places=2)
    lesion = models.BooleanField(default=False)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="jugadores")
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.SET_NULL, null=True, related_name="jugadores")
    goles_carrera = models.IntegerField(default=0)
    asistencias_carrera = models.IntegerField(default=0)
    partidos_carrera = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Entrenador(models.Model):
    TIPO_ENTRENADOR = [
        ('Ofensivo', 'Ofensivo'),
        ('Defensivo', 'Defensivo'),
        ('Equilibrado', 'Equilibrado'),
    ]

    nombre = models.CharField(max_length=255)
    experiencia = models.IntegerField()  # Años de experiencia
    tipo = models.CharField(max_length=50, choices=TIPO_ENTRENADOR)
    entrenamiento = models.IntegerField(default=0)  # Escala de 0-100
    tactica = models.IntegerField(default=0)  # Escala de 0-100
    motivacion = models.IntegerField(default=0)  # Escala de 0-100
    equipo_actual = models.OneToOneField(
        Equipo, on_delete=models.SET_NULL, null=True, blank=True, related_name="entrenador"
    )

    def __str__(self):
        return self.nombre

class Lesion(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name="lesiones")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    tipo = models.CharField(max_length=50)  # Leve, Moderada, Grave
    impacto = models.IntegerField()  # Porcentaje de impacto en habilidades

    def __str__(self):
        return f"{self.tipo} - {self.jugador.nombre}"

class Temporada(models.Model):
    anio = models.IntegerField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return str(self.anio)
    
class Partido(models.Model):
    fecha = models.DateField()
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="partidos_local")
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="partidos_visitante")
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE, related_name="partidos")
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE, related_name="partidos")
    estadio = models.ForeignKey(Estadio, on_delete=models.SET_NULL, null=True, related_name="partidos")
    goles_local = models.IntegerField(default=0)
    goles_visitante = models.IntegerField(default=0)
    goles_jugadores_local = models.JSONField(default=dict)  # {jugador_id: goles}
    goles_jugadores_visitante = models.JSONField(default=dict)  # {jugador_id: goles}
    asistencias_jugadores_local = models.JSONField(default=dict)  # {jugador_id: asistencias}
    asistencias_jugadores_visitante = models.JSONField(default=dict)  # {jugador_id: asistencias}

    def __str__(self):
        return f"{self.equipo_local.nombre} vs {self.equipo_visitante.nombre} - {self.competencia.nombre}"

class EstadisticaPorTemporada(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name="estadisticas")
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE, related_name="estadisticas")
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="estadisticas")
    goles = models.IntegerField(default=0)
    asistencias = models.IntegerField(default=0)
    partidos = models.IntegerField(default=0)

    class Meta:
        unique_together = ("jugador", "temporada", "equipo")
        indexes = [
            models.Index(fields=['jugador', 'temporada', 'equipo']),
        ]

    def __str__(self):
        return f"{self.jugador.nombre} - {self.temporada.anio}"
