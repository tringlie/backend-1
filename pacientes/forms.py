from datetime import timedelta

from django import forms
from django.utils import timezone

from .models import Cita, Dueno, Mascota


# =========================================================
# FORMULARIO DE MASCOTAS
# =========================================================

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


# =========================================================
# FORMULARIO DE DUEÑOS
# =========================================================

class DuenoForm(forms.ModelForm):
    class Meta:
        model = Dueno

        fields = [
            'nombre',
            'email',
            'telefono',
            'direccion',
            'ciudad',
        ]

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()

        duenos = Dueno.objects.filter(
            email__iexact=email
        )

        # Si estamos editando, no contamos al mismo dueño
        if self.instance.pk:
            duenos = duenos.exclude(
                pk=self.instance.pk
            )

        if duenos.exists():
            raise forms.ValidationError(
                'Ya existe un dueño registrado con este correo.'
            )

        return email


# =========================================================
# FORMULARIO DE CITAS
# =========================================================

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita

        fields = [
            'mascota',
            'veterinario',
            'fecha_hora',
            'razon',
            'estado',
            'notas',
            'duracion',
        ]

        widgets = {
            'fecha_hora': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                },
                format='%Y-%m-%dT%H:%M',
            ),

            'notas': forms.Textarea(
                attrs={
                    'rows': 4,
                }
            ),

            'duracion': forms.NumberInput(
                attrs={
                    'min': '1',
                    'step': '1',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['fecha_hora'].input_formats = [
            '%Y-%m-%dT%H:%M',
        ]

    def clean(self):
        cleaned_data = super().clean()

        mascota = cleaned_data.get('mascota')
        veterinario = cleaned_data.get('veterinario')
        fecha_hora = cleaned_data.get('fecha_hora')
        duracion = cleaned_data.get('duracion')
        estado = cleaned_data.get('estado')

        # Si faltan datos básicos, Django ya mostrará
        # los errores correspondientes
        if not fecha_hora or not duracion:
            return cleaned_data

        # Duración inválida
        if duracion <= 0:
            self.add_error(
                'duracion',
                'La duración debe ser mayor que 0 minutos.'
            )

            return cleaned_data

        # No permitir nuevas citas programadas en el pasado
        if (
            estado == 'PROGRAMADA'
            and fecha_hora < timezone.now()
        ):
            self.add_error(
                'fecha_hora',
                'La cita no puede programarse en una fecha pasada.'
            )

        # Una cita cancelada no necesita reservar horario
        if estado == 'CANCELADA':
            return cleaned_data

        nueva_fin = fecha_hora + timedelta(
            minutes=duracion
        )

        # Ignoramos citas canceladas
        citas = Cita.objects.exclude(
            estado='CANCELADA'
        )

        # Si estamos editando, excluimos la misma cita
        if self.instance.pk:
            citas = citas.exclude(
                pk=self.instance.pk
            )

        # -------------------------------------------------
        # VALIDAR HORARIO DEL VETERINARIO
        # -------------------------------------------------

        if veterinario:
            citas_veterinario = citas.filter(
                veterinario__iexact=veterinario
            )

            for cita in citas_veterinario:
                cita_fin = (
                    cita.fecha_hora
                    + timedelta(minutes=cita.duracion)
                )

                hay_cruce = (
                    fecha_hora < cita_fin
                    and nueva_fin > cita.fecha_hora
                )

                if hay_cruce:
                    self.add_error(
                        'fecha_hora',
                        'El veterinario ya tiene una cita en ese horario.'
                    )
                    break

        # -------------------------------------------------
        # VALIDAR HORARIO DE LA MASCOTA
        # -------------------------------------------------

        if mascota:
            citas_mascota = citas.filter(
                mascota=mascota
            )

            for cita in citas_mascota:
                cita_fin = (
                    cita.fecha_hora
                    + timedelta(minutes=cita.duracion)
                )

                hay_cruce = (
                    fecha_hora < cita_fin
                    and nueva_fin > cita.fecha_hora
                )

                if hay_cruce:
                    self.add_error(
                        'fecha_hora',
                        'La mascota ya tiene una cita en ese horario.'
                    )
                    break

        return cleaned_data