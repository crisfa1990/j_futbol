# **Planificación del Proyecto: Componente Esencial (Modelo + Simulación de Partidos)**

## **Fase 1: Implementación de Modelos y Base de Datos (2-3 semanas)**

En esta fase nos vamos a centrar en crear la estructura fundamental del proyecto: los modelos y la base de datos. Esto es crucial porque te permitirá tener una base estable para el resto de la funcionalidad y te ayudará a estructurar los datos de manera eficiente desde el principio.

### **1.1. Crear los Modelos Básicos (Semana 1)**

#### **Objetivo**:
Desarrollar los modelos de datos básicos para el sistema de gestión del club de fútbol.

#### **Acciones**:
1. **Modelo `Jugador`**:
   - **Atributos**:
     - `nombre` (CharField)
     - `fecha_nacimiento` (DateField)
     - `habilidades` (JSONField para almacenar las habilidades de forma flexible)
     - `moral` (IntegerField, escala de 0-100)
     - `salario` (DecimalField)
     - `lesion` (BooleanField)
     - `equipo` (ForeignKey a `Equipo`)
     - `nacionalidad` (CharField)
     - `goles_totales` (IntegerField)
     - `goles_temporada` (IntegerField)
     - `asistencias_totales` (IntegerField)
     - `asistencias_temporada` (IntegerField)
     - `partidos_totales` (IntegerField)
     - `partidos_temporada` (IntegerField)
   - **Relaciones**:
     - Relacionar `Jugador` con `Equipo` mediante una relación `ForeignKey`.
     - Relacionar a cada jugador con su `equipo`, su `nacionalidad` y otros atributos.
  
2. **Modelo `Equipo`**:
   - **Atributos**:
     - `nombre` (CharField)
     - `fundacion` (DateField)
     - `presupuesto` (DecimalField)
     - `jugadores` (ManyToMany con `Jugador`)
     - `entrenador` (ForeignKey con `Entrenador`)
   - **Relaciones**:
     - Relación de tipo `ManyToMany` con `Jugador`, ya que un equipo puede tener varios jugadores.
     - Relación de tipo `ForeignKey` con `Entrenador`, que será otro modelo que se desarrollará más tarde.

3. **Modelo `Temporada`**:
   - **Atributos**:
     - `año` (IntegerField)
     - `equipo` (ForeignKey a `Equipo`)
     - `partidos_jugados` (IntegerField)
     - `victorias` (IntegerField)
     - `derrotas` (IntegerField)
     - `goles_favor` (IntegerField)
     - `goles_contra` (IntegerField)
     - `puntaje_total` (IntegerField)
   - **Relaciones**:
     - Relacionar `Temporada` con `Equipo` mediante una relación `ForeignKey`.

4. **Modelo `Lesión`**:
   - **Atributos**:
     - `jugador` (ForeignKey a `Jugador`)
     - `fecha_inicio` (DateField)
     - `fecha_fin` (DateField)
     - `tipo` (CharField, para clasificar la lesión: leve, moderada, grave)
     - `impacto` (IntegerField, por ejemplo, porcentaje de impacto en habilidades)
   - **Relaciones**:
     - Relación de tipo `ForeignKey` con `Jugador`.

#### **Acciones adicionales**:
- **Migraciones**: Realizar las migraciones correspondientes para aplicar estos modelos a la base de datos.
- **Pruebas iniciales**: Asegurarse de que los modelos y las relaciones funcionan correctamente mediante pruebas básicas en Django Admin.
#### **Informe avance:**: 
**Logrado completamente 16-01-2025, revisar 1modelos.md para mas información.**

---

### **1.2. Relacionar los Modelos con Funcionalidades Básicas (Semana 2)**

Una vez que se hayan creado los modelos básicos, es importante asegurarse de que las relaciones entre ellos sean funcionales y estables. 

#### **Acciones**:
1. **Configuración de la base de datos**:
   - Configurar las migraciones para todos los modelos y asegurarse de que la base de datos esté correctamente inicializada.
   
2. **Implementación de los cálculos de sueldos y habilidades**:
   - Añadir una función para calcular el sueldo del jugador en función de sus habilidades, moral y otros atributos. Este cálculo podría ser implementado como una propiedad calculada o una función dentro del modelo `Jugador`.

3. **Sistema básico de moral**:
   - Crear una función que ajuste la moral de un jugador según su rendimiento (partidos jugados, goles marcados, etc.). Esto permitirá que la moral del jugador se vea reflejada en su rendimiento y en su sueldo.

4. **Interfaz básica con Django Admin**:
   - Crear vistas en Django Admin para poder gestionar y visualizar los jugadores, equipos, temporadas, y lesiones.
   - Añadir formularios de entrada y edición para cada modelo, asegurándose de que la información se pueda gestionar fácilmente.

5. **Testeo inicial**:
   - Verificar que las funcionalidades básicas como la creación y edición de jugadores, equipos y temporadas estén funcionando correctamente.
   - Probar la capacidad de cálculo de sueldos y la integración de datos.

---

## **Fase 2: Implementación del Sistema de Simulación de Partidos (3-4 semanas)**

#### **2.1. Simulación Básica de Partidos**
La simulación de partidos será el siguiente gran paso después de tener los modelos listos. En esta fase, implementaremos una lógica simple que utilice las habilidades de los jugadores para determinar el resultado de los partidos.

#### **Acciones**:
1. **Definir las habilidades clave**:
   - **Fuerza ofensiva** (remate, desmarques).
   - **Fuerza defensiva** (defensa, mental).
   - **Fuerza de mediocampo** (pases, jugadas).
   - **Porteros**: Implementar un cálculo especial para los porteros que les dé un peso mayor en el resultado.

2. **Crear la lógica básica de partidos**:
   - **Lógica de simulación**: Basado en las habilidades individuales de los jugadores y las tácticas generales (por ejemplo, si un equipo tiene más fuerza ofensiva, tendrá más probabilidades de marcar goles).
   - **Eventos aleatorios**: Introducir eventos aleatorios como goles, tarjetas y lesiones durante los partidos.
   
**Ejemplo de la lógica para determinar si un jugador marca un gol**:
```python
def calcular_probabilidad_gol(jugador):
    habilidad_ofensiva = jugador.remate + jugador.desmarques
    probabilidad = habilidad_ofensiva / 100
    if random.random() < probabilidad:
        return True  # Gol marcado
    return False
```
### **Simulación de partidos:**
1. Implementar la simulación de partidos entre dos equipos donde cada equipo tiene una formación basada en las habilidades de sus jugadores.
2. Los partidos se simularán según la fuerza total de cada equipo (sumando las habilidades de los jugadores), y los resultados serán afectados por eventos aleatorios.

3. **Registrar el resultado**:
   - Crear un sistema para registrar los resultados de los partidos, actualizando la temporada y las estadísticas de los jugadores (goles, asistencias, tarjetas, etc.).

4. **Integración con el sistema de temporadas**:
   - Registrar los partidos jugados dentro de la `Temporada`, actualizando las estadísticas del equipo y los jugadores.

---

### **2.2. Expansión de la Simulación (Semana 3-4)**

#### **Acciones**:
1. **Incorporar tácticas**:
   - Crear una manera de que los entrenadores puedan configurar tácticas de equipo.
2. **Simulación de la moral**:
   - Introducir el impacto de la moral del jugador en su rendimiento en los partidos.
3. **Mejoras en la simulación**:
   - Añadir más complejidad al sistema de simulación, como la capacidad de cambiar jugadores durante el partido (sustituciones) y cómo esto afecta el rendimiento.

4. **Interfaz de simulación**:
   - Crear una interfaz básica para que el usuario pueda simular partidos, ver los resultados y analizar estadísticas.

5. **Pruebas de integración**:
   - Realizar pruebas para asegurar que la simulación se comporte correctamente con los datos reales (jugadores, equipos, partidos).

---

## **Fase 3: Funcionalidades Complementarias (4-6 semanas)**

En esta fase, nos enfocaremos en añadir más funcionalidades avanzadas, como ligas, copas, y la interfaz de usuario para gestionar todo el sistema.

### **3.1. Desarrollo de Ligas y Copas**
1. **Gestión de ligas nacionales e internacionales**:
   - Crear la estructura de ligas con equipos, partidos, clasificaciones, etc.
2. **Sistema de copas**:
   - Crear un sistema de copas nacionales e internacionales con eliminación directa o formato de grupos.

### **3.2. Desarrollo de la Interfaz de Usuario**
1. **Interfaz web**:
   - Usar Django templates o un framework como React para crear una interfaz de usuario para la simulación de partidos, gestión de equipos y jugadores, y ver estadísticas.