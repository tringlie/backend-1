from django import forms
from django.utils import timezone

from .models import Mascota


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota

        fields = [
            'dueno',
            'nombre',
            'especie',
            'raza',
            'fecha_nacimiento',
            'peso',
            'foto',
            'sexo',
            'estado',
        ]

        widgets = {
            'fecha_nacimiento': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'peso': forms.NumberInput(
                attrs={
                    'step': '0.01',
                    'min': '0.01',
                }
            ),
        }

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data['fecha_nacimiento']

        if fecha > timezone.localdate():
            raise forms.ValidationError(
                'La fecha de nacimiento no puede ser futura.'
            )

        return fecha

    def clean_peso(self):
        peso = self.cleaned_data['peso']

        if peso <= 0:
            raise forms.ValidationError(
                'El peso debe ser mayor que 0.'
            )

        return peso
