from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

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
    imagen = models.TextField(max_length=100)

    def __str__(self):
        return self.nombre 
    
    def get_absolute_url(self):
        return reverse('detalleCamp', args=[str(self.id)])
    
    

class Habilidad(models.Model):
    nombre = models.TextField(max_length=40)
    class Ratio(models.TextChoices):
        AD = 'Attack Damage'
        AP ='Ability Power'
        TRUEDAMAGE ='True damage'
        APAD = 'AP & AD'
        APTD = 'AD & True damage'
    ratio = models.CharField(max_length=25, choices=Ratio.choices, default=Ratio.AP)
    class Tecla(models.TextChoices):
        TECLA_Q ='Tecla Q'
        TECLA_W ='Tecla W'
        TECLA_E ='Tecla E'
        TECLA_R ='Tecla R'
    tecla = models.CharField(max_length=15, choices=Tecla.choices, default=Tecla.TECLA_Q)
    campeon = models.ForeignKey(Campeon, on_delete=models.CASCADE, related_name="habilidades")
    imagen = models.TextField(max_length=100)
    def __str__(self):
        return self.nombre 

class Coleccion(models.Model):
    nombre = models.TextField(max_length=50)
    fechaSalida = models.DateField()
    
    def __str__(self):
        return self.nombre 
    def get_absolute_url(self):
        return reverse('detalleCol', args=[str(self.id)])

class Skin(models.Model):
    precio = models.IntegerField()
    class Rareza(models.TextChoices):
        BASICA = 'Basica'
        UNICA = 'Unica'
        EPICA = 'Epica'
        LEGENDARIA ='Legendaria'
        DEFINITIVA = 'Definitiva'
        MITICA ='Mitica'
    rareza = models.CharField(max_length=15, choices=Rareza.choices, default=Rareza.BASICA)
    nombre = models.TextField(max_length=50)
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE, related_name="skins")
    campeon = models.ForeignKey(Campeon, on_delete = models.CASCADE, default=0)
    imagen = models.TextField(max_length=100)
    def __str__(self):
        return self.nombre 