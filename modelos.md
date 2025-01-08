# Modelos del Proyecto de Gestión de Club de Fútbol

## Modelo `Patrocinador`
Representa a los patrocinadores que financian a los equipos.

- **Atributos**:
  - `nombre` (CharField): Nombre del patrocinador.
  - `presupuesto` (IntegerField): Presupuesto del patrocinador.

- **Métodos**:
  - `__str__`: Devuelve el nombre del patrocinador.

## Modelo `Equipo`
Representa a un equipo de fútbol.

- **Atributos**:
  - `nombre` (CharField): Nombre del equipo.
  - `fundacion` (DateField): Fecha de fundación del equipo.
  - `presupuesto` (DecimalField): Presupuesto del equipo.
  - `nacionalidad` (ForeignKey): Relación con el modelo `Nacionalidad`.
  - `patrocinador` (ForeignKey): Relación con el modelo `Patrocinador`.
  - `competencias` (ManyToManyField): Relación con el modelo `Competencia`.
  - `goles_favor` (IntegerField): Goles a favor del equipo.
  - `goles_contra` (IntegerField): Goles en contra del equipo.
  - `asistencias` (IntegerField): Asistencias del equipo.
  - `partidos_jugados` (IntegerField): Partidos jugados por el equipo.

- **Métodos**:
  - `__str__`: Devuelve el nombre del equipo.

## Modelo `Jugador`
Representa a un jugador de fútbol.

- **Atributos**:
  - `nombre` (CharField): Nombre del jugador.
  - `edad` (IntegerField): Edad del jugador.
  - `habilidades` (JSONField): Habilidades del jugador.
  - `moral` (IntegerField): Moral del jugador.
  - `salario` (DecimalField): Salario del jugador.
  - `lesion` (BooleanField): Indica si el jugador está lesionado.
  - `equipo` (ForeignKey): Relación con el modelo `Equipo`.
  - `nacionalidad` (ForeignKey): Relación con el modelo `Nacionalidad`.
  - `goles_carrera` (IntegerField): Goles en la carrera del jugador.
  - `asistencias_carrera` (IntegerField): Asistencias en la carrera del jugador.
  - `partidos_carrera` (IntegerField): Partidos jugados en la carrera del jugador.

- **Métodos**:
  - `__str__`: Devuelve el nombre del jugador.

## Modelo `Estadio`
Representa un estadio de fútbol.

- **Atributos**:
  - `nombre` (CharField): Nombre del estadio.
  - `nivel` (IntegerField): Nivel del estadio.
  - `capacidad` (IntegerField): Capacidad del estadio.

- **Métodos**:
  - `__str__`: Devuelve el nombre del estadio.

## Modelo `Lesion`
Representa una lesión de un jugador.

- **Atributos**:
  - `jugador` (ForeignKey): Relación con el modelo `Jugador`.
  - `fecha_inicio` (DateField): Fecha de inicio de la lesión.
  - `fecha_fin` (DateField): Fecha de fin de la lesión.
  - `tipo` (CharField): Tipo de lesión.
  - `impacto` (IntegerField): Impacto de la lesión en las habilidades del jugador.

- **Métodos**:
  - `__str__`: Devuelve el tipo de lesión y el nombre del jugador.

## Modelo `Temporada`
Representa una temporada de fútbol.

- **Atributos**:
  - `anio` (IntegerField): Año de la temporada.
  - `fecha_inicio` (DateTimeField): Fecha de inicio de la temporada.
  - `fecha_fin` (DateTimeField): Fecha de fin de la temporada.

- **Métodos**:
  - `__str__`: Devuelve el año de la temporada.

## Modelo `Partido`
Representa un partido de fútbol.

- **Atributos**:
  - `fecha` (DateField): Fecha del partido.
  - `equipo_local` (ForeignKey): Relación con el modelo `Equipo` (equipo local).
  - `equipo_visitante` (ForeignKey): Relación con el modelo `Equipo` (equipo visitante).
  - `competencia` (ForeignKey): Relación con el modelo `Competencia`.
  - `temporada` (ForeignKey): Relación con el modelo `Temporada`.
  - `estadio` (ForeignKey): Relación con el modelo `Estadio`.
  - `goles_local` (IntegerField): Goles del equipo local.
  - `goles_visitante` (IntegerField): Goles del equipo visitante.
  - `goles_jugadores_local` (JSONField): Goles de los jugadores del equipo local.
  - `goles_jugadores_visitante` (JSONField): Goles de los jugadores del equipo visitante.
  - `asistencias_jugadores_local` (JSONField): Asistencias de los jugadores del equipo local.
  - `asistencias_jugadores_visitante` (JSONField): Asistencias de los jugadores del equipo visitante.

- **Métodos**:
  - `__str__`: Devuelve una cadena con los nombres de los equipos y la competencia.

## Modelo `EstadisticaPorTemporada`
Representa las estadísticas de un jugador por temporada.

- **Atributos**:
  - `jugador` (ForeignKey): Relación con el modelo `Jugador`.
  - `temporada` (ForeignKey): Relación con el modelo `Temporada`.
  - `equipo` (ForeignKey): Relación con el modelo `Equipo`.
  - `goles` (IntegerField): Goles del jugador en la temporada.
  - `asistencias` (IntegerField): Asistencias del jugador en la temporada.
  - `partidos` (IntegerField): Partidos jugados por el jugador en la temporada.

- **Métodos**:
  - `__str__`: Devuelve una cadena con el nombre del jugador y el año de la temporada.

## Modelo `Competencia`
Representa una competencia de fútbol.

- **Atributos**:
  - `nombre` (CharField): Nombre de la competencia.
  - `tipo` (CharField): Tipo de competencia.
  - `temporada` (ForeignKey): Relación con el modelo `Temporada`.
  - `equipos` (ManyToManyField): Equipos participantes en la competencia.
  - `nacionalidad` (OneToOneField): Relación con el modelo `Nacionalidad`.
  - `fecha_inicio` (DateField): Fecha de inicio de la competencia.
  - `fecha_fin` (DateField): Fecha de fin de la competencia.

- **Métodos**:
  - `__str__`: Devuelve el nombre de la competencia.

## Modelo `Nacionalidad`
Representa la nacionalidad de los jugadores y selecciones.

- **Atributos**:
  - `nombre` (CharField): Nombre de la nacionalidad.

- **Métodos**:
  - `__str__`: Devuelve el nombre de la nacionalidad.