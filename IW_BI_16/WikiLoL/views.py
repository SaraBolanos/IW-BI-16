from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

# Create your views here.
from django.http import HttpResponse

from .models import Campeon, Habilidad, Coleccion, Skin


class MainView(View):
    template_name = 'chillaid/index.html'

    def get_context_data(self, **kwargs):
        context = {
            'campeon': Campeon.objects.order_by('nombre'),
            'coleccion': Coleccion.objects.order_by('nombre'),
            'skin': Skin.objects.order_by('precio'),
            'habilidad': Habilidad.objects.order_by('nombre'),
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

# ------ CAMPEONES -----

class CampeonesListView(ListView):
    model = Campeon
    queryset = Campeon.objects.order_by('nombre')
    template_name = 'listaCampeones.html'
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

def detalleCampeones(request,id_campeon):
    campeon = Campeon.objects.get(pk = id_campeon)
    habilidad = Habilidad.objects.order_by('nombre')
    skin = Skin.objects.order_by('nombre')
    context = { 'login':True,'campeon' : campeon, 'habilidades_list' : habilidad, 'skin_list' : skin}

    return render(request, 'detalleCampeon.html', context)

# ------ COLECCIONES ------
class ColeccionesListView(ListView):
    model = Coleccion
    queryset = Coleccion.objects.order_by('nombre')
    template_name = 'coleccion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


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

