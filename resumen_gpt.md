# Planificación Detallada del Juego de Gestión de Club de Fútbol

## Índice

1. [Modelos Actualizados](#1-modelos-actualizados)
    - [Jugador](#jugador)
    - [Lesión](#lesión)
    - [Temporada](#temporada)
    - [Copa Nacional](#copa-nacional)
    - [Copa Internacional](#copa-internacional)
    - [Selección Nacional](#selección-nacional)
    - [Entrenador](#entrenador)
    - [Liga Juvenil](#liga-juvenil)
2. [Relaciones Entre Modelos](#2-relaciones-entre-modelos)
3. [Funcionalidades del Sistema](#3-funcionalidades-del-sistema)
    - [Desarrollo de Jugadores Juveniles](#31-desarrollo-de-jugadores-juveniles)
    - [Cálculo del Sueldo de los Jugadores](#32-cálculo-del-sueldo-de-los-jugadores)
    - [Lesiones de Jugadores](#33-lesiones-de-jugadores)
    - [Simulación de Partidos y Resultados](#34-simulación-de-partidos-y-resultados)
4. [Desarrollo y Planificación para el Juego](#4-desarrollo-y-planificación-para-el-juego)

---

## 1. Modelos Actualizados

### **Jugador**
- **Atributos**:
  - `nombre`: (CharField) Nombre completo del jugador.
  - `nacionalidad`: (ForeignKey) Relación con el modelo `Nacionalidad`, representa la nacionalidad del jugador.
  - `habilidades`: (JSONField) Un diccionario con las habilidades clave del jugador, como `defensa`, `ataque`, `pases`, `remate`, etc.
  - `goles_carrera`: (IntegerField) Goles marcados en su carrera profesional.
  - `goles_temporada`: (IntegerField) Goles marcados en la temporada actual.
  - `goles_club`: (IntegerField) Goles marcados con el club actual.
  - `asistencias_carrera`: (IntegerField) Total de asistencias en su carrera profesional.
  - `asistencias_temporada`: (IntegerField) Asistencias realizadas en la temporada actual.
  - `asistencias_club`: (IntegerField) Asistencias realizadas en el club actual.
  - `partidos_carrera`: (IntegerField) Número total de partidos jugados en su carrera.
  - `partidos_temporada`: (IntegerField) Partidos jugados en la temporada actual.
  - `partidos_club`: (IntegerField) Partidos jugados en el club actual.
  - `lesionado`: (BooleanField) Indica si el jugador está lesionado.
  - `lesion`: (ForeignKey) Relación con el modelo `Lesion` que describe los detalles de la lesión.
  - `edad`: (IntegerField) Edad actual del jugador, calculada en función de su fecha de nacimiento.
  - `moral`: (IntegerField) Nivel de moral del jugador (escala de 1 a 100).
  - `sueldo`: (IntegerField) Sueldo del jugador calculado en base a su nivel de habilidades, moral y liderazgo.
  - `liderazgo`: (IntegerField) Habilidad entrenable que refleja la capacidad del jugador para liderar, tanto en el campo como fuera de él (escala de 1 a 100).
  - `media`: (FloatField) Media de las habilidades del jugador (promedio de todas las habilidades clave).
  - `jugador_juvenil`: (BooleanField) Indica si el jugador es parte del equipo juvenil.
  - `jugador_primer_equipo`: (BooleanField) Indica si el jugador ha sido ascendido o pertenece al primer equipo.

### **Lesión**
- **Atributos**:
  - `tipo`: (CharField) Tipo de lesión sufrida (por ejemplo, "esguince", "fractura", "contractura").
  - `tiempo_recuperacion`: (IntegerField) Duración de la recuperación en días.
  - `fecha_inicio`: (DateField) Fecha en la que ocurrió la lesión.
  - `fecha_fin`: (DateField) Fecha estimada en la que el jugador podrá regresar a la acción.

---

## 2. Relaciones Entre Modelos

- **Jugador y Equipo**: Relación de muchos a muchos, un jugador puede pertenecer a varios equipos (por ejemplo, transferencias entre equipos, cesiones), pero cada equipo tiene varios jugadores.
- **Jugador y Nacionalidad**: Relación de uno a muchos, un jugador tiene una nacionalidad, y una nacionalidad puede tener varios jugadores.
- **Jugador y Lesión**: Relación de uno a muchos, cada jugador puede tener varias lesiones a lo largo de su carrera.
- **Jugador y Moral, Sueldo, Liderazgo**: Los atributos de moral, sueldo y liderazgo están vinculados al rendimiento y comportamiento del jugador.
- **Jugador y Liga Juvenil**: Relación de muchos a muchos. Los jugadores juveniles forman parte de la liga juvenil, pero solo pueden ascender al primer equipo cuando cumplen con ciertos requisitos, como tener una media de habilidades adecuada y un rendimiento sobresaliente.
- **Equipo y Temporada**: Relación de uno a muchos, un equipo participa en una temporada específica, y cada temporada tiene varios equipos.

---

## 3. Funcionalidades del Sistema

### 3.1 Desarrollo de Jugadores Juveniles

- **Descripción**: El sistema de desarrollo juvenil está diseñado para entrenar a jugadores menores de 20 años...

- **Cálculos y Reglas de Ascenso**:
  - **Edad del Jugador**: Los jugadores deben tener entre 16 y 19 años...

...

---

## 4. Desarrollo y Planificación para el Juego

### **Base de Datos**
Es fundamental contar con una base de datos bien estructurada...

### **Optimización**
Los cálculos en tiempo real serán importantes para...


# Planificación Detallada del Juego de Gestión de Club de Fútbol

## 1. Modelos Actualizados

### **Jugador**
- **Atributos**:
  - `nombre`: (CharField) Nombre completo del jugador.
  - `nacionalidad`: (ForeignKey) Relación con el modelo `Nacionalidad`, representa la nacionalidad del jugador.
  - `habilidades`: (JSONField) Un diccionario con las habilidades clave del jugador, como `defensa`, `ataque`, `pases`, `remate`, etc.
  - `goles_carrera`: (IntegerField) Goles marcados en su carrera profesional.
  - `goles_temporada`: (IntegerField) Goles marcados en la temporada actual.
  - `goles_club`: (IntegerField) Goles marcados con el club actual.
  - `asistencias_carrera`: (IntegerField) Total de asistencias en su carrera profesional.
  - `asistencias_temporada`: (IntegerField) Asistencias realizadas en la temporada actual.
  - `asistencias_club`: (IntegerField) Asistencias realizadas en el club actual.
  - `partidos_carrera`: (IntegerField) Número total de partidos jugados en su carrera.
  - `partidos_temporada`: (IntegerField) Partidos jugados en la temporada actual.
  - `partidos_club`: (IntegerField) Partidos jugados en el club actual.
  - `lesionado`: (BooleanField) Indica si el jugador está lesionado.
  - `lesion`: (ForeignKey) Relación con el modelo `Lesion` que describe los detalles de la lesión.
  - `edad`: (IntegerField) Edad actual del jugador, calculada en función de su fecha de nacimiento.
  - `moral`: (IntegerField) Nivel de moral del jugador (escala de 1 a 100).
  - `sueldo`: (IntegerField) Sueldo del jugador calculado en base a su nivel de habilidades, moral y liderazgo.
  - `liderazgo`: (IntegerField) Habilidad entrenable que refleja la capacidad del jugador para liderar, tanto en el campo como fuera de él (escala de 1 a 100).
  - `media`: (FloatField) Media de las habilidades del jugador (promedio de todas las habilidades clave).
  - `jugador_juvenil`: (BooleanField) Indica si el jugador es parte del equipo juvenil.
  - `jugador_primer_equipo`: (BooleanField) Indica si el jugador ha sido ascendido o pertenece al primer equipo.

### **Lesion**
- **Atributos**:
  - `tipo`: (CharField) Tipo de lesión sufrida (por ejemplo, "esguince", "fractura", "contractura").
  - `tiempo_recuperacion`: (IntegerField) Duración de la recuperación en días.
  - `fecha_inicio`: (DateField) Fecha en la que ocurrió la lesión.
  - `fecha_fin`: (DateField) Fecha estimada en la que el jugador podrá regresar a la acción.

### **Temporada**
- **Atributos**:
  - `año`: (IntegerField) Año de la temporada (por ejemplo, 2024).
  - `inicio`: (DateField) Fecha de inicio de la temporada.
  - `fin`: (DateField) Fecha de fin de la temporada.
  - `equipos`: (ManyToManyField) Equipos participantes en la temporada (relación con el modelo `Equipo`).

### **Copa Nacional**
- **Atributos**:
  - `nombre`: (CharField) Nombre de la copa nacional.
  - `temporada`: (ForeignKey) Relación con el modelo `Temporada`.
  - `equipos`: (ManyToManyField) Equipos participantes en la copa nacional.

### **Copa Internacional**
- **Atributos**:
  - `nombre`: (CharField) Nombre de la copa internacional.
  - `temporada`: (ForeignKey) Relación con el modelo `Temporada`.
  - `selecciones`: (ManyToManyField) Selecciones participantes en la copa internacional.

### **Selección Nacional**
- **Atributos**:
  - `nombre`: (CharField) Nombre de la selección nacional.
  - `nacionalidad`: (ForeignKey) Relación con el modelo `Nacionalidad`.
  - `jugadores`: (ManyToManyField) Jugadores que forman parte de la selección.
  - `entrenador`: (ForeignKey) Relación con el modelo `Entrenador`.

### **Entrenador**
- **Atributos**:
  - `nombre`: (CharField) Nombre del entrenador.
  - `equipo`: (OneToOneField) Relación con el modelo `Equipo`.
  - `experiencia`: (IntegerField) Años de experiencia del entrenador.
  - `tacticas`: (JSONField) Estrategias o tácticas del entrenador.

### **Liga Juvenil**
- **Atributos**:
  - `nombre`: (CharField) Nombre de la liga juvenil.
  - `equipos`: (ManyToManyField) Equipos que participan en la liga juvenil.
  - `temporada`: (ForeignKey) Relación con el modelo `Temporada`, que indica a qué temporada pertenece la liga.

---

## 2. Relaciones Entre Modelos

- **Jugador y Equipo**: Relación de muchos a muchos, un jugador puede pertenecer a varios equipos (por ejemplo, transferencias entre equipos, cesiones), pero cada equipo tiene varios jugadores.
- **Jugador y Nacionalidad**: Relación de uno a muchos, un jugador tiene una nacionalidad, y una nacionalidad puede tener varios jugadores.
- **Jugador y Lesión**: Relación de uno a muchos, cada jugador puede tener varias lesiones a lo largo de su carrera.
- **Jugador y Moral, Sueldo, Liderazgo**: Los atributos de moral, sueldo y liderazgo están vinculados al rendimiento y comportamiento del jugador.
- **Jugador y Liga Juvenil**: Relación de muchos a muchos. Los jugadores juveniles forman parte de la liga juvenil, pero solo pueden ascender al primer equipo cuando cumplen con ciertos requisitos, como tener una media de habilidades adecuada y un rendimiento sobresaliente.
- **Equipo y Temporada**: Relación de uno a muchos, un equipo participa en una temporada específica, y cada temporada tiene varios equipos.
- **Liga Juvenil y Temporada**: Relación de muchos a muchos, varias ligas juveniles pueden tener lugar en una temporada, y un equipo juvenil puede participar en múltiples ligas juveniles.
- **Jugador y Primer Equipo**: Relación de uno a muchos, un jugador juvenil solo puede pertenecer al primer equipo si cumple con los requisitos de rendimiento, habilidades y edad.

---

## 3. Funcionalidades del Sistema

### 3.1 **Desarrollo de Jugadores Juveniles**
  
- **Descripción**: El sistema de desarrollo juvenil está diseñado para entrenar a jugadores menores de 20 años, quienes no pueden jugar en el primer equipo a menos que sean ascendidos. Los jugadores juveniles tienen un límite de edad entre los 16 y los 19 años, y no pueden tener habilidades superiores a 70 en ningún atributo. Cuando un jugador alcanza los 20 años, automáticamente se ascenderá al primer equipo. 

##### **Cálculos y Reglas de Ascenso**:
  - **Edad del Jugador**: Los jugadores de la liga juvenil deben tener entre 16 y 19 años, si superan los 19 años y 365 días, serán automáticamente ascendidos al primer equipo.
  - **Requisitos para Ascender**:
    - **Edad**: Al cumplir 20 años, el jugador se traslada automáticamente al primer equipo.
    - **Habilidades**: La media de las habilidades no puede superar 70. Si un jugador tiene alguna habilidad superior a 70, no podrá formar parte del equipo juvenil.
    - **Ascenso**: Cuando un jugador cumple 20 años, independientemente de su habilidad media, debe ser ascendido al primer equipo. 

- **Relación con los Modelos**:
  - **Jugador**: Los jugadores juveniles son parte de la liga juvenil. Tienen una edad, media y habilidades limitadas. 
  - **Liga Juvenil**: Los jugadores juveniles juegan en esta liga y desarrollan sus habilidades. Si son buenos, pueden ser ascendidos al primer equipo.
  - **Ascenso Automático**: Cuando un jugador cumple 20 años, pasa al primer equipo automáticamente. La condición es que haya tenido un rendimiento adecuado en la liga juvenil.

- **Ascenso de Juveniles**: Cuando un jugador alcanza los 20 años o su habilidad media supera los 70, debe ser ascendido al primer equipo.
  
- **Condiciones de los Juveniles**:
  - Edad entre **16 años** y **19 años 365 días**.
  - Habilidad media máxima de **70**.
  - Ninguna habilidad puede superar **70**.

#### **Evolución de los Juveniles**:
  - Los juveniles tendrán una evolución anual de sus habilidades, dependiendo de su entrenamiento y partidos jugados.
  - Las habilidades no podrán superar 70 hasta ser ascendido al primer equipo.
  - Los jugadores en la liga juvenil tendrán un sueldo menor en comparación con los jugadores del primer equipo.

#### **Modelo de Liga Juvenil**:

```python
class Juvenil(models.Model):
    jugador = models.OneToOneField(Jugador, on_delete=models.CASCADE)
    edad = models.IntegerField()
    habilidad_media = models.IntegerField()
    habilidades_maximas = models.JSONField()
    en_primer_equipo = models.BooleanField(default=False)
    
    def actualizar_edad(self):
        # Se actualiza la edad del jugador de acuerdo al año en curso
        self.edad += 1
    
    def verificar_ascenso(self):
        if self.edad >= 20 or self.habilidad_media > 70:
            self.en_primer_equipo = True
            self.save()
```

### 3.2 **Cálculo del Sueldo de los Jugadores**
  
- **Descripción**: El sueldo de los jugadores se calcula en base a su rendimiento general, habilidades, moral y liderazgo. A medida que un jugador aumenta su rendimiento y habilidades, su sueldo incrementará.

#### **Cálculo**:
- El sueldo se calcula de la siguiente forma:
  - **Base**: Sueldo base según el club.
  - **Habilidad Media**: Un porcentaje de su habilidad media influirá en el sueldo.
  - **Moral**: La moral también afectará el sueldo (si la moral es baja, el sueldo será más bajo).
  - **Liderazgo**: Un jugador con alto liderazgo recibirá un bono extra al sueldo.
  

Donde:
- **Factor Habilidad**: Coeficiente que multiplica la media de habilidades (por ejemplo, 100).
- **Factor Moral**: Coeficiente para la moral (por ejemplo, 50).
- **Factor Liderazgo**: Coeficiente para el liderazgo (por ejemplo, 200).

### 3.3 **Lesiones de Jugadores**

- **Descripción**: Los jugadores pueden lesionarse durante los entrenamientos o partidos, lo que afectará su rendimiento. Cada lesión tendrá una duración específica, y el jugador no podrá jugar hasta recuperarse completamente.

#### **Relación con el Modelo de Lesión**:
- Cada jugador tiene un campo de `lesionado`, que será `True` si está lesionado.
- La lesión está vinculada a un modelo `Lesion`, que contiene información sobre el tipo de lesión y la duración de la recuperación.

#### **Cálculo**:
- Si el jugador se lesiona, se registra la fecha de inicio de la lesión y la duración.
- Los jugadores lesionados no pueden participar en partidos hasta que se recuperen.

## **Impacto de las Lesiones**:

   Las lesiones afectarán temporalmente las habilidades de los jugadores. El jugador lesionado tendrá una penalización en sus habilidades de acuerdo con la gravedad de la lesión, que puede variar dependiendo del tipo de lesión. Ejemplo de cálculo:
   ```python
   Penalización Habilidad = Habilidad * (1 - % Lesión)

```

### **Modelo de Lesión**:

```python
class Lesion(models.Model):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)  # Ejemplo: "Distensión muscular", "Rotura de ligamento"
    gravedad = models.IntegerField()  # Escala del 1 al 10
    duracion_dias = models.IntegerField()  # Duración estimada de la lesión
    fecha_inicio = models.DateField(auto_now_add=True)

    def aplicar_lesion(self):
        # Reduce las habilidades en función de la gravedad
        self.jugador.habilidad_media -= (self.gravedad * 2)
        self.jugador.save()

    def curar(self):
        # Restaura las habilidades al nivel original
        self.jugador.habilidad_media += (self.gravedad * 2)
        self.jugador.save()
```

### **Desarrollo y Planificación para el Juego**

- **Base de Datos**: Es fundamental crear relaciones eficientes entre jugadores, equipos, ligas y competiciones. Las relaciones `Many-to-Many`, `ForeignKey` y `OneToOneField` deben ser correctamente implementadas para asegurar la integridad de los datos.

- **Cálculos en Tiempo Real**: Los sueldos, moral y habilidades de los jugadores se actualizarán constantemente según el rendimiento, las lesiones y los entrenamientos. La fórmula de cálculo debe ser eficiente, y las actualizaciones se realizarán al final de cada temporada o cuando un jugador alcance un nuevo nivel de habilidad o moral.

- **Interfaz de Usuario**: La aplicación debe ofrecer una interfaz clara para gestionar jugadores, equipos, ligas y competiciones. Además, debe permitir la simulación de partidos y el seguimiento del rendimiento de cada jugador a lo largo de las temporadas.

- **Simulación de Competencias**: Las competiciones (copas nacionales e internacionales) deben reflejar la evolución de las habilidades de los jugadores, el rendimiento del equipo y las decisiones tácticas.

## 3.4 Simulación de Partidos y Resultados

### **Descripción del Sistema de Simulación de Partidos**:

La simulación de los partidos es una de las funcionalidades clave del sistema. El sistema de simulación determinará cómo interactúan las habilidades individuales de los jugadores durante los partidos y cómo afectan al rendimiento del equipo en cada competición. Para que esto sea realista y detallado, se tienen en cuenta las habilidades específicas de cada jugador (porteros, defensas, mediocampistas, delanteros, etc.), su moral, su estado físico (lesiones), y la estrategia del entrenador.

### **Cálculos Involucrados en la Simulación de Partidos**:

1. **Fuerzas por posición**:

   - **Porteros**: La habilidad en **Portería** es crucial. Los porteros también suman a la fuerza defensiva en función de su habilidad en **Mentalidad** y **Pases**. Ejemplo:
     ```python
     Fuerza Defensiva Portero = (Portería * 0.6) + (Mentalidad * 0.3) + (Pases * 0.1)
     ```

   - **Defensas**: Los defensas priorizan habilidades como **Defensa** y **Mentalidad**, que son cruciales para bloquear ataques. Ejemplo:
     ```python
     Fuerza Defensiva Defensa = (Defensa * 0.7) + (Mentalidad * 0.3)
     ```

   - **Mediocampistas**: La habilidad en **Pases** y **Jugada** es crucial para distribuir el balón de manera efectiva. Ejemplo:
     ```python
     Fuerza Mediocampo = (Pases * 0.6) + (Jugada * 0.4)
     ```

   - **Delanteros**: Los delanteros se centran en **Remate** y **Desmarques**, siendo estos los indicadores clave para marcar goles. Ejemplo:
     ```python
     Fuerza Ofensiva Delantero = (Remate * 0.7) + (Desmarques * 0.3)
     ```

   - **Laterales**: Los laterales (DEFLAT, MEDLAT, DELEX) tienen una habilidad principal que determinará si se ubican en la defensa, el mediocampo o la ofensiva. Ejemplo:
     ```python
     Fuerza Lateral = Lateral * 0.5
     ```