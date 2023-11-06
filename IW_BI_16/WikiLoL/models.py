from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Campeon(models.Model):
    nombre = models.CharField(max_length=20)
    class Linea(models.TextChoices):
        TOP = 'TopLane'
        MID = 'MidLane'
        JUNGLE = 'Jungle'
        ADC = 'ADC'
        SUPPORT ='Support'
    linea = models.CharField(max_length=10, choices=Linea.choices, default=Linea.MID)
    class Region(models.TextChoices):
        AGUAS_ESTANCADAS = "Aguas Estancadas"
        CIUDAD_DE_BUNDLE = "Ciudad de Bundle"
        DEMACIA = "Demacia"
        EL_VACIO = "El Vacio"
        FRELJORD = "Freljord"
        ISLAS_DE_LA_SOMBRA = "Islas de la Sombra"
        IXTAL = "Ixtal"
        JONIA = "Jonia"
        NOXUS = "Noxus"
        PILTOVER = "Piltover"
        SHURIMA = "Shurima"
        TARGON = "Targon"
        ZAUN = "Zaun"
        RUNETERRA = "Runeterra"    
    region = models.CharField( max_length=25, choices=Region.choices, default=Region.AGUAS_ESTANCADAS)
    
    añoSalida = models.IntegerField(default = 2009, null = True)

    def __str__(self):
        return self.nombre 
    
    

class Habilidad(models.Model):
    nombre = models.TextField(max_length=40)
    class Ratio(models.IntegerChoices):
        AD = 0, _('Attack Damage')
        AP = 1, _('Ability Power')
        TRUEDAMAGE = 2, _('True damage')
        APAD = 3, _('AP & AD')
        APTD = 4, _('AD & True damage')
    ratio = models.IntegerField(default = 0, choices=Ratio.choices)
    class Tecla(models.IntegerChoices):
        TECLA_Q = 0, _('Tecla Q')
        TECLA_W = 1, _('Tecla W')
        TECLA_E = 2, _('Tecla E')
        TECLA_R = 3, _('Tecla R')
    tecla = models.IntegerField(default=0, choices=Tecla.choices)
    campeon = models.ForeignKey(Campeon, on_delete=models.CASCADE, related_name="habilidades")
    
    def __str__(self):
        return self.nombre 

class Coleccion(models.Model):
    nombre = models.TextField(max_length=50)
    fechaSalida = models.DateField()
    
    def __str__(self):
        return self.nombre 

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
    campeon = models.ForeignKey(Campeon, on_delete=models.CASCADE, related_name="skins_campeon")
    
    def __str__(self):
        return self.nombre 