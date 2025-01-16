from django.db import models

class Competencia(models.Model):
    TIPO_COMPETENCIA = [
        ('Liga Local', 'Liga Local'),
        ('Copa Local', 'Copa Local'),
        ('Copa Internacional', 'Copa Internacional'),
        ('Seleccion Nacional', 'Seleccion Nacional'),
        ('Amistosos', 'Amistosos'),
        ('Copa Internacional de Equipos', 'Copa Internacional de Equipos'),
        ('Partidos de Promocion', 'Partidos de Promocion'),
    ]

    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, choices=TIPO_COMPETENCIA)
    temporada = models.ForeignKey('equipos.Temporada', on_delete=models.CASCADE)
    equipos = models.ManyToManyField('equipos.Equipo')
    nacionalidad = models.OneToOneField('selecciones.Nacionalidad', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    bono_por_partido = models.IntegerField(default=0)
    bono_por_titulo = models.IntegerField(default=0)
    bono_por_victoria = models.IntegerField(default=0)
    bono_por_clasificacion = models.IntegerField(default=0)
    sistema_puntos = models.JSONField(default=dict)  # Por ejemplo, {"victoria": 3, "empate": 1, "derrota": 0}
    fases = models.JSONField(default=dict)  # Por ejemplo, {"grupos": ["A", "B"], "eliminatorias": ["cuartos", "semifinal", "final"]}
    trofeo = models.BooleanField(default=True)  # Indica si la competencia tiene un trofeo asociado

    def __str__(self):
        return self.nombre
    
    def esta_disponible(self, fecha_actual):
        return fecha_actual > self.fecha_fin if self.fecha_fin else True

    def calcular_inversion_total(self):
        return self.presupuesto + self.bono_por_titulo + self.bono_por_victoria + self.bono_por_clasificacion 
