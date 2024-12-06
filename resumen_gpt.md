# Planificación del Juego de Gestión de Club de Fútbol

## 1. Modelos Actualizados

### Jugador
- **Atributos**:
  - `nombre`: (CharField) Nombre del jugador.
  - `nacionalidad`: (ForeignKey) Relación con el modelo `Nacionalidad`.
  - `habilidades`: (JSONField) Un diccionario que contiene todas las habilidades del jugador (defensa, ataque, pases, etc.).
  - `goles_carrera`: (IntegerField) Total de goles en toda la carrera.
  - `goles_temporada`: (IntegerField) Goles marcados en la temporada actual.
  - `goles_club`: (IntegerField) Goles marcados en el club actual.
  - `asistencias_carrera`: (IntegerField) Total de asistencias en toda la carrera.
  - `asistencias_temporada`: (IntegerField) Asistencias en la temporada actual.
  - `asistencias_club`: (IntegerField) Asistencias en el club actual.
  - `partidos_carrera`: (IntegerField) Total de partidos jugados en la carrera.
  - `partidos_temporada`: (IntegerField) Partidos jugados en la temporada actual.
  - `partidos_club`: (IntegerField) Partidos jugados en el club actual.
  - `lesionado`: (BooleanField) Indica si el jugador está lesionado.
  - `lesion`: (ForeignKey) Relación con el modelo `Lesion`, si aplica.

### Lesion
- **Atributos**:
  - `tipo`: (CharField) Tipo de lesión (e.g., rotura de ligamentos, esguince).
  - `tiempo_recuperacion`: (IntegerField) Tiempo estimado en días para la recuperación.
  - `fecha_inicio`: (DateField) Fecha en que comenzó la lesión.
  - `fecha_fin`: (DateField) Fecha en que se espera que termine la recuperación.

### Temporada
- **Atributos**:
  - `año`: (IntegerField) Año de la temporada (por ejemplo, 2024-2025).
  - `inicio`: (DateField) Fecha de inicio de la temporada.
  - `fin`: (DateField) Fecha de finalización de la temporada.
  - `equipos`: (ManyToManyField) Relación con los equipos que participan en la temporada.

### Copa Nacional
- **Atributos**:
  - `nombre`: (CharField) Nombre de la copa.
  - `temporada`: (ForeignKey) Relación con el modelo `Temporada`.
  - `equipos`: (ManyToManyField) Equipos que participan en la copa.

### Copa Internacional
- **Atributos**:
  - `nombre`: (CharField) Nombre de la copa.
  - `temporada`: (ForeignKey) Relación con el modelo `Temporada`.
  - `selecciones`: (ManyToManyField) Selecciones que participan en la copa.

### Selección Nacional
- **Atributos**:
  - `nombre`: (CharField) Nombre de la selección.
  - `nacionalidad`: (ForeignKey) Relación con el modelo `Nacionalidad`.
  - `jugadores`: (ManyToManyField) Jugadores que forman parte de la selección.
  - `entrenador`: (ForeignKey) Relación con el modelo `Entrenador`.

### Entrenador
- **Atributos**:
  - `nombre`: (CharField) Nombre del entrenador.
  - `equipo`: (OneToOneField) Relación con el modelo `Equipo`, cada equipo tiene un entrenador asignado.

---

## 2. Relaciones Entre Modelos

- **Jugador y Equipo**: Relación de muchos a muchos, un jugador puede estar en varios equipos y un equipo tiene varios jugadores.
- **Jugador y Nacionalidad**: Relación de uno a muchos, un jugador pertenece a una sola nacionalidad.
- **Equipo y Temporada**: Relación de uno a muchos, un equipo tiene varias temporadas, pero cada temporada corresponde a un solo equipo.
- **Equipo y Entrenador**: Relación de uno a uno, cada equipo tiene un solo entrenador.
- **Equipo y Patrocinador**: Relación de uno a muchos, un patrocinador puede tener varios equipos asociados.
- **Jugador y Lesión**: Relación de uno a muchos, un jugador puede estar lesionado, y cada lesión pertenece a un solo jugador.
- **Copa Nacional y Equipo**: Relación de muchos a muchos, varios equipos participan en una copa nacional.
- **Copa Internacional y Selección**: Relación de muchos a muchos, varias selecciones participan en una copa internacional.
- **Selección y Nacionalidad**: Relación de uno a muchos, una selección está asociada a una sola nacionalidad.

---

## 3. Funcionalidades del Sistema

### **Simulación de Partidos**

- **Descripción**: El sistema simula partidos entre equipos o selecciones, basándose en las habilidades de los jugadores. Cada jugador tendrá un conjunto de habilidades (por ejemplo, ataque, defensa, pase, etc.) que influirá en los eventos del partido.
  
- **Relación con los Modelos**:
  - Los **jugadores** tienen habilidades que se utilizan durante los partidos. Por ejemplo, los **defensores** y **porteros** priorizan habilidades defensivas y de mentalidad, mientras que los **delanteros** priorizan remate y desmarque.
  - Cada **partido** involucrará un conjunto de jugadores, y sus **habilidades** afectarán los resultados.
  - La **lesión** de un jugador puede afectar su participación en el partido y su rendimiento.
  - Los **entrenadores** pueden influir en la táctica de los equipos, optimizando el rendimiento de los jugadores según sus habilidades.
  - Las **estadísticas de goles, asistencias y partidos jugados** de los jugadores se actualizarán tras cada partido.

### **Entrenamiento de Jugadores**

- **Descripción**: Los jugadores pueden mejorar sus habilidades mediante entrenamientos programados. Estos entrenamientos se pueden personalizar para enfocarse en áreas específicas (pases, defensa, ataque, etc.).
  
- **Relación con los Modelos**:
  - Los **jugadores** tienen atributos de habilidades que pueden incrementarse mediante entrenamientos. Por ejemplo, un jugador podría mejorar su habilidad de pase o defensa a través de entrenamiento específico.
  - Un **entrenador** tiene la capacidad de gestionar los entrenamientos y asignar prioridades según las necesidades del equipo.
  - Las **lesiones** también pueden influir en la capacidad de un jugador para entrenar, por lo que el sistema debe gestionar los jugadores lesionados con tiempos de recuperación.
  - Las **estadísticas de jugadores** se actualizan según los avances durante el entrenamiento.

### **Estadísticas de Jugadores**

- **Descripción**: Los jugadores tienen estadísticas detalladas, que incluyen goles marcados en su carrera, en la temporada actual y en el club. Lo mismo para asistencias y partidos jugados.
  
- **Relación con los Modelos**:
  - Los **jugadores** tienen atributos de goles, asistencias y partidos jugados, los cuales se actualizan después de cada partido o competición.
  - Las **estadísticas de jugadores** se utilizan para determinar el rendimiento de un jugador a lo largo del tiempo, y su impacto en el equipo.
  - Los **partidos** jugados influirán directamente en estas estadísticas. Los goles y asistencias se sumarán tanto en la temporada como en el club.

### **Lesiones de Jugadores**

- **Descripción**: Los jugadores pueden sufrir lesiones durante los entrenamientos o partidos, lo que afectará su rendimiento y su disponibilidad para los partidos.
  
- **Relación con los Modelos**:
  - Un **jugador** puede estar relacionado con un **modelo de lesión**. Cada lesión tendrá un tipo (ej. esguince, rotura de ligamentos) y una duración estimada.
  - Si un jugador está lesionado, su **estado físico** se reflejará en las simulaciones de los partidos, lo que afectará su rendimiento.
  - Los **entrenadores** gestionan los jugadores lesionados y sus tiempos de recuperación, lo cual puede afectar las alineaciones y las tácticas durante los partidos.
  - Las **estadísticas** de los jugadores también se ven afectadas por las lesiones, ya que un jugador lesionado no podrá participar en los partidos y su rendimiento se verá limitado.

### **Transferencias de Jugadores**

- **Descripción**: Los jugadores pueden ser transferidos entre equipos, basándose en su rendimiento, el estado de su contrato y las necesidades del equipo.
  
- **Relación con los Modelos**:
  - Un **jugador** tiene un equipo actual y puede ser transferido a otro equipo. La **transacción** dependerá de las negociaciones entre equipos, con influencias de las **habilidades** del jugador, sus **estadísticas** y su valor de mercado.
  - Los **equipos** tienen un presupuesto limitado para realizar transferencias, y los **entrenadores** toman decisiones sobre las necesidades del equipo.
  - Las **lesiones** pueden afectar la capacidad de los jugadores para ser transferidos. Un jugador lesionado puede tener su valor de mercado reducido.

### **Competiciones y Copas**

- **Descripción**: Se simulan competiciones entre equipos y selecciones, como copas nacionales e internacionales, donde se determinan los campeones a través de partidos.