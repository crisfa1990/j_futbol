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


    def __str__(self):
        return self.nombre