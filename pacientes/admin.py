from django.contrib import admin
from .models import Dueno, Mascota, Cita


@admin.register(Dueno)
class DuenoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'ciudad')
    search_fields = ('nombre', 'email', 'telefono')
    list_filter = ('ciudad',)


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'dueno', 'estado')
    search_fields = ('nombre', 'especie', 'raza', 'dueno__nombre')
    list_filter = ('especie', 'estado', 'sexo')


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'veterinario', 'fecha_hora', 'estado')
    search_fields = ('mascota__nombre', 'veterinario', 'razon')
    list_filter = ('estado', 'fecha_hora')
