from django.urls import path
from . import views

urlpatterns = [


   path('listadoDeCampeones', views.listaCampeones, name="listaC"),



]