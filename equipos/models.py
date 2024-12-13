from django.db import models
from django.core.exceptions import ValidationError
from selecciones.models import Nacionalidad
from competiciones.models import Competencia

class Patrocinador(models.Model):
    nombre = models.CharField(max_length=255)
    presupuesto = models.IntegerField()

    def __str__(self):
        return self.nombre

class Estadio(models.Model):
    nombre = models.CharField(max_length=255)
    nivel = models.IntegerField()  # Por ejemplo, 1 a 5
    capacidad = models.IntegerField()
    equipo = models.OneToOneField('Equipo', on_delete=models.CASCADE, related_name="estadio")

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=255)
    fundacion = models.DateField()
    presupuesto = models.DecimalField(max_digits=15, decimal_places=2)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.SET_NULL, null=True, related_name="equipos")
    patrocinador = models.ForeignKey(Patrocinador, on_delete=models.SET_NULL, null=True, related_name="equipos")
    competencias = models.ManyToManyField(Competencia, related_name="equipos")

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    habilidades = models.JSONField()
    moral = models.IntegerField()
    salario = models.DecimalField(max_digits=15, decimal_places=2)
    lesion = models.BooleanField(default=False)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="jugadores")
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.SET_NULL, null=True, related_name="jugadores")

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


