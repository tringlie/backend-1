from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DuenoForm, MascotaForm
from .models import Dueno, Mascota


# =========================================================
# MASCOTAS
# =========================================================

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

    return render(
        request,
        'pacientes/agregar.html',
        {'form': form},
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

    return render(
        request,
        'pacientes/editar.html',
        {
            'form': form,
            'mascota': mascota,
        },
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

    return render(
        request,
        'pacientes/eliminar.html',
        {'mascota': mascota},
    )


# =========================================================
# DUEÑOS
# =========================================================

@login_required
def listar_duenos(request):
    duenos = Dueno.objects.all().order_by('nombre')

    busqueda = request.GET.get('nombre', '').strip()

    if busqueda:
        duenos = duenos.filter(
            nombre__icontains=busqueda
        )

    return render(
        request,
        'pacientes/duenos/listar.html',
        {
            'duenos': duenos,
            'busqueda': busqueda,
        },
    )


@login_required
def agregar_dueno(request):
    if request.method == 'POST':
        form = DuenoForm(request.POST)

        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()

            except IntegrityError:
                form.add_error(
                    'email',
                    'Ya existe un dueño registrado con este correo.'
                )

            else:
                messages.success(
                    request,
                    'Dueño registrado correctamente.'
                )

                return redirect('listar_duenos')

    else:
        form = DuenoForm()

    return render(
        request,
        'pacientes/duenos/agregar.html',
        {'form': form},
    )


@login_required
def editar_dueno(request, dueno_id):
    dueno = get_object_or_404(
        Dueno,
        id=dueno_id,
    )

    if request.method == 'POST':
        form = DuenoForm(
            request.POST,
            instance=dueno,
        )

        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()

            except IntegrityError:
                form.add_error(
                    'email',
                    'Ya existe un dueño registrado con este correo.'
                )

            else:
                messages.success(
                    request,
                    'Dueño actualizado correctamente.'
                )

                return redirect('listar_duenos')

    else:
        form = DuenoForm(instance=dueno)

    return render(
        request,
        'pacientes/duenos/editar.html',
        {
            'form': form,
            'dueno': dueno,
        },
    )


@login_required
def eliminar_dueno(request, dueno_id):
    dueno = get_object_or_404(
        Dueno,
        id=dueno_id,
    )

    if request.method == 'POST':

        if dueno.mascotas.exists():
            messages.error(
                request,
                'No se puede eliminar el dueño porque tiene mascotas registradas.'
            )

            return redirect('listar_duenos')

        nombre = dueno.nombre
        dueno.delete()

        messages.success(
            request,
            f'Dueño {nombre} eliminado correctamente.'
        )

        return redirect('listar_duenos')

    return render(
        request,
        'pacientes/duenos/eliminar.html',
        {'dueno': dueno},
    )