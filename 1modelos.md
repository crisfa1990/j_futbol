# Modelos del Proyecto de Gestión de Club de Fútbol

## Índice
- [Modelos del Proyecto de Gestión de Club de Fútbol](#modelos-del-proyecto-de-gestión-de-club-de-fútbol)
  - [Índice](#índice)
  - [Modelo `Patrocinador`](#modelo-patrocinador)
  - [Modelo `Nacionalidad`](#modelo-nacionalidad)
  - [Modelo `Equipo`](#modelo-equipo)
  - [Modelo `Jugador`](#modelo-jugador)
  - [Modelo `Estadio`](#modelo-estadio)
  - [Modelo `Lesion`](#modelo-lesion)
  - [Modelo `Temporada`](#modelo-temporada)
  - [Modelo `Partido`](#modelo-partido)
  - [Modelo `EstadisticaPorTemporada`](#modelo-estadisticaportemporada)
  - [Modelo `Competencia`](#modelo-competencia)
  - [Modelo `Alineacion`](#modelo-alineacion)
  - [Relaciones entre los Modelos](#relaciones-entre-los-modelos)
  - [Orden de Creación de los Registros](#orden-de-creación-de-los-registros)

## Modelo `Patrocinador`
Representa a los patrocinadores que financian a los equipos.

- **Atributos**:
  - `nombre` (CharField): Nombre del patrocinador.
  - `objetivo_basico` (IntegerField): Objetivo básico del patrocinador.
  - `objetivo_extra` (IntegerField): Objetivo extra del patrocinador.

- **Métodos**:
  - `__str__`: Devuelve el nombre del patrocinador.

## Modelo `Nacionalidad`
Representa la nacionalidad de los jugadores y selecciones.

- **Atributos**:
  - `nombre` (CharField): Nombre de la nacionalidad.

- **Métodos**:
  - `__str__`: Devuelve el nombre de la nacionalidad.

## Modelo `Equipo`
Representa a un equipo de fútbol.

- **Atributos**:
  - `nombre` (CharField): Nombre del equipo.
  - `fundacion` (DateField): Fecha de fundación del equipo.
  - `presupuesto` (IntegerField): Presupuesto del equipo.
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
  - `portero` (BooleanField): Indica si el jugador es portero.
  - `habilidades` (JSONField): Habilidades del jugador.
  - `moral` (IntegerField): Moral del jugador.
  - `forma_fisica` (IntegerField): Forma física del jugador.
  - `salario` (IntegerField): Salario del jugador.
  - `lesion` (BooleanField): Indica si el jugador está lesionado.
  - `equipo` (ForeignKey): Relación con el modelo `Equipo`.
  - `nacionalidad` (ForeignKey): Relación con el modelo `Nacionalidad`.
  - `goles_carrera` (IntegerField): Goles en la carrera del jugador.
  - `asistencias_carrera` (IntegerField): Asistencias en la carrera del jugador.
  - `partidos_carrera` (IntegerField): Partidos jugados en la carrera del jugador.
  - `partidos_internacionales` (IntegerField): Partidos internacionales jugados.
  - `goles_internacionales` (IntegerField): Goles internacionales marcados.
  - `asistencias_internacionales` (IntegerField): Asistencias internacionales realizadas.

- **Métodos**:
  - `__str__`: Devuelve el nombre del jugador.

## Modelo `Estadio`
Representa un estadio de fútbol.

- **Atributos**:
  - `nombre` (CharField): Nombre del estadio.
  - `nivel` (IntegerField): Nivel del estadio.
  - `capacidad` (IntegerField): Capacidad del estadio.
  - `equipo` (OneToOneField): Relación con el modelo `Equipo`.
  - `mantenimiento` (IntegerField): Costo de mantenimiento del estadio.

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
  - `espectadores` (IntegerField): Número de espectadores del partido.
  - `clima` (CharField): Clima durante el partido.

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
  - `bono_por_partido` (IntegerField): Bono por partido.
  - `bono_por_titulo` (IntegerField): Bono por título.
  - `bono_por_victoria` (IntegerField): Bono por victoria.
  - `bono_por_clasificacion` (IntegerField): Bono por clasificación.
  - `sistema_puntos` (JSONField): Sistema de puntos de la competencia.
  - `fases` (JSONField): Fases de la competencia.
  - `trofeo` (BooleanField): Indica si la competencia tiene un trofeo asociado.

- **Métodos**:
  - `__str__`: Devuelve el nombre de la competencia.
  - `esta_disponible`: Verifica si la competencia está disponible en una fecha específica.
  - `calcular_inversion_total`: Calcula la inversión total en la competencia.

## Modelo `Alineacion`
Representa una alineación de un equipo para un partido específico.

- **Atributos**:
  - `nombre` (CharField): Nombre de la alineación.
  - `fecha_creacion` (DateTimeField): Fecha de creación de la alineación.
  - `fecha_actualizacion` (DateTimeField): Fecha de última actualización de la alineación.
  - `equipo` (ForeignKey): Relación con el modelo `Equipo`.
  - `partido` (ForeignKey): Relación con el modelo `Partido`.
  - `titulares` (JSONField): Lista de IDs de jugadores titulares.
  - `suplentes` (JSONField): Lista de IDs de jugadores suplentes.
  - `estilo_pases` (CharField): Estilo de pases del equipo.
  - `actitud` (CharField): Actitud del equipo.
  - `entradas` (CharField): Tipo de entradas del equipo.
  - `marcaje` (CharField): Tipo de marcaje del equipo.
  - `presion` (CharField): Tipo de presión del equipo.

- **Métodos**:
  - `__str__`: Devuelve el nombre de la alineación.
  - `get_or_create_alineacion`: Obtiene o crea una alineación para un equipo y partido específicos.
  - `actualizar_alineacion`: Actualiza la alineación con nuevos titulares y suplentes.

## Relaciones entre los Modelos
- **Patrocinador** y **Equipo**: Relación de uno a muchos. Un patrocinador puede financiar varios equipos.
- **Nacionalidad** y **Equipo**: Relación de uno a muchos. Una nacionalidad puede tener varios equipos.
- **Nacionalidad** y **Jugador**: Relación de uno a muchos. Una nacionalidad puede tener varios jugadores.
- **Equipo** y **Jugador**: Relación de uno a muchos. Un equipo puede tener varios jugadores.
- **Equipo** y **Estadio**: Relación de uno a uno. Un equipo tiene un estadio.
- **Jugador** y **Lesion**: Relación de uno a muchos. Un jugador puede tener varias lesiones.
- **Equipo** y **Competencia**: Relación de muchos a muchos. Un equipo puede participar en varias competencias y una competencia puede tener varios equipos.
- **Temporada** y **Competencia**: Relación de uno a muchos. Una temporada puede tener varias competencias.
- **Temporada** y **Partido**: Relación de uno a muchos. Una temporada puede tener varios partidos.
- **Competencia** y **Partido**: Relación de uno a muchos. Una competencia puede tener varios partidos.
- **Equipo** y **Partido**: Relación de uno a muchos. Un equipo puede tener varios partidos como local y varios partidos como visitante.
- **Estadio** y **Partido**: Relación de uno a muchos. Un estadio puede tener varios partidos.
- **Jugador** y **EstadisticaPorTemporada**: Relación de uno a muchos. Un jugador puede tener varias estadísticas por temporada.
- **Temporada** y **EstadisticaPorTemporada**: Relación de uno a muchos. Una temporada puede tener varias estadísticas por temporada.
- **Equipo** y **EstadisticaPorTemporada**: Relación de uno a muchos. Un equipo puede tener varias estadísticas por temporada.

## Orden de Creación de los Registros
1. Crear registros de `Nacionalidad`.
2. Crear registros de `Patrocinador`.
3. Crear registros de `Equipo` vinculados a `Nacionalidad` y `Patrocinador`.
4. Crear registros de `Estadio` vinculados a `Equipo`.
5. Crear registros de `Jugador` vinculados a `Equipo` y `Nacionalidad`.
6. Crear registros de `Temporada`.
7. Crear registros de `Competencia` vinculados a `Temporada` y `Nacionalidad`.
8. Vincular `Equipo` a `Competencia`.
9. Crear registros de `Partido` vinculados a `Equipo`, `Competencia`, `Temporada` y `Estadio`.
10. Crear registros de `Lesion` vinculados a `Jugador`.
11. Crear registros de `EstadisticaPorTemporada` vinculados a `Jugador`, `Temporada` y `Equipo`.
12. Crear registros de `Alineacion` vinculados a `Equipo` y `Partido`.