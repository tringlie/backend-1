from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db import IntegrityError, transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from .forms import CitaForm, DuenoForm, MascotaForm
from .models import Cita, Dueno, Mascota, Vacuna


# =========================================================
# MASCOTAS
# =========================================================

@login_required
@permission_required('pacientes.view_mascota', raise_exception=True)
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

    paginator = Paginator(mascotas, 5)
    numero_pagina = request.GET.get('page')
    mascotas = paginator.get_page(numero_pagina)

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
@permission_required('pacientes.add_mascota', raise_exception=True)
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
@permission_required('pacientes.change_mascota', raise_exception=True)
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
@permission_required('pacientes.delete_mascota', raise_exception=True)
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
@permission_required('pacientes.view_dueno', raise_exception=True)
def listar_duenos(request):
    duenos = Dueno.objects.all().order_by('nombre')

    busqueda = request.GET.get('nombre', '').strip()

    if busqueda:
        duenos = duenos.filter(
            nombre__icontains=busqueda
        )

    paginator = Paginator(duenos, 5)
    numero_pagina = request.GET.get('page')
    duenos = paginator.get_page(numero_pagina)

    return render(
        request,
        'pacientes/duenos/listar.html',
        {
            'duenos': duenos,
            'busqueda': busqueda,
        },
    )


@login_required
@permission_required('pacientes.add_dueno', raise_exception=True)
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
@permission_required('pacientes.change_dueno', raise_exception=True)
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
@permission_required('pacientes.delete_dueno', raise_exception=True)
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


# =========================================================
# CITAS
# =========================================================

@login_required
@permission_required('pacientes.view_cita', raise_exception=True)
def listar_citas(request):
    citas = (
        Cita.objects
        .select_related(
            'mascota',
            'mascota__dueno',
        )
        .order_by('fecha_hora')
    )

    busqueda = request.GET.get('buscar', '').strip()
    estado = request.GET.get('estado', '').strip()

    if busqueda:
        citas = citas.filter(
            Q(mascota__nombre__icontains=busqueda)
            | Q(veterinario__icontains=busqueda)
        )

    if estado:
        citas = citas.filter(estado=estado)

    paginator = Paginator(citas, 5)
    numero_pagina = request.GET.get('page')
    citas = paginator.get_page(numero_pagina)

    contexto = {
        'citas': citas,
        'busqueda': busqueda,
        'estado': estado,
    }

    return render(
        request,
        'pacientes/citas/listar.html',
        contexto,
    )


@login_required
@permission_required('pacientes.add_cita', raise_exception=True)
def agregar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Cita registrada correctamente.'
            )

            return redirect('listar_citas')

    else:
        form = CitaForm()

    return render(
        request,
        'pacientes/citas/agregar.html',
        {'form': form},
    )


@login_required
@permission_required('pacientes.change_cita', raise_exception=True)
def editar_cita(request, cita_id):
    cita = get_object_or_404(
        Cita,
        id=cita_id,
    )

    if request.method == 'POST':
        form = CitaForm(
            request.POST,
            instance=cita,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Cita actualizada correctamente.'
            )

            return redirect('listar_citas')

    else:
        form = CitaForm(instance=cita)

    return render(
        request,
        'pacientes/citas/editar.html',
        {
            'form': form,
            'cita': cita,
        },
    )


@login_required
@permission_required('pacientes.delete_cita', raise_exception=True)
def eliminar_cita(request, cita_id):
    cita = get_object_or_404(
        Cita,
        id=cita_id,
    )

    if request.method == 'POST':
        mascota = cita.mascota.nombre
        cita.delete()

        messages.success(
            request,
            f'Cita de {mascota} eliminada correctamente.'
        )

        return redirect('listar_citas')

    return render(
        request,
        'pacientes/citas/eliminar.html',
        {'cita': cita},
    )


# =========================================================
# CARNET DE VACUNACIÓN PDF
# =========================================================

@login_required
@permission_required('pacientes.view_mascota', raise_exception=True)
def carnet_vacunacion_pdf(request, mascota_id):
    mascota = get_object_or_404(
        Mascota.objects.select_related('dueno'),
        id=mascota_id,
    )

    vacunas = (
        Vacuna.objects
        .filter(mascota=mascota)
        .order_by('fecha_administracion')
    )

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        f'attachment; filename="carnet_{mascota.nombre}.pdf"'
    )

    documento = SimpleDocTemplate(
        response,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    estilos = getSampleStyleSheet()
    contenido = []

    contenido.append(
        Paragraph(
            'Carnet de Vacunación',
            estilos['Title'],
        )
    )

    contenido.append(Spacer(1, 0.5 * cm))

    contenido.append(
        Paragraph(
            f'<b>Mascota:</b> {mascota.nombre}',
            estilos['Normal'],
        )
    )

    contenido.append(
        Paragraph(
            f'<b>Dueño:</b> {mascota.dueno.nombre}',
            estilos['Normal'],
        )
    )

    contenido.append(
        Paragraph(
            f'<b>Especie:</b> {mascota.especie}',
            estilos['Normal'],
        )
    )

    contenido.append(Spacer(1, 0.7 * cm))

    datos = [
        [
            'Vacuna',
            'Fecha administración',
            'Próximo refuerzo',
            'Veterinario',
        ]
    ]

    for vacuna in vacunas:
        fecha = vacuna.fecha_administracion.strftime(
            '%d/%m/%Y'
        )

        if vacuna.proximo_refuerzo:
            refuerzo = vacuna.proximo_refuerzo.strftime(
                '%d/%m/%Y'
            )
        else:
            refuerzo = 'Sin fecha'

        datos.append(
            [
                vacuna.nombre,
                fecha,
                refuerzo,
                vacuna.veterinario,
            ]
        )

    if vacunas.exists():
        tabla = Table(
            datos,
            colWidths=[
                4 * cm,
                4 * cm,
                4 * cm,
                4 * cm,
            ],
        )

        tabla.setStyle(
            TableStyle(
                [
                    (
                        'BACKGROUND',
                        (0, 0),
                        (-1, 0),
                        colors.lightgrey,
                    ),
                    (
                        'GRID',
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.grey,
                    ),
                    (
                        'VALIGN',
                        (0, 0),
                        (-1, -1),
                        'MIDDLE',
                    ),
                    (
                        'FONTNAME',
                        (0, 0),
                        (-1, 0),
                        'Helvetica-Bold',
                    ),
                    (
                        'ALIGN',
                        (1, 1),
                        (2, -1),
                        'CENTER',
                    ),
                ]
            )
        )

        contenido.append(tabla)

    else:
        contenido.append(
            Paragraph(
                'Esta mascota no tiene vacunas registradas.',
                estilos['Normal'],
            )
        )

    documento.build(contenido)

    return response