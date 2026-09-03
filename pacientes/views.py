from django.shortcuts import render
from .models import Mascota

def listar_mascotas(request):
    mascotas = Mascota.objects.all()

    especies = Mascota.objects.values_list('especie', flat=True).distinct()
    busqueda = request.GET.get('busqueda')

    especie_filtrada = request.GET.get('especie')

    if especie_filtrada:
        mascotas = mascotas.filter(especie=especie_filtrada)

    if busqueda:
        busqueda = busqueda.strip()
        if busqueda:
            mascotas = mascotas.filter(nombre__icontains=busqueda)

    contexto = {
        'mascotas': mascotas,
        'especies': especies,
        'especie_activa': especie_filtrada or '',
        'busqueda': busqueda or '',
    }


    return render(request, 'listar.html', contexto)