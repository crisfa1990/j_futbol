document.addEventListener('DOMContentLoaded', function() {
    const equipoSelect = document.getElementById('id_equipo');
    const jugadoresSelects = document.querySelectorAll('select[id^="id_titular_"], select[id^="id_suplente_"]');
    const jugadoresSeleccionados = new Set();

    function actualizarJugadoresDisponibles() {
        jugadoresSeleccionados.clear();
        jugadoresSelects.forEach(select => {
            if (select.value) {
                jugadoresSeleccionados.add(select.value);
            }
        });

        jugadoresSelects.forEach(select => {
            const valorActual = select.value;
            Array.from(select.options).forEach(option => {
                if (option.value && option.value !== valorActual) {
                    option.disabled = jugadoresSeleccionados.has(option.value);
                }
            });
        });
    }

    // Actualizar jugadores cuando cambia el equipo
    equipoSelect.addEventListener('change', function() {
        const equipoId = this.value;
        if (equipoId) {
            fetch(`/api/equipos/${equipoId}/jugadores/`)
                .then(response => response.json())
                .then(jugadores => {
                    jugadoresSelects.forEach(select => {
                        const currentValue = select.value;
                        select.innerHTML = '<option value="">---------</option>';
                        jugadores.forEach(jugador => {
                            const option = new Option(jugador.nombre, jugador.id);
                            select.add(option);
                        });
                        select.value = currentValue;
                    });
                    actualizarJugadoresDisponibles();
                });
        }
    });

    // Actualizar disponibilidad cuando se selecciona un jugador
    jugadoresSelects.forEach(select => {
        select.addEventListener('change', actualizarJugadoresDisponibles);
    });
});