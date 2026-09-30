from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

from .models import (
    Dueno,
    Mascota,
    Cita,
    HistorialMedico,
    Vacuna,
    Medicamento,
    Receta,
    Factura,
)


@admin.register(Dueno)
class DuenoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'ciudad')
    search_fields = ('nombre', 'email', 'telefono')
    list_filter = ('ciudad',)


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'especie',
        'raza',
        'dueno',
        'estado',
        'proxima_vacuna',
        'ultima_cita',
    )

    search_fields = (
        'nombre',
        'especie',
        'raza',
        'dueno__nombre',
        'dueno__email',
    )

    list_filter = ('especie', 'estado', 'sexo')

    @admin.display(description='Próxima vacuna')
    def proxima_vacuna(self, obj):
        vacuna = (
            obj.vacunas
            .filter(
                proximo_refuerzo__isnull=False,
                proximo_refuerzo__gte=timezone.localdate(),
            )
            .order_by('proximo_refuerzo')
            .first()
        )

        if vacuna:
            return vacuna.proximo_refuerzo

        return 'Sin refuerzo'


    @admin.display(description='Última cita')
    def ultima_cita(self, obj):
        cita = obj.citas.order_by('-fecha_hora').first()

        if cita:
            return cita.fecha_hora

        return 'Sin citas'


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = (
        'mascota',
        'veterinario',
        'fecha_hora',
        'estado',
        'duracion',
    )

    search_fields = (
        'mascota__nombre',
        'veterinario',
        'razon',
    )

    list_filter = ('estado', 'fecha_hora')


@admin.register(HistorialMedico)
class HistorialMedicoAdmin(admin.ModelAdmin):
    list_display = (
        'mascota',
        'fecha',
        'veterinario',
        'diagnostico',
    )

    search_fields = (
        'mascota__nombre',
        'veterinario',
        'diagnostico',
    )

    list_filter = ('fecha',)


@admin.register(Vacuna)
class VacunaAdmin(admin.ModelAdmin):
    list_display = (
        'mascota',
        'nombre',
        'fecha_administracion',
        'proximo_refuerzo',
        'veterinario',
    )

    search_fields = (
        'mascota__nombre',
        'nombre',
        'veterinario',
    )

    list_filter = (
        'fecha_administracion',
        'proximo_refuerzo',
    )


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'presentacion',
        'stock',
        'precio',
        'fecha_vencimiento',
        'estado_inventario',
    )

    search_fields = ('nombre', 'presentacion')
    list_filter = ('fecha_vencimiento',)

    @admin.display(description='Estado')
    def estado_inventario(self, obj):
        hoy = timezone.localdate()

        if obj.fecha_vencimiento < hoy:
            estado = 'VENCIDO'
        elif obj.stock < 5:
            estado = 'BAJO'
        else:
            estado = 'OK'

        estilos = {
            'VENCIDO': ('red', 'Vencido'),
            'BAJO': ('orange', 'Bajo stock'),
            'OK': ('green', 'OK'),
        }

        color, texto = estilos.get(
            estado,
            ('gray', 'Sin estado'),
        )

        return format_html(
            '<span style="color:{}; font-weight:bold;">{}</span>',
            color,
            texto,
        )


@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = (
        'cita',
        'medicamento',
        'dosis',
        'duracion_dias',
    )

    search_fields = (
        'cita__mascota__nombre',
        'medicamento__nombre',
    )


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = (
        'dueno',
        'cita',
        'monto',
        'fecha',
        'estado_pago',
    )

    search_fields = (
        'dueno__nombre',
        'dueno__email',
    )

    list_filter = (
        'estado_pago',
        'fecha',
    )