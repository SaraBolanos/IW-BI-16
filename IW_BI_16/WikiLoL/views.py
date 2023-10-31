from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Campeon, Habilidad, Coleccion, Skin


# Create your views here.
def listaCampeones(request):
    campeon = Campeon.objects.order_by('nombre')
    output = ', '.join([e.nombre for e in campeon])
    return HttpResponse(output)