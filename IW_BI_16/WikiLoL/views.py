from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.views.generic.detail import DetailView

# Create your views here.
from django.http import HttpResponse

from .models import Campeon, Habilidad, Coleccion, Skin


class MainView(View):
    template_name = 'chillaid/main.html'

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
    template_name = 'chillaid/pages/gallery.html'
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class CampeonesDetailView(DetailView):
    model = Campeon
    template_name='chillaid/campeondetalles.html'
    
     # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(CampeonesDetailView,
             self).get_context_data(*args, **kwargs)
        # add extra field 
        campeon = self.object
        habilidades = Habilidad.objects.filter(campeon=campeon)[:4]
        skins = Skin.objects.filter(campeon=campeon)[:5]
        context['habilidades'] = habilidades   
        context ['skins'] = skins
        return context
    

# ------ COLECCIONES ------
class ColeccionesListView(ListView):
    model = Coleccion
    queryset = Coleccion.objects.order_by('nombre')
    template_name = 'chillaid/listaColecciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class ColeccionesDetailView(DetailView):
    model = Coleccion
    template_name = 'chillaid/detalleColeccion.html'
    def get_context_data(self,*args, **kwargs):
        context = super(ColeccionesDetailView,
            self).get_context_data(*args, **kwargs)
        coleccion = self.object
        skins = Skin.objects.filter(coleccion=coleccion)
        context['skins'] = skins
        return context
    def get_object(self, queryset=None):
        id_coleccion = self.kwargs.get('id_coleccion')
        return Coleccion.objects.get(pk=id_coleccion)
        
    


# ------ SKINS ------
class SkinDetailView(DetailView):
    model = Skin
    template_name = 'chillaid/detalleSkin.html'
    def get_context_data(self,*args, **kwargs):
        context = super(SkinDetailView,
            self).get_context_data(*args, **kwargs)
        
        return context

def listaSkins(request):
    skins = Skin.objects.order_by('nombre')
    context =  {'skin_list' : skins}
    return render(request, 'listaSkins.html', context)

# ------ HABILIDADES ------
def listaHabilidad(request):
    habilidades = Habilidad.objects.order_by('nombre')
    context =  {'habilidades_list':habilidades}
    return render(request, 'habilidad.html', context)


def detalleHabilidad(request,id_habilidad):
    habilidad = Habilidad.objects.get( pk = id_habilidad)

    context = { 'login':True,'habilidad' : habilidad}

    return render(request, 'habilidad.html', context)

