from django.db import models
from selecciones.models import Nacionalidad
from competiciones.models import Competencia

class Patrocinador(models.Model):
    nombre = models.CharField(max_length=255)
    objetivo_basico = models.IntegerField(default = 0)
    objetivo_extra = models.IntegerField(default = 0)

    def __str__(self):
        return self.nombre
    
class Equipo(models.Model):
    nombre = models.CharField(max_length=255)
    fundacion = models.DateField()
    presupuesto = models.IntegerField(default = 0 )
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
    mantenimiento = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    portero = models.BooleanField(default=False)
    habilidades = models.JSONField()
    moral = models.IntegerField(default = 5) # Escala de 0-10
    forma_fisica = models.IntegerField(default = 5) # Escala de 0-10    
    salario = models.IntegerField(default = 60000)
    lesion = models.BooleanField(default=False)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="jugadores")
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.SET_NULL, null=True, related_name="jugadores")
    goles_carrera = models.IntegerField(default=0)
    asistencias_carrera = models.IntegerField(default=0)
    partidos_carrera = models.IntegerField(default=0)
    partidos_internacionales = models.IntegerField(default=0)
    goles_internacionales = models.IntegerField(default=0)
    asistencias_internacionales = models.IntegerField(default=0)

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
    espectadores = models.IntegerField(default=0)  # Total de personas que vieron el partido
    CLIMA_OPCIONES = [
        ('Despejado', 'Despejado'),
        ('Parcialmente nublado', 'Parcialmente nublado'),
        ('Nublado', 'Nublado'),
        ('Lluvia', 'Lluvia'),
    ]
    clima = models.CharField(max_length=20, choices=CLIMA_OPCIONES, default='Despejado')

    def __str__(self):
        return f"{self.equipo_local.nombre} vs {self.equipo_visitante.nombre} - {self.competencia.nombre}"
    
class Transferencia(models.Model):
    jugador = models.ForeignKey('Jugador', on_delete=models.CASCADE, related_name='transferencias')
    equipo_anterior = models.ForeignKey('Equipo', on_delete=models.SET_NULL, null=True, related_name='salidas')
    equipo_nuevo = models.ForeignKey('Equipo', on_delete=models.SET_NULL, null=True, related_name='fichajes')
    monto_transferencia = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_transferencia = models.DateField()

    def __str__(self):
        return f"{self.jugador.nombre} de {self.equipo_anterior} a {self.equipo_nuevo}" if self.equipo_anterior and self.equipo_nuevo else self.jugador.nombre

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

class Alineacion(models.Model):

    ESTILOS_PASES = [('C', 'Cortos'), ('L', 'Largos'), ('M', 'Mixtos')]
    ACTITUD = [('A', 'Ataque'), ('D', 'Defensa'), ('E', 'Equilibrado'), ('L', 'Lateral')]
    ENTRADAS = [('F', 'Fuertes'), ('N', 'Normal'), ('S', 'Suaves')]
    MARCAJE = [('F', 'Férreo'), ('N', 'Normal'), ('Z', 'A zona')]
    PRESION = [('B', 'Baja'), ('M', 'Media'), ('A', 'Alta')]
    
    estilo_pases = models.CharField(max_length=1, choices=ESTILOS_PASES, default='M')
    actitud = models.CharField(max_length=1, choices=ACTITUD, default='E')
    entradas = models.CharField(max_length=1, choices=ENTRADAS, default='N')
    marcaje = models.CharField(max_length=1, choices=MARCAJE, default='N')
    presion = models.CharField(max_length=1, choices=PRESION, default='M')
    nombre = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE, related_name='alineaciones')
    partido = models.ForeignKey('Partido', on_delete=models.CASCADE, related_name='alineaciones')
    titulares = models.JSONField(default=list)  # Almacena una lista de IDs de jugadores
    suplentes = models.JSONField(default=list)  # Almacena una lista de IDs de jugadores

    @staticmethod
    def get_or_create_alineacion(equipo, partido):
        alineacion, created = Alineacion.objects.get_or_create(equipo=equipo, partido=partido, defaults={
            'nombre': f'Alineación {equipo.nombre} vs {partido.equipo_visitante if equipo == partido.equipo_local else partido.equipo_local}',
            'titulares': [],
            'suplentes': [],
            'estrategia': None
        })
        return alineacion, created

    def actualizar_alineacion(self, titulares, suplentes, estrategia):
        self.titulares = titulares
        self.suplentes = suplentes
        self.estrategia = estrategia
        self.save()

    def __str__(self):
        return f"Alineación {self.nombre} ({self.equipo}) para {self.partido}"

