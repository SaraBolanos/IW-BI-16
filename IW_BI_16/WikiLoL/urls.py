from django.urls import path
from . import views

urlpatterns = [


   path('Main', views.main, name='Main'),
   path('listaCampeones', views.listaCampeones, name= 'listaCamp' ),
   path('detalleCampeones/<int:id_campeon>', views.detalleCampeones, name= 'detalleCamp' ),
   path('listaColecciones', views.listaColecciones, name= 'listaCol' ),
   path('detalleColecciones', views.detalleColecciones, name= 'detalleCol' ),
   path('listaSkins', views.listaSkins, name= 'listaSkin' ),
   path('detalleSkins', views.detalleSkins, name= 'detalleSkin' ),
   path('listaHab', views.listaHabilidad, name= 'listaHab' ),
   path('detalleHab', views.detalleHabilidad, name= 'detalleHab' )


]