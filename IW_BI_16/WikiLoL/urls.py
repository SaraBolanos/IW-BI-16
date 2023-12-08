from django.urls import path
from . import views
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

   path('Main', MainView.as_view(), name = 'Main'),
   path('listaCampeones', CampeonesListView.as_view(), name='listaCamp'),
   path('listaColecciones', ColeccionesListView.as_view(), name='listaCol'),
   path('detalleCampeones/<int:pk>/', CampeonesDetailView.as_view(), name='detalleCamp'),
   path('detalleColecciones/<int:id_coleccion>', ColeccionesDetailView.as_view(), name= 'detalleCol' ),
   path('listaSkins', views.listaSkins, name= 'listaSkin' ),
   path('detalleSkins/<int:pk>',SkinDetailView.as_view(), name= 'detalleSkin' ),
   path('listaHab', views.listaHabilidad, name= 'listaHab' ),
   path('detalleHab/<int:id_habilidad>', views.detalleHabilidad, name= 'detalleHab' ),
   
   


]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)