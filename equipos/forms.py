from django import forms
from .models import Alineacion, Jugador, JugadorAlineacion

class AlineacionForm(forms.ModelForm):
    class Meta:
        model = Alineacion
        fields = ['nombre', 'equipo', 'partido', 'estilo_pases', 'actitud', 'entradas', 'marcaje', 'presion']

    def __init__(self, *args, **kwargs):
        equipo = kwargs.pop('equipo', None)
        super().__init__(*args, **kwargs)
        
        # Initialize fields for all positions
        for pos_code, pos_name in Alineacion.POSICIONES:
            self.fields[f'titular_{pos_code}'] = forms.ModelChoiceField(
                queryset=Jugador.objects.none(),
                required=False,
                label=f"{pos_name}",
                widget=forms.Select(attrs={'class': 'form-control'})
            )

        # Initialize fields for substitutes
        for i in range(1, 7):
            self.fields[f'suplente_{i}'] = forms.ModelChoiceField(
                queryset=Jugador.objects.none(),
                required=False,
                label=f'Suplente {i}',
                widget=forms.Select(attrs={'class': 'form-control'})
            )

        # Update querysets if we have an equipo
        if equipo:
            jugadores = Jugador.objects.filter(equipo=equipo)
            # Update querysets for all player fields
            for field_name in self.fields:
                if field_name.startswith('titular_') or field_name.startswith('suplente_'):
                    self.fields[field_name].queryset = jugadores

    def clean(self):
        cleaned_data = super().clean()
        titulares = {}
        suplentes = []

        # Validar titulares
        for pos_code, _ in Alineacion.POSICIONES:
            jugador = cleaned_data.get(f'titular_{pos_code}')
            if jugador:
                titulares[pos_code] = jugador.id

        # Validar suplentes
        for i in range(1, 7):
            jugador = cleaned_data.get(f'suplente_{i}')
            if jugador:
                suplentes.append(jugador.id)

        # Validar número de titulares
        if len(titulares) != 11:
            raise forms.ValidationError("Debe seleccionar exactamente 11 jugadores titulares")

        # Validar que no haya jugadores repetidos
        todos_jugadores = list(titulares.values()) + suplentes
        if len(todos_jugadores) != len(set(todos_jugadores)):
            raise forms.ValidationError("Un jugador no puede estar seleccionado más de una vez")

        return cleaned_data