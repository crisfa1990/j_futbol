## 2.1 Alineacion

**Objetivo:** Crear un formulario en Django que permita a los usuarios crear formaciones de fútbol del equipo de futbol para un partido en particular, se deben incluir 11 titulares y 6 sustitutos.

### **Restricciones:**

* **Jugadores por posición:**
    * **POR:** Mínimo 1, máximo 1.
    * **DFC:** Mínimo 1,máximo 3.
    * **DFD:** Mínimo 0,máximo 1. 
    * **DFL:** Mínimo 0,máximo 1. 
  
    * **Mediocampista defensivo (MCD):** Mínimo 0, máximo 3.
  
    * **Mediocampista central (MEC):** Mínimo 0. máximo 3.
    * **Mediocampista derecho (MED):** Mínimo 0, máximo 1.
    * **Mediocampista izquierdo (MEI):** Mínimo 0, máximo 1.

    * **Mediocampista ofensivo (MPC):** Mínimo 0, máximo 3.
    * **Extremo derecho (MPD):** Mínimo 0, máximo 3.
    * **Extremo izquierdo (MPI):** Mínimo 0, máximo 3.

    * **Delantero centro(DLC):** Mínimo 0, máximo .
    * **Delantero centro derecho(DLD):** Mínimo 0, máximo 1.
    * **Delantero centro izquierdo(DLI):** Mínimo 0, máximo 1.
    
* **Jugadores por línea:**
    * **Defensa(DFC, DFD y DFI):** MMáximo 5.
    * **Mediocentro(MCD):** Máximo 3.
    * **Mediocampo(MEC, MED, MEI):** Máximo 5.
    * **Mediapunta(MPC, MPD, MPI):** Máximo 5
    * **Delantera(DLC, DLD, DLI):** Máximo 3.

### **Estrategia equipo:**

* **Estilos de pases:**
    * Cortos
    * Largos
    * Mixtos
* **Actitud del equipo:**
    * Ataque
    * Defensa
    * Equilibrado
* **Entradas:**
    * Fuertes
    * Suaves
* **Marcaje:**
    * Férreo
    * Normal
    * A zona
* **Presión:**
    * Baja
    * Media
    * Alta


### Implementacion en Django
Este prompt se dividirá en 4 respuestas principales, con preguntas específicas antes de avanzar a la siguiente etapa.

1. **Modelos de la Base de Datos (models.py)**
* **Pregunta a ChatGPT:** "Crea los modelos de Django necesarios para representar la información de jugadores, alineaciones y estrategias. Considera campos como nombre del jugador, posición, estilo de pases, actitud del equipo, etc. Incluye las relaciones necesarias entre los modelos (por ejemplo, un jugador pertenece a una alineación)."

* **Detalles adicionales:**

Asegúrate de incluir campos para:
* Información básica del jugador (nombre, posición, dorsal, etc.)
* Detalles de la alineación (nombre de la alineación, fecha de creación, etc.)
* Estrategias (estilo de pases, actitud, entradas, marcaje, presión)

2. **Vistas, Formularios y Lógica de Guardado (views.py, forms.py)**
* **Pregunta a ChatGPT:** "Con los modelos definidos, crea las vistas y formularios de Django necesarios para:

* Mostrar un formulario para crear o editar alineaciones.
* Permitir la selección de jugadores existentes para la alineación.
* Guardar la información de la alineación en la base de datos."
* **Detalles adicionales:**

* Utiliza formularios de Django (ModelForm) para facilitar la creación de formularios basados en modelos.
* Implementa la lógica necesaria en las vistas para procesar el formulario y guardar los datos.
* Considera validaciones en el formulario para asegurar la integridad de los datos (por ejemplo, que no haya más de un portero).

3. **URLs y Detalles Adicionales (urls.py)**
* **Pregunta a ChatGPT:** "Define las URLs necesarias para acceder a las vistas de creación y edición de alineaciones. Incluye cualquier otro detalle necesario para la correcta implementación del sistema, como configuración de archivos estáticos o mensajes de éxito/error."

* **Detalles adicionales:**

* Crea las URLs en el archivo urls.py de tu aplicación.
* Considera el uso de nombres para las URLs (name='nombre_url') para facilitar la generación de enlaces.

4. **Templates (templates/)**
* **Pregunta a ChatGPT:** "Crea los templates HTML necesarios para:

* Mostrar el formulario de creación/edición de alineaciones.
* Mostrar una lista de alineaciones existentes (opcional).
* Incluir mensajes de éxito o error (opcional)."
* 
* **Detalles adicionales:**

* Utiliza el lenguaje de templates de Django para mostrar el formulario y los datos.
* Considera el uso de frameworks CSS como Bootstrap para mejorar la apariencia de los templates.

### Formato de Respuesta Esperado
Para cada respuesta, espera:

* Código Python para modelos, vistas y formularios.
* Código HTML para templates.
* Explicaciones claras y concisas del código generado.
* Preguntas Intermedias
* 
### Antes de avanzar a la siguiente respuesta, ChatGPT deberá preguntar:

* "¿Estás de acuerdo con los modelos propuestos?" (Respuesta 1)
* "¿Deseas agregar validaciones específicas al formulario?" (Respuesta 2)
* "¿Necesitas alguna URL adicional o configuración específica?" (Respuesta 3)
* "¿Prefieres algún estilo o estructura HTML particular para los templates?" (Respuesta 4)

