from django import forms
from .models import Alineacion, Jugador, JugadorAlineacion

class AlineacionForm(forms.ModelForm):
    class Meta:
        model = Alineacion
        fields = [
            'nombre', 'equipo', 'partido', 'estilo_pases', 
            'actitud', 'entradas', 'marcaje', 'presion'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'equipo': forms.Select(attrs={'class': 'form-control'}),
            'partido': forms.Select(attrs={'class': 'form-control'}),
            'estilo_pases': forms.Select(attrs={'class': 'form-control'}),
            'actitud': forms.Select(attrs={'class': 'form-control'}),
            'entradas': forms.Select(attrs={'class': 'form-control'}),
            'marcaje': forms.Select(attrs={'class': 'form-control'}),
            'presion': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.equipo:
            jugadores = Jugador.objects.filter(equipo=self.instance.equipo)
            for pos_code, pos_name in Alineacion.POSICIONES:
                self.fields[f'titular_{pos_code}'] = forms.ModelChoiceField(
                    queryset=jugadores,
                    required=False,
                    label=pos_name,
                    widget=forms.Select(attrs={'class': 'form-control'})
                )

            for i in range(1, 7):
                self.fields[f'suplente_{i}'] = forms.ModelChoiceField(
                    queryset=jugadores,
                    required=False,
                    label=f'Suplente {i}',
                    widget=forms.Select(attrs={'class': 'form-control'})
                )

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