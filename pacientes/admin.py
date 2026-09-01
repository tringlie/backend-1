from django.contrib import admin
from .models import Mascota



@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'edad', 'vacunacion')
    list_filter = ('especie', 'vacunacion')
    search_fields = ('nombre', 'especie')

