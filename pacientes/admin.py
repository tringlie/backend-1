from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from .models import Dueno, Mascota, Cita, HistorialMedico, Vacuna, Medicamento, Receta, Factura


#modificacion medicamento
@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'presentacion', 'precio', 'estado_stock', 'estado_vencimiento')
    search_fields = ('nombre',)

    def estado_stock(self, obj):
        if obj.stock <= 0:
            return format_html('<span style="color: white; background: red; padding: 3px 8px; border-radius: 4px;">Agotado</span>')
        elif obj.stock <= 10:
            return format_html('<span style="color: black; background: gold; padding: 3px 8px; border-radius: 4px;">Bajo ({})</span>', obj.stock)
        return format_html('<span style="color: white; background: green; padding: 3px 8px; border-radius: 4px;">OK ({})</span>', obj.stock)
    estado_stock.short_description = 'Inventario'

    def estado_vencimiento(self, obj):
        hoy = timezone.now().date()
        dias_restantes = (obj.fecha_vencimiento - hoy).days
        if dias_restantes < 0:
            return format_html('<span style="color: white; background: red; padding: 3px 8px; border-radius: 4px;">Vencido</span>')
        elif dias_restantes <= 30:
            return format_html('<span style="color: black; background: gold; padding: 3px 8px; border-radius: 4px;">Próximo ({} días)</span>', dias_restantes)
        return format_html('<span style="color: white; background: green; padding: 3px 8px; border-radius: 4px;">Vigente</span>')
    estado_vencimiento.short_description = 'Vencimiento'

#modificacion mascota
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dueno', 'especie', 'ultima_cita', 'proxima_vacuna')
    search_fields = ('nombre', 'dueno__nombre')
    list_filter = ('especie', 'estado')

    def ultima_cita(self, obj):
        cita = obj.citas.filter(estado='COMPLETADA').order_by('-fecha_hora').first()
        return cita.fecha_hora.strftime('%d/%m/%Y') if cita else 'Sin citas previas'
    
    def proxima_vacuna(self, obj):
        vacuna = obj.vacunas.filter(proximo_refuerzo__gte=timezone.now().date()).order_by('proximo_refuerzo').first()
        return vacuna.proximo_refuerzo.strftime('%d/%m/%Y') if vacuna else 'Al día / No programada'

#registro de modelos en el admin
admin.site.register(Dueno)
admin.site.register(Cita)
admin.site.register(HistorialMedico)
admin.site.register(Vacuna)
admin.site.register(Receta)
admin.site.register(Factura)