from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Campeon, Habilidad, Coleccion, Skin


def main(request):
    campeon = Campeon.objects.order_by('nombre')
    coleccion = Coleccion.objects.order_by('nombre')
    skin = Skin.objects.order_by('precio')
    habilidad = Habilidad.objects.order_by('nombre')
    return render(request, 'main.html')


# Create your views here.
def listaCampeones(request):
    campeon = Campeon.objects.order_by('nombre')
    output = ', '.join([e.nombre for e in campeon])
    return HttpResponse(output)

# ------ CAMPEONES ------
def listaCampeones(request):
    campeon = Campeon.objects.order_by('nombre')

    context = {'campeon_list' : campeon}

    return render(request, 'listaCampeones.html', context)

def detalleCampeones(request,id_campeon):
    campeon = Campeon.objects.get(pk = id_campeon)
    habilidad = Habilidad.objects.order_by('nombre')
    skin = Skin.objects.order_by('nombre')
    context = { 'login':True,'campeon' : campeon, 'habilidades_list' : habilidad, 'skin_list' : skin}

    return render(request, 'detalleCampeon.html', context)

# ------ COLECCIONES ------
def listaColecciones(request):
    colecciones = Coleccion.objects.order_by('nombre')
    skin = Skin.objects.order_by('nombre')
    context =  {'coleccion_list':colecciones, 'skin_list' : skin}
    return render(request, 'coleccion.html', context)


def detalleColecciones(request,id_coleccion):
    coleccion = Coleccion.objects.get( pk = id_coleccion)

    skin = Skin.objects.order_by('nombre')
    context = { 'login':True,'coleccion' : coleccion, 'skin_list' : skin}

    return render(request, 'detalleColeccion.html', context)

# ------ SKINS ------
def listaSkins(request):
    skins = Skin.objects.order_by('nombre')
    context =  {'skin_list' : skins}
    return render(request, 'listaSkins.html', context)


def detalleSkins(request,id_skins):
    skin = Skin.objects.get( pk = id_skins)

    context = { 'login':True,'skin' : skin}
    return render(request, 'detalleSkin.html', context)

# ------ HABILIDADES ------
def listaHabilidad(request):
    habilidades = Habilidad.objects.order_by('nombre')
    context =  {'habilidades_list':habilidades}
    return render(request, 'habilidad.html', context)


def detalleHabilidad(request,id_habilidad):
    habilidad = Habilidad.objects.get( pk = id_habilidad)

    context = { 'login':True,'habilidad' : habilidad}

    return render(request, 'habilidad.html', context)