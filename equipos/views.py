from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import AlineacionForm
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Alineacion, JugadorAlineacion
from .forms import AlineacionForm

# JUGADORES
def jugadores_list(request):
    jugadores = Jugador.objects.all()
    return render(request, 'equipos/jugadores_list.html', {'jugadores': jugadores})

def jugador_detail(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    estadisticas = EstadisticaPorTemporada.objects.filter(jugador=jugador)
    return render(request, 'equipos/jugador_detail.html', {'jugador': jugador, 'estadisticas': estadisticas})

# ESTADIOS
def estadios_list(request):
    estadios = Estadio.objects.all()
    return render(request, 'equipos/estadios_list.html', {'estadios': estadios})

def estadio_detail(request, pk):
    estadio = get_object_or_404(Estadio, pk=pk)
    return render(request, 'equipos/estadio_detail.html', {'estadio': estadio})

# EQUIPOS
def equipos_list(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos/equipos_list.html', {'equipos': equipos})

def equipo_detail(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    jugadores = Jugador.objects.filter(equipo=equipo)
    return render(request, 'equipos/equipo_detail.html', {'equipo': equipo, 'jugadores': jugadores})

# ENTRENADORES
def entrenadores_list(request):
    entrenadores = Entrenador.objects.all()
    return render(request, 'equipos/entrenadores_list.html', {'entrenadores': entrenadores})

def entrenador_detail(request, pk):
    entrenador = get_object_or_404(Entrenador, pk=pk)
    return render(request, 'equipos/entrenador_detail.html', {'entrenador': entrenador})

# PARTIDOS
def partidos_list(request):
    partidos = Partido.objects.all()
    return render(request, 'equipos/partidos_list.html', {'partidos': partidos})

def partido_detail(request, pk):
    partido = get_object_or_404(Partido, pk=pk)
    jugadores_ids = (
        list(partido.goles_jugadores_local.keys()) +
        list(partido.goles_jugadores_visitante.keys()) +
        list(partido.asistencias_jugadores_local.keys()) +
        list(partido.asistencias_jugadores_visitante.keys())
    )
    jugadores = Jugador.objects.filter(pk__in=jugadores_ids)
    jugadores_dict = {str(jugador.pk): jugador for jugador in jugadores}

    return render(request, 'equipos/partido_detail.html', {
        'partido': partido,
        'jugadores_dict': jugadores_dict
    })

# REGISTRAR GOLES, ASISTENCIAS Y PARTIDOS

def registrar_resultado(request, pk):
    partido = get_object_or_404(Partido, pk=pk)
    if request.method == 'POST':
        goles_local = int(request.POST['goles_local'])
        goles_visitante = int(request.POST['goles_visitante'])
        goles_jugadores = request.POST.getlist('goles_jugadores')
        asistencias_jugadores = request.POST.getlist('asistencias_jugadores')

        partido.goles_local = goles_local
        partido.goles_visitante = goles_visitante
        partido.goles_jugadores = goles_jugadores
        partido.asistencias_jugadores = asistencias_jugadores
        partido.save()

        # Actualizar goles y asistencias de los equipos
        partido.equipo_local.goles_favor += goles_local
        partido.equipo_local.goles_contra += goles_visitante
        partido.equipo_local.partidos_jugados += 1
        partido.equipo_local.save()

        partido.equipo_visitante.goles_favor += goles_visitante
        partido.equipo_visitante.goles_contra += goles_local
        partido.equipo_visitante.partidos_jugados += 1
        partido.equipo_visitante.save()

        # Actualizar goles y asistencias de los jugadores
        for jugador_id in goles_jugadores:
            jugador = Jugador.objects.get(pk=jugador_id)
            jugador.goles_carrera += 1
            jugador.partidos_carrera += 1
            jugador.save()

            estadistica, created = EstadisticaPorTemporada.objects.get_or_create(
                jugador=jugador, temporada=partido.temporada, equipo=jugador.equipo,
                defaults={'goles': 0, 'asistencias': 0, 'partidos': 0}
            )
            estadistica.goles += 1
            estadistica.partidos += 1
            estadistica.save()

        for jugador_id in asistencias_jugadores:
            jugador = Jugador.objects.get(pk=jugador_id)
            jugador.asistencias_carrera += 1
            jugador.partidos_carrera += 1
            jugador.save()

            estadistica, created = EstadisticaPorTemporada.objects.get_or_create(
                jugador=jugador, temporada=partido.temporada, equipo=jugador.equipo,
                defaults={'goles': 0, 'asistencias': 0, 'partidos': 0}
            )
            estadistica.asistencias += 1
            estadistica.partidos += 1
            estadistica.save()

        return redirect('partido_detail', pk=partido.pk)

    return render(request, 'equipos/registrar_resultado.html', {'partido': partido})

def crear_alineacion(request):
    if request.method == 'POST':
        form = AlineacionForm(request.POST)
        if form.is_valid():
            try:
                alineacion = form.save()
                
                # Procesar titulares
                for pos_code, _ in Alineacion.POSICIONES:
                    jugador = form.cleaned_data.get(f'titular_{pos_code}')
                    if jugador:
                        JugadorAlineacion.objects.create(
                            alineacion=alineacion,
                            jugador=jugador,
                            posicion=pos_code,
                            es_titular=True
                        )
                
                # Procesar suplentes
                for i in range(1, 7):
                    jugador = form.cleaned_data.get(f'suplente_{i}')
                    if jugador:
                        JugadorAlineacion.objects.create(
                            alineacion=alineacion,
                            jugador=jugador,
                            posicion='SUP',
                            es_titular=False,
                            numero_suplente=i
                        )
                
                messages.success(request, 'Alineación creada exitosamente.')
                return redirect('alineacion_detail', pk=alineacion.pk)
            
            except ValueError as e:
                messages.error(request, str(e))
    else:
        form = AlineacionForm()
    
    return render(request, 'equipos/alineacion_create.html', {'form': form})

def editar_alineacion(request, pk):
    alineacion = get_object_or_404(Alineacion, pk=pk)
    
    if request.method == 'POST':
        form = AlineacionForm(request.POST, instance=alineacion)
        if form.is_valid():
            try:
                # Eliminar jugadores existentes
                alineacion.jugadores_alineacion.all().delete()
                
                # Guardar la alineación actualizada
                alineacion = form.save()
                
                # Procesar titulares
                for pos_code, _ in Alineacion.POSICIONES:
                    jugador = form.cleaned_data.get(f'titular_{pos_code}')
                    if jugador:
                        JugadorAlineacion.objects.create(
                            alineacion=alineacion,
                            jugador=jugador,
                            posicion=pos_code,
                            es_titular=True
                        )
                
                # Procesar suplentes
                for i in range(1, 7):
                    jugador = form.cleaned_data.get(f'suplente_{i}')
                    if jugador:
                        JugadorAlineacion.objects.create(
                            alineacion=alineacion,
                            jugador=jugador,
                            posicion='SUP',
                            es_titular=False,
                            numero_suplente=i
                        )
                
                messages.success(request, 'Alineación actualizada exitosamente.')
                return redirect('alineacion_detail', pk=alineacion.pk)
            
            except ValueError as e:
                messages.error(request, str(e))
    else:
        form = AlineacionForm(instance=alineacion)
        
        # Cargar jugadores actuales
        titulares = alineacion.jugadores_alineacion.filter(es_titular=True)
        for jugador_alineacion in titulares:
            form.fields[f'titular_{jugador_alineacion.posicion}'].initial = jugador_alineacion.jugador
        
        suplentes = alineacion.jugadores_alineacion.filter(es_titular=False).order_by('numero_suplente')
        for idx, jugador_alineacion in enumerate(suplentes, 1):
            form.fields[f'suplente_{idx}'].initial = jugador_alineacion.jugador
    
    return render(request, 'equipos/alineacion_form.html', {
        'form': form,
        'alineacion': alineacion,
        'is_edit': True
    })

@require_http_methods(["GET"])
def get_jugadores_equipo(request, equipo_id):
    jugadores = Jugador.objects.filter(equipo_id=equipo_id).values('id', 'nombre', 'portero')
    return JsonResponse(list(jugadores), safe=False)


def alineacion_detail(request, pk):
    alineacion = get_object_or_404(Alineacion, pk=pk)
    titulares = alineacion.jugadores_alineacion.filter(es_titular=True).order_by('posicion')
    suplentes = alineacion.jugadores_alineacion.filter(es_titular=False).order_by('numero_suplente')
    
    context = {
        'alineacion': alineacion,
        'titulares': titulares,
        'suplentes': suplentes,
    }
    return render(request, 'equipos/alineacion_detail.html', context)


def crear_alineacion_preseleccionada(request, equipo_id, partido_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id)
    partido = get_object_or_404(Partido, pk=partido_id)
    
    if request.method == 'POST':
        form = AlineacionForm(request.POST, equipo=equipo)
        if form.is_valid():
            try:
                # Set equipo and partido before saving
                alineacion = form.save(commit=False)
                alineacion.equipo = equipo
                alineacion.partido = partido
                alineacion.save()
                
                # Process players...
                for pos_code, _ in Alineacion.POSICIONES:
                    jugador = form.cleaned_data.get(f'titular_{pos_code}')
                    if jugador:
                        JugadorAlineacion.objects.create(
                            alineacion=alineacion,
                            jugador=jugador,
                            posicion=pos_code,
                            es_titular=True
                        )
                
                # Procesar suplentes
                for i in range(1, 7):
                    jugador = form.cleaned_data.get(f'suplente_{i}')
                    if jugador:
                        JugadorAlineacion.objects.create(
                            alineacion=alineacion,
                            jugador=jugador,
                            posicion='SUP',
                            es_titular=False,
                            numero_suplente=i
                        )
                
                messages.success(request, 'Alineación creada exitosamente.')
                return redirect('alineacion_detail', pk=alineacion.pk)
            
            except ValueError as e:
                messages.error(request, str(e))
    else:
        initial_data = {
            'equipo': equipo,
            'partido': partido,
            'nombre': f'Alineación {equipo.nombre} vs {partido.equipo_visitante.nombre if equipo == partido.equipo_local else partido.equipo_local.nombre}'
        }
        form = AlineacionForm(initial=initial_data, equipo=equipo)

    context = {
        'form': form,
        'equipo': equipo,
        'partido': partido
    }
    return render(request, 'equipos/crear_alineacion.html', context)