from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_mascotas, name='listar_mascotas'),
    # Comenta la línea de abajo agregando un '#' al inicio:
    # path('mascota/<int:mascota_id>/carnet/', views.descargar_carnet_pdf, name='descargar_carnet'),
]