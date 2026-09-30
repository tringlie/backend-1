from django.shortcuts import render
from .models import Mascota


def listar_mascotas(request):
    mascotas = Mascota.objects.select_related('dueno').all()

    busqueda = request.GET.get('nombre', '').strip()
    especie = request.GET.get('especie', '').strip()
    estado = request.GET.get('estado', '').strip()

    especies = (
        Mascota.objects
        .values_list('especie', flat=True)
        .distinct()
        .order_by('especie')
    )

    if busqueda:
        mascotas = mascotas.filter(nombre__icontains=busqueda)

    if especie:
        mascotas = mascotas.filter(especie__iexact=especie)

    if estado:
        mascotas = mascotas.filter(estado=estado)

    estados_config = {
        'ACTIVO': {
            'texto': 'Activo',
            'clase': 'activo',
        },
        'INACTIVO': {
            'texto': 'Inactivo',
            'clase': 'inactivo',
        },
        'FALLECIDO': {
            'texto': 'Fallecido',
            'clase': 'fallecido',
        },
    }

    estado_default = {
        'texto': 'Sin estado',
        'clase': 'sin-estado',
    }

    for mascota in mascotas:
        config = estados_config.get(
            mascota.estado,
            estado_default,
        )

        mascota.estado_texto = config['texto']
        mascota.estado_clase = config['clase']

    contexto = {
        'mascotas': mascotas,
        'busqueda': busqueda,
        'especie': especie,
        'estado': estado,
        'especies': especies,
    }

    return render(
        request,
        'pacientes/listar.html',
        contexto,
    )