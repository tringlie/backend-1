from django.shortcuts import render
from .models import Mascota


def listar_mascotas(request):
    mascotas = Mascota.objects.all()

    busqueda = request.GET.get('nombre')
    especie = request.GET.get('especie')
    vacunacion = request.GET.get('vacunacion')

    if busqueda:
        mascotas = mascotas.filter(nombre__icontains=busqueda)

    if especie:
        mascotas = mascotas.filter(especie__iexact=especie)

    if vacunacion:
        mascotas = mascotas.filter(vacunacion=vacunacion)

    contexto = {
        'mascotas': mascotas,
        'busqueda': busqueda,
        'especie': especie,
        'vacunacion': vacunacion
    }

    return render(request, 'pacientes/listar.html', contexto)