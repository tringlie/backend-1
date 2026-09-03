from django.shortcuts import render
from .models import Mascota

def listar_mascotas(request):
    mascotas = Mascota.objects.all()

    especies = Mascota.objects.values_list('especie', flat=True).distinct()

    especie_filtrada = request.GET.get('especie')

    if especie_filtrada:
        mascotas = mascotas.filter(especie=especie_filtrada)

    contexto = {
        'mascotas': mascotas,
        'especies': especies,
        'especie_filtrada': especie_filtrada
    }


    return render(request, 'listar.html', contexto)