from django.urls import path

from . import views


urlpatterns = [
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
]