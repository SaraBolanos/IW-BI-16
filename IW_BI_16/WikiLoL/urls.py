from django.urls import path
from . import views
from .views import *

urlpatterns = [


   path('Main', views.main, name='Main'),
   path('listaCampeones', CampeonesListView.as_view(), name='listaCamp'),
   path('listaColecciones', ColeccionesListView.as_view(), name='listaCol'),
   path('detalleCampeones/<int:id_campeon>', views.detalleCampeones, name= 'detalleCamp' ),
   #path('listaColecciones', views.listaColecciones, name= 'listaCol' ),
   path('detalleColecciones/<int:id_coleccion>', views.detalleColecciones, name= 'detalleCol' ),
   path('listaSkins', views.listaSkins, name= 'listaSkin' ),
   path('detalleSkins/<int:id_skins>', views.detalleSkins, name= 'detalleSkin' ),
   path('listaHab', views.listaHabilidad, name= 'listaHab' ),
   path('detalleHab/<int:id_habilidad>', views.detalleHabilidad, name= 'detalleHab' ),
   


]