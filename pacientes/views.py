from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MascotaForm
from .models import Mascota


@login_required
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


@login_required
def agregar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Mascota registrada correctamente.'
            )

            return redirect('listar_mascotas')

    else:
        form = MascotaForm()

    contexto = {
        'form': form,
    }

    return render(
        request,
        'pacientes/agregar.html',
        contexto,
    )


@login_required
def editar_mascota(request, mascota_id):
    mascota = get_object_or_404(
        Mascota,
        id=mascota_id,
    )

    if request.method == 'POST':
        form = MascotaForm(
            request.POST,
            request.FILES,
            instance=mascota,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Mascota actualizada correctamente.'
            )

            return redirect('listar_mascotas')

    else:
        form = MascotaForm(instance=mascota)

    contexto = {
        'form': form,
        'mascota': mascota,
    }

    return render(
        request,
        'pacientes/editar.html',
        contexto,
    )


@login_required
def eliminar_mascota(request, mascota_id):
    mascota = get_object_or_404(
        Mascota,
        id=mascota_id,
    )

    if request.method == 'POST':
        nombre = mascota.nombre

        mascota.delete()

        messages.success(
            request,
            f'Mascota {nombre} eliminada correctamente.'
        )

        return redirect('listar_mascotas')

    contexto = {
        'mascota': mascota,
    }

    return render(
        request,
        'pacientes/eliminar.html',
        contexto,
    )