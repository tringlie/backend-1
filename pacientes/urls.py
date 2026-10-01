from django.urls import path

from . import views


urlpatterns = [
    # Mascotas
    path(
        '',
        views.listar_mascotas,
        name='listar_mascotas',
    ),
    path(
        'agregar/',
        views.agregar_mascota,
        name='agregar_mascota',
    ),
    path(
        'editar/<int:mascota_id>/',
        views.editar_mascota,
        name='editar_mascota',
    ),
    path(
        'eliminar/<int:mascota_id>/',
        views.eliminar_mascota,
        name='eliminar_mascota',
    ),
    path(
        'mascotas/<int:mascota_id>/carnet-vacunacion/',
        views.carnet_vacunacion_pdf,
        name='carnet_vacunacion_pdf',
    ),

    # Dueños
    path(
        'duenos/',
        views.listar_duenos,
        name='listar_duenos',
    ),
    path(
        'duenos/agregar/',
        views.agregar_dueno,
        name='agregar_dueno',
    ),
    path(
        'duenos/editar/<int:dueno_id>/',
        views.editar_dueno,
        name='editar_dueno',
    ),
    path(
        'duenos/eliminar/<int:dueno_id>/',
        views.eliminar_dueno,
        name='eliminar_dueno',
    ),

    # Citas
    path(
        'citas/',
        views.listar_citas,
        name='listar_citas',
    ),
    path(
        'citas/agregar/',
        views.agregar_cita,
        name='agregar_cita',
    ),
    path(
        'citas/editar/<int:cita_id>/',
        views.editar_cita,
        name='editar_cita',
    ),
    path(
        'citas/eliminar/<int:cita_id>/',
        views.eliminar_cita,
        name='eliminar_cita',
    ),
]