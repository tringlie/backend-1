from django.shortcuts import render
from .models import Mascota

def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'pacientes/listar.html', {'mascotas': mascotas})
