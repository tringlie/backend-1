from django.shortcuts import render
from .models import Mascota


def listar_mascotas(request):
    mascotas = Mascota.objects.all()

    contexto = {
        'mascotas': mascotas
    }

    return render(request, 'pacientes/listar.html', contexto)