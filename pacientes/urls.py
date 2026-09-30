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
]