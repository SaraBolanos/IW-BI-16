from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Campeon(models.Model):
    nombre = models.CharField(max_length=20)
    class Linea(models.IntegerChoices):
        TOP = 0, _('TopLane')
        MID = 1, _('MidLane')
        JUNGLE = 2, _('Jungle')
        ADC = 3, _('ADC')
        SUPPORT = 4, _('Support')
    linea = models.IntegerField(default = 0, choices = Linea.choices)
    class Region(models.IntegerChoices):
        AGUAS_ESTANCADAS = 0, _('Aguas Estancadas')
        CIUDAD_DE_BUNDLE = 1, _('Ciudad de Bundle')
        DEMACIA = 2, _('Demacia')
        EL_VACIO = 3, _('El Vacio')
        FRELJORD = 4, _('Freljord')
        ISLAS_DE_LA_SOMBRA = 5, _('Islas de la Sombra')
        IXTAL = 6, _('Ixtal')
        JONIA = 7, _('Jonia')
        NOXUS = 8, _('Noxus')
        PILTOVER = 9, _('Piltover')
        SHURIMA = 10, _('Shurima')
        TARGON = 11, _('Targon')
        ZAUN = 12, _('Zaun')
        RUNETERRA = 13, _('Runeterra')
    region = models.IntegerField(default=0, choices = Region.choices)
   
    añoSalida = models.IntegerField(default = 2009, null = True)

    def __str__(self):
        return self.nombre 

class Habilidad(models.Model):
    nombre = models.TextField(max_length=40)
    ratio = models.IntegerField()
    class Tecla(models.IntegerChoices):
        TECLA_Q = 0, _('Tecla Q')
        TECLA_W = 1, _('Tecla W')
        TECLA_E = 2, _('Tecla E')
        TECLA_R = 3, _('Tecla R')
    tecla = models.IntegerField(default=0, choices=Tecla.choices)
    campeon = models.ForeignKey(Campeon, on_delete=models.CASCADE, related_name="habilidades")

class Coleccion(models.Model):
    nombre = models.TextField(max_length=50)
    fechaSalida = models.DateField()
    tematica = models.TextField(max_length=50)

class Skin(models.Model):
    precio = models.IntegerField()
    class Rareza(models.IntegerChoices):
        BASICA = 0, _('Basica')
        UNICA = 1, _('Unica')
        CLASICA = 2, _('Clasica')
        REAL = 3, _('Real')
        IMPERIAL = 4, _('Imperial')
        EPICA = 5, _('Epica')
        LEGENDARIA = 6, _('Legendaria')
        DEFINITIVA = 7, _('Definitiva')
        HEXTECH = 8, _('Hextech')
        LIMITADA = 9, _('Limitada')
        VICTORIOSA = 10, _('Victoriosa')
    rareza = models.IntegerField(default=0, choices=Rareza.choices)
    nombre = models.TextField(max_length=50)
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE, related_name="skins")
