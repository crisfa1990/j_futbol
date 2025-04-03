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
    defensa = models.IntegerField(default=0)
    pases = models.IntegerField(default=0)
    remate = models.IntegerField(default=0,)
    lateral = models.IntegerField(default=0)
    mentalidad = models.IntegerField(default=0)
    vision = models.IntegerField(default=0)
    desmarques = models.IntegerField(default=0)
    atajadas = models.IntegerField(default=0)  # Solo para porteros
    distribucion = models.IntegerField(default=0)  # Solo para porteros
    moral = models.IntegerField(default=5)  # Escala de 0-10
    forma_fisica = models.IntegerField(default=5)  # Escala de 0-10    
    salario = models.IntegerField(default=60000)
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
    # ... (después de la clase Partido)

class GolPartido(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='goles')
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='goles')
    minuto = models.IntegerField()
    es_local = models.BooleanField()  # True si el jugador es del equipo local
    tipo = models.CharField(max_length=20, choices=[
        ('Normal', 'Normal'),
        ('Penal', 'Penal'),
        ('Falta', 'Falta'),
        ('Autogol', 'Autogol')
    ], default='Normal')

    class Meta:
        ordering = ['minuto']

    def __str__(self):
        return f"Gol de {self.jugador.nombre} - {self.partido}"

class AsistenciaPartido(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='asistencias')
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='asistencias')
    gol = models.OneToOneField(GolPartido, on_delete=models.CASCADE, related_name='asistencia')
    es_local = models.BooleanField()  # True si el jugador es del equipo local

    def __str__(self):
        return f"Asistencia de {self.jugador.nombre} - {self.partido}"

class Tarjeta(models.Model):
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE, related_name='tarjetas')
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='tarjetas')
    minuto = models.IntegerField()
    es_local = models.BooleanField()  # True si la tarjeta es del equipo local
    es_amarilla = models.BooleanField()  # True si es amarilla, False si es roja
    tipo = models.CharField(max_length=20, choices=[
        ('Amarilla', 'Amarilla'),
        ('Roja', 'Roja')
    ], default='Amarilla')

    class Meta:
        ordering = ['minuto']

    def __str__(self):
        return f"{self.tipo} de {self.jugador.nombre} - {self.partido}"

# Modelo para la tabla de transferencias
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
    minutos_jugados = models.IntegerField(default=0)
    tarjetas_amarillas = models.IntegerField(default=0)
    tarjetas_rojas = models.IntegerField(default=0)
    goles_encajados = models.IntegerField(default=0) # Solo para porteros
    goles_de_falta = models.IntegerField(default=0)
    goles_de_penal = models.IntegerField(default=0)

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
    POSICIONES = [('POR', 'Portero'), ('DFC', 'Defensa Central'), ('DFD', 'Defensa Derecho'), ('DFI', 'Defensa Izquierdo'), ('MCD', 'Mediocentro defensivo'), ('MED', 'Mediocampista Derecho'), ('MEI', 'Mediocampista Izquierdo'), ('MEC', 'Mediocampista central'), ('MPC', 'Mediapunta Centro'), ('MPD', 'Mediapunta Derecho'), ('MPI', 'Mediapunta Izquierdo'), ('DLC', 'Delantero Centro'), ('DLD', 'Delantero Derecho'), ('DLI', 'Delantero Izquierdo')]
    
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


    @staticmethod
    def get_or_create_alineacion(equipo, partido):
        alineacion, created = Alineacion.objects.get_or_create(
            equipo=equipo, 
            partido=partido, 
            defaults={
                'nombre': f'Alineación {equipo.nombre} vs {partido.equipo_visitante.nombre if equipo == partido.equipo_local else partido.equipo_local.nombre}'
            }
        )
        return alineacion, created

    def validar_titulares(self, titulares_dict):
        if len(titulares_dict) != 11:
            raise ValueError("Debe haber exactamente 11 jugadores titulares")
        return True

    def actualizar_alineacion(self, titulares_dict, suplentes_list):
        # Validar número de titulares
        self.validar_titulares(titulares_dict)
        
        # Eliminar alineaciones existentes
        self.jugadores_alineacion.all().delete()
        
        # Crear nuevos registros para titulares
        for posicion, jugador_id in titulares_dict.items():
            JugadorAlineacion.objects.create(
                alineacion=self,
                jugador_id=jugador_id,
                posicion=posicion,
                es_titular=True
            )
        
        # Crear nuevos registros para suplentes
        for idx, jugador_id in enumerate(suplentes_list, 1):
            JugadorAlineacion.objects.create(
                alineacion=self,
                jugador_id=jugador_id,
                posicion='SUP',  # Suplente
                es_titular=False,
                numero_suplente=idx
            )

    def __str__(self):
        return f"Alineación {self.nombre} ({self.equipo.nombre}) para {self.partido}"


class JugadorAlineacion(models.Model):
    alineacion = models.ForeignKey(Alineacion, on_delete=models.CASCADE, related_name='jugadores_alineacion')
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE, related_name='alineaciones')
    posicion = models.CharField(max_length=3, choices=Alineacion.POSICIONES)
    es_titular = models.BooleanField(default=True)
    numero_suplente = models.IntegerField(null=True, blank=True)  # Para suplentes (S1, S2, etc.)

    def save(self, *args, **kwargs):
        if self.es_titular:
            # Contar titulares actuales en esta alineación
            titulares_count = JugadorAlineacion.objects.filter(
                alineacion=self.alineacion,
                es_titular=True
            ).exclude(pk=self.pk).count()
            
            if titulares_count >= 11:
                raise ValueError("No pueden haber más de 11 jugadores titulares en una alineación")
        
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('alineacion', 'jugador')
        ordering = ['numero_suplente']
        # Agregar constraints
        constraints = [
            models.CheckConstraint(
                check=models.Q(es_titular=False) | models.Q(numero_suplente__isnull=True),
                name='titular_no_numero_suplente'
            )
        ]

    def __str__(self):
        tipo = "Titular" if self.es_titular else f"Suplente {self.numero_suplente}"
        return f"{self.jugador.nombre} - {self.posicion} ({tipo})"

