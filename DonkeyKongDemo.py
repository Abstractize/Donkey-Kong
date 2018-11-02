"""
Instituto Tecnológico de Costa Rica
Ingeniería en Computadores
Proyecto #2
Lenguaje: Python 3.6.1
Versión: 1.0
Fecha de última modificación: 5/18/2017
Estudiante: Gabriel Abarca Aguiar
Carné:2017110442
"""
"Versión Corregida en los puntajes"
# Módulos
import sys, pygame #aquí se importa la biblioteca
import random
from pygame.locals import *
import time as tiempo
# Constantes Numéricas
WIDTH = 640
HEIGHT = 730
life=2
SCORE=0
#Contadores
cont=6
cont2=6
cont3=6
cont4=6
#Booleanos del Inicio
Cunt=1
Cunt2=0
Booleano1=False
Booleano2=False
Booleano3=False
Booleano4=False
#Booleanos de Game Over
Booleano21=False
Booleano22=False
name=""
Write=True
#Barriles
Barro1=False
Barro2=False
Barro3=False
Barro4=False
Barro5=False
Barro6=False
#Interruptores de Pausa
pause=False
ContP=1
BooleanoP1=False
BooleanoP2=False
BooleanoP3=False
on_off="off"
Vol_off=False
#Mejores 5 Scores
Score1=0
Score2=0
Score3=0
Score4=0
Score5=0
Score6=0
Score7=0
Score8=0
Score9=0
Score10=0
# Objetos
# ---------------------------------------------------------------------
class Background(pygame.sprite.Sprite):#Fondo de la pantalla principal
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/stage1.png")
class Inicio(pygame.sprite.Sprite):#Fondo de la pantalla de Inicio
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("Images/Inicio.png",True)
class Instructions(pygame.sprite.Sprite):#Cartel de Instrucciones
        def __init__(self):#Self y detalles como la imagen
                global Booleano2
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("Images/Instructions.png",True)
        def update(self):
                if Booleano2==True:#Cambio de imagen para entrar a las instrucciones
                        self.image = load_image("Images/Instructions1.png",True)
                else:
                        self.image = load_image("Images/Instructions.png",True)
class Starto(pygame.sprite.Sprite):#Cartel de Start
        def __init__(self):#Imagen
                global Booleano1
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("Images/Start.png",True)
        def update(self):#Cambio de imagen
                if Booleano1==True:
                        self.image = load_image("Images/Start1.png",True)
                else:
                        self.image = load_image("Images/Start.png",True)
class Pausa(pygame.sprite.Sprite):#Letrero del menu de Pausa
        def __init__(self):#Imagen
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/pause.png",True)
                self.rect=self.image.get_rect()
                self.rect.centerx=WIDTH+40000
                self.rect.centery=HEIGHT+20000
        def update(self):#Teclado durante el menu de Pausa
                global pause, ContP, BooleanoP1, BooleanoP2, BooleanoP3
                if pause==True:
                        self.rect.centerx=WIDTH/2
                        self.rect.centery=HEIGHT/2
                        BooleanoP1=True
                        if ContP>=4:
                                ContP=1
                        if ContP<1:
                               ContP=3
                        if ContP==1:
                                BooleanoP1=True
                                BooleanoP2=False
                                BooleanoP3=False
                        if ContP==2:
                                BooleanoP1=False
                                BooleanoP2=True
                                BooleanoP3=False
                        if ContP==3:
                                BooleanoP1=False
                                BooleanoP2=False
                                BooleanoP3=True
                if pause==False:
                        self.rect.centerx=WIDTH+40000
                        self.rect.centery=HEIGHT+20000
class Yes(pygame.sprite.Sprite):#Cartel de Yes
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("Images/Yes.png")
        def update(self):
                global Booleano21
                if Booleano21==True:
                        self.image = load_image("Images/Yes1.png")

                else:
                        self.image = load_image("Images/Yes.png")
class No(pygame.sprite.Sprite):#Cartel de No
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("Images/No.png")
        def update(self):
                global Booleano22
                if Booleano22==True:
                        self.image = load_image("Images/No1.png")

                else:
                        self.image = load_image("Images/No.png")
class About(pygame.sprite.Sprite):#Cartel de About
        global Booleano3
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("Images/About.png",True)
        def update(self):
                if Booleano3==True:
                        self.image = load_image("Images/About1.png",True)
                else:
                        self.image = load_image("Images/About.png",True)
class Exit(pygame.sprite.Sprite):#Cartel de Exit
        global Booleano4
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("Images/Exit.png",True)
        def update(self):
                if Booleano4==True:
                        self.image = load_image("Images/Exit1.png",True)
                else:
                        self.image = load_image("Images/Exit.png",True)
class DK (pygame.sprite.Sprite):#Donkey Kong
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/DonkeyKongSprites1.png",True)
                self.rect = self.image.get_rect()
                self.rect.x=40
                self.rect.y=176
        def spriteDK(self):#Sprites de DK
                global cont2
                p=6
                if cont2==p:
                        self.image = load_image("images/DonkeyKongSprites1.png",True)
                if cont2==p*2:
                        self.image = load_image("images/DonkeyKongSprites2.png",True)
                if cont2==p*3:
                        self.image = load_image("images/DonkeyKongSprites3.png",True)
                if cont2==p*4:
                        self.image = load_image("images/DonkeyKongSprites4.png",True)
                if cont2==p*5:
                        self.image = load_image("images/DonkeyKongSprites5.png",True)
                if cont2==p*6:
                        self.image = load_image("images/DonkeyKongSprites6.png",True)
                        cont2=0
        def colisiones(self,protagonista):#Colisión con Mario
                if pygame.sprite.collide_rect(self, protagonista):
                        #print (0)
                        return vidas()
                
class Pauline(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/pauline.png",True)
                self.image_inv = pygame.transform.flip(self.image,True,False)
                self.rect = self.image.get_rect()
                self.rect.x =250
                self.rect.y =110
        def colisiones(self,protagonista):#Colisión con Mario
                global SCORE,cont4,life
                if pygame.sprite.collide_rect(self, protagonista):
                        SCORE+=life*1500
                        SCORE+=1500
                        cont4=6
                        return win()
class Mario (pygame.sprite.Sprite):
        def __init__(self):
                global xixf, i
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/mario1.png",True)
                self.image_inv = pygame.transform.flip(self.image,True,False)
                self.rect = self.image.get_rect()
                #Posición de Mario
                self.rect.x=36 #Posición de Mario en X
                self.xi=0 #Posición inicial de Mario en X, para algunas funciones de movimiento
                self.rect.y=620 #Posición de Mario en Y
                self.yi=0 #Posición inicial de Mario en Y, para algunas funciones de movimiento
                #Interruptores
                self.direc=True
                self.salto = False
                self.salto_Par=False
                self.bajada=False
                self.bajada_Par=False
                self.salto_in=False
                self.bajada_in=False
                self.subir=False
                self.punto=False
                self.subirspr=False
                self.saltopuntos=False
       
        def movimiento_Y(self):
                #Restricciones de Pantalla
                iY=-40
                iX=20
                
                f2=67
                f3=93
                f4=49
                f5=116
                f6=477
                f7=137
                if self.rect.x<=0:
                        self.rect.x=1
                if self.rect.x>=WIDTH-24:
                        self.rect.x=WIDTH-24
                if self.rect.y<=0:
                        self.rect.y=0
                #Acceso a self.subir por las escaleras
                EscalerasX1=[17,18,19,20,21,22,23,24]
                EscalerasX2=[40,41,42,43,44,45,46,47,48,49,50]
                EscalerasX3=[170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,221,222,223,224,225,226,227,228,229,230,231,232,234,235]
                EscalerasX4=[580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600]
                EscalerasX5=[515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535]
                EscalerasX6=[580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600]
                EscalerasX7=[445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465]
                EscalerasX8=[385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405]
                EscalerasX9=[350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370]
                if self.rect.x==comparador_de_lista(EscalerasX1,self.rect.x,0) and self.rect.y==622:
                        self.xi=self.rect.x
                        self.punto=True
                if self.rect.x==comparador_de_lista(EscalerasX2,self.rect.x,0) and self.rect.y==508:
                        self.xi=self.rect.x
                        self.punto=True
                if self.rect.x==comparador_de_lista(EscalerasX3,self.rect.x,0) and self.rect.y==552:
                        self.xi=self.rect.x
                        self.punto=True
                if self.rect.x==comparador_de_lista(EscalerasX4,self.rect.x,0) and self.rect.y==552:
                        self.xi=self.rect.x
                        self.punto=True
                if self.rect.x==comparador_de_lista(EscalerasX5,self.rect.x,0) and self.rect.y==464:
                        self.xi=self.rect.x
                        self.punto=True
                if self.rect.x==comparador_de_lista(EscalerasX6,self.rect.x,0) and self.rect.y==370:
                        self.xi=self.rect.x
                        self.punto=True
                if self.rect.x==comparador_de_lista(EscalerasX7,self.rect.x,0) and self.rect.y==302:
                        self.xi=self.rect.x
                        self.punto=True
                if self.rect.x==comparador_de_lista(EscalerasX8,self.rect.x,0) and self.rect.y==416:
                        self.xi=self.rect.x
                        self.punto=True
                if self.rect.x==comparador_de_lista(EscalerasX9,self.rect.x,0) and self.rect.y==210:
                        self.xi=self.rect.x
                        self.punto=True
                #Subir por la escaleras
                if self.subir==True:
                        self.rect.y-=1
                        self.subir=False
                #Floor2
                        if f2>self.rect.x>0 and self.rect.y==662+iY:#Ubicación del Sprite en X+Ancho en pixeles del sprite>self.rect.x>Ubicacion del Sprite, Pos Y del sprite
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                        if f2>self.rect.x>0 and self.rect.y==548+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                        if f2>self.rect.x>0 and self.rect.y==388+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                        if 181+f2>self.rect.x>181-iX and self.rect.y==592+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                        if 341+f2>self.rect.x>341-iX and self.rect.y==662+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                        if 568+f2>self.rect.x>568-iX and self.rect.y==592+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                        if 365+f2>self.rect.x>365-iX and self.rect.y==362+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                #Floor3
                        if 158+f3>self.rect.x>158-iX and self.rect.y==388+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                #Floor4
                        if 430+f4>self.rect.x>420-iX and self.rect.y==638+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                        if 499+f4>self.rect.x>489-iX and self.rect.y==616+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                        if 589+f4>self.rect.x>579-iX and self.rect.y==524+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                        if 523+f4>self.rect.x>523-iX and self.rect.y==504+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                        if 453+f4>self.rect.x>443-iX and self.rect.y==478+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                        if 385+f4>self.rect.x>375-iX and self.rect.y==456+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                        if 454+f4>self.rect.x>444-iX and self.rect.y==342+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                        if 523+f4>self.rect.x>513-iX and self.rect.y==320+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                        if 592+f4>self.rect.x>582-iX and self.rect.y==298+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                #Floor5
                        if 520+f5>self.rect.x>510-iX and self.rect.y==410+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                #Floor6
                        if f6>self.rect.x>0 and self.rect.y==250+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                #Floor7
                        if f7+250>self.rect.x>250-iX and self.rect.y==160+iY:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
                        #Comparador de la X para que no tenga acceso al self.subir infinito
                        if self.rect.x>self.xi+2 or self.xi-2>self.rect.x:
                                self.punto=False
                                self.subir=False
                                self.subirspr=False
        #Caída de las plataformas
                if self.salto_in==True:#Movimiento Semiparabólico
                        self.subirspr=False
                        if self.bajada_in==False:
                                self.rect.y-=0                 
                        if self.bajada_in==True:
                                if self.rect.y%2!=0:
                                        self.rect.y=self.rect.y-1
                                self.rect.y+=2
                        if self.rect.y==self.yi:
                                self.yi=self.rect.y
                                self.bajada_in=True
                        #Floor1
                        if self.rect.y==708+iY:#46Px de diferecia desde el centro del sprite hasta la plataforma
                                self.bajada_in=False
                                self.salto_in=False
                        #Floor2
                        if f2>self.rect.x>=0 and self.rect.y==662+iY:#Ubicación del Sprite en X+Ancho en pixeles del sprite>self.rect.x>Ubicacion del Sprite, Pos Y del sprite
                                self.bajada_in=False
                                self.salto_in=False
                        if f2>self.rect.x>=0 and self.rect.y==548+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        if f2>self.rect.x>=0 and self.rect.y==388+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        if 181+f2>self.rect.x>181-iX and self.rect.y==592+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        if 341+f2>self.rect.x>341-iX and self.rect.y==662+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        if 568+f2>self.rect.x>568-iX and self.rect.y==592+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        if 365+f2>self.rect.x>365-iX and self.rect.y==366+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        #Floor3
                        if 158+f3>self.rect.x>158-iX and self.rect.y==388+iY:
                                self.bajada_in=False
                                self.salto_in=False
                       #Floor4
                        if 430+f4>self.rect.x>430-iX and self.rect.y==638+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        if 499+f4>self.rect.x>499-iX and self.rect.y==616+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        if 589+f4>self.rect.x>589-iX and self.rect.y==524+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        if 523+f4>self.rect.x>523-iX and self.rect.y==504+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        if 453+f4>self.rect.x>453-iX and self.rect.y==478+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        if 385+f4>self.rect.x>385-iX and self.rect.y==456+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        if 454+f4>self.rect.x>454-iX and self.rect.y==342+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        if 523+f4>self.rect.x>523-iX and self.rect.y==320+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        if 592+f4>self.rect.x>592-iX and self.rect.y==298+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        #Floor5
                        if 520+f5>self.rect.x>520-iX and self.rect.y==410+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        #Floor6
                        if f6>self.rect.x>0 and self.rect.y==250+iY:
                                self.bajada_in=False
                                self.salto_in=False
                        #Floor7
                        if f7+250>self.rect.x>250-iX and self.rect.y==160+iY:
                                self.bajada_in=False
                                self.salto_in=False
        #Salto Normal
                if self.salto==True:#Caída Libre
                        self.saltopuntos=True
                        self.subirspr=False
                        if self.bajada==False:
                                self.rect.y-=2                 
                        if self.bajada==True:
                                if self.rect.y%2!=0:
                                        self.rect.y=self.rect.y-1
                                self.rect.y+=2
                        if self.rect.y==self.yi-70:#Sube 70Px
                                self.yi=self.rect.y
                                self.bajada=True
                        #Floor1
                        if self.rect.y==708+iY:#40Px de diferecia desde el centro del sprite hasta la plataforma
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        #Todos los Floor2 (if tipo de base>self.rect.x>inicio de la base)
                        if f2>self.rect.x>=0 and self.rect.y==662+iY:#Ubicación del Sprite en X+Ancho en pixeles del sprite>self.rect.x>Ubicacion del Sprite, Pos Y del sprite
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        if f2>self.rect.x>=0 and self.rect.y==548+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        if f2>self.rect.x>=0 and self.rect.y==388+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        if 181+f2>self.rect.x>181-iX and self.rect.y==592+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        if 341+f2>self.rect.x>341-iX and self.rect.y==662+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        if 568+f2>self.rect.x>568-iX and self.rect.y==592+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        if 365+f2>self.rect.x>365-iX and self.rect.y==366+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        #Floor3
                        if 158+f3>self.rect.x>158-iX and self.rect.y==388+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                       #Floor4
                        if 430+f4>self.rect.x>420-iX and self.rect.y==638+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        if 499+f4>self.rect.x>489-iX and self.rect.y==616+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        if 589+f4>self.rect.x>579-iX and self.rect.y==524+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        if 523+f4>self.rect.x>510-iX and self.rect.y==504+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        if 453+f4>self.rect.x>443-iX and self.rect.y==478+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        if 385+f4>self.rect.x>375-iX and self.rect.y==456+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        if 454+f4>self.rect.x>444-iX and self.rect.y==342+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        if 523+f4>self.rect.x>513-iX and self.rect.y==320+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        if 592+f4>self.rect.x>582-iX and self.rect.y==298+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        #Floor5
                        if 520+f5>self.rect.x>510-iX and self.rect.y==410+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        #Floor6
                        if f6>self.rect.x>0 and self.rect.y==250+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
                        #Floor7
                        if f7+250>self.rect.x>250-iX and self.rect.y==160+iY:
                                self.bajada=False
                                self.salto=False
                                self.saltopuntos=False
        #Salto Curveado
                #Movimiento parabólico a la derecha
                if self.salto_Par==True and self.direc==True:           
                        self.subirspr=False
                        self.saltopuntos=True
                   
                        if self.bajada_Par==False:
                                self.rect.y-=2
                                self.rect.x+=1
                       
                        if self.bajada_Par==True:
                                if self.rect.y%2!=0:
                                        self.rect.y=self.rect.y-1
                                self.rect.y+=2
                                self.rect.x+=1
                           
                        if self.rect.y==self.yi-70:
                                self.yi=self.rect.y
                                self.bajada_Par=True
                        iY=-40
                        #Floor1
                        if self.rect.y==708+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False

                        #Todos los Floor2
                        if f2>self.rect.x>=0 and self.rect.y==662+iY:#Ubicación del Sprite en X+Ancho en pixeles del sprite>self.rect.x>Ubicacion del Sprite, Pos Y del sprite
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if f2>self.rect.x>=0 and self.rect.y==548+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if f2>self.rect.x>=0 and self.rect.y==388+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 181+f2>self.rect.x>181-iX and self.rect.y==592+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 341+f2>self.rect.x>341-iX and self.rect.y==662+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 568+f2>self.rect.x>568-iX and self.rect.y==592+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 365+f2>self.rect.x>365-iX and self.rect.y==366+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        #Floor3
                        if 158+f3>self.rect.x>158-iX and self.rect.y==388+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                       #Floor4
                        if 430+f4>self.rect.x>430-iX and self.rect.y==638+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 499+f4>self.rect.x>499-iX and self.rect.y==616+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 589+f4>self.rect.x>589-iX and self.rect.y==524+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 523+f4>self.rect.x>523-iX and self.rect.y==504+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 453+f4>self.rect.x>453-iX and self.rect.y==478+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 385+f4>self.rect.x>385-iX and self.rect.y==456+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 454+f4>self.rect.x>454-iX and self.rect.y==342+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 523+f4>self.rect.x>523-iX and self.rect.y==320+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 592+f4>self.rect.x>592-iX and self.rect.y==298+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        #Floor5
                        if 520+f5>self.rect.x>520-iX and self.rect.y==410+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        #Floor6
                        if f6>self.rect.x>0 and self.rect.y==250+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        #Floor7
                        if f7+250>self.rect.x>250-iX and self.rect.y==160+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                #Movimiento Parabólico a la Izquierda   
                elif self.salto_Par==True and self.direc==False:
                        self.subirspr=False
                        self.saltopuntos=True
                        if self.bajada_Par==False:
                                self.rect.y-=2
                                self.rect.x-=1
                               
                        if self.bajada_Par==True:
                                if self.rect.y%2!=0:
                                        self.rect.y=self.rect.y-1
                                self.rect.y+=2
                                self.rect.x-=1
                        if self.rect.y==self.yi-70:
                                self.yi=self.rect.y
                                self.bajada_Par=True           
                    #Floor1
                        if self.rect.y==708+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False

                        #Todos los Floor2
                        if f2>self.rect.x>=0 and self.rect.y==662+iY:#Ubicación del Sprite en X+Ancho en pixeles del sprite>self.rect.x>Ubicacion del Sprite, Pos Y del sprite
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if f2>self.rect.x>=0 and self.rect.y==548+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if f2>self.rect.x>=0 and self.rect.y==388+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 181+f2>self.rect.x>181-iX and self.rect.y==592+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 341+f2>self.rect.x>341-iX and self.rect.y==662+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 568+f2>self.rect.x>568-iX and self.rect.y==592+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 365+f2>self.rect.x>365-iX and self.rect.y==366+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        #Floor3

                        if 158+f3>self.rect.x>158-iX and self.rect.y==388+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                       #Floor4
                        if 430+f4>self.rect.x>430-iX and self.rect.y==638+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 499+f4>self.rect.x>499-iX and self.rect.y==616+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 589+f4>self.rect.x>589-iX and self.rect.y==524+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 523+f4>self.rect.x>523-iX and self.rect.y==504+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 453+f4>self.rect.x>453-iX and self.rect.y==478+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 385+f4>self.rect.x>385-iX and self.rect.y==456+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 454+f4>self.rect.x>454-iX and self.rect.y==342+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 523+f4>self.rect.x>523-iX and self.rect.y==320+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        if 592+f4>self.rect.x>592-iX and self.rect.y==298+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        #Floor5
                        if 520+f5>self.rect.x>520-iX and self.rect.y==410+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        #Floor6
                        if f6>self.rect.x>0 and self.rect.y==250+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
                        #Floor7
                        if f7+250>self.rect.x>250-iX and self.rect.y==160+iY:
                                self.bajada_Par=False
                                self.salto_Par=False
                                self.saltopuntos=False
        def keyboard(self):#Movimientos de Mario
                global cont, pause #Variables Globales
   
                teclado = pygame.key.get_pressed()
                if pause==False:
                        if teclado[K_w] and teclado[K_d] and self.salto_Par==False and self.salto_in==False and self.salto==False:
                                self.yi=self.rect.y
                                self.salto_Par=True
                                self.salto=False
                                self.bajada=False
                        elif teclado[K_w] and teclado[K_a] and self.salto_Par==False and self.salto_in==False and self.salto==False:
                                self.yi=self.rect.y
                                self.salto_Par=True
                                self.salto=False
                                self.bajada=False
                        elif teclado[K_a]and self.salto==False and self.salto_Par==False:
                                self.yi=self.rect.y
                                self.rect.x-=1
                                cont+=1
                                self.direc=False
                                self.salto_in=True
                        elif teclado[K_d]and self.salto==False and self.salto_Par==False:
                                self.yi=self.rect.y
                                self.rect.x+=1
                                cont+=1
                                self.direc=True
                                self.salto_in=True
                        elif teclado[K_w] and self.salto==False and self.salto_Par==False and self.salto_in==False and self.punto==False:
                                self.yi=self.rect.y
                                self.salto=True
                        elif teclado[K_w] and self.salto==False and self.salto_Par==False and self.salto_in==False and self.punto==True:
                                self.yi=self.rect.y
                                self.subir=True
                                self.subirspr=True
                        else :
                                cont=6
                 
                return
        def sprites(self):
                #Movimiento Sprites de Mario
                #Subir por las Escaleras
                if self.subirspr==True:
                        self.image=load_image("images/banana.png",True)
                #Movimiento Semiparabólico
                if self.salto_in==True:
                        if self.direc==True:
                                self.image=load_image("images/mario1.png",True)
                        if self.direc==False:
                                self.image=load_image("images/mario1i.png",True)
                #Salto Normal
                if self.salto==True:#Caída Libre
                        if self.direc==True:
                                self.image=load_image("images/mario5.png",True)
                        if self.direc==False:
                                self.image=load_image("images/mario5i.png",True)
                #Salto Parabólico
                if self.salto_Par==True and self.direc==True:#Sprites de movimiento Parabólico a la Derecha          
                        self.image=load_image("images/mario5.png",True)
                elif self.salto_Par==True and self.direc==False:#Sprites de movimiento Parabólico a la Izquierda          
                        self.image=load_image("images/mario5i.png",True)
        def sprite(self):#Animación
                p=6
                if self.direc==True and self.subir==False:
                        global cont
                        if cont==p:
                                self.image=load_image("images/mario1.png",True)
                        if cont==p*2:
                                self.image=load_image("images/mario2.png",True)
                        if cont==p*3:
                                self.image=load_image("images/mario3.png",True)
                        if cont==p*4:
                                self.image=load_image("images/mario4.png",True)
                        if cont==p*5:
                                self.image=load_image("images/mario5.png",True)
                        if cont==p*6:
                                self.image=load_image("images/mario6.png",True)
                                cont=0
                elif self.direc==False and self.subir==False:
                        if cont==p:
                                self.image=load_image("images/mario1i.png",True)
                        if cont==p*2:
                                self.image=load_image("images/mario2i.png",True)
                        if cont==p*3:
                                self.image=load_image("images/mario3i.png",True)
                        if cont==p*4:
                                self.image=load_image("images/mario4i.png",True)
                        if cont==p*5:
                                self.image=load_image("images/mario5i.png",True)
                        if cont==p*6:
                                self.image=load_image("images/mario6i.png",True)
                                cont=0
                return
        def puntos(self,barriles):#Acumulador de Puntos
                global SCORE
                if self.saltopuntos == True:
                        if barriles[0].rect.centery-80<=self.rect.centery<=barriles[0].rect.centery:#Valida la posición en Y de Mario arriba del barril
                                if barriles[0].rect.centerx<=self.rect.centerx<=barriles[0].rect.centerx+2:#Valida la posiciones en X iguales
                                        SCORE+=100
                        if barriles[1].rect.centerx<=self.rect.centerx<=barriles[1].rect.centerx+1:
                                if barriles[1].rect.centery-80<=self.rect.centery<=barriles[1].rect.centery:
                                        SCORE+=100
                        if barriles[2].rect.centerx<=self.rect.centerx<=barriles[2].rect.centerx+1:
                                if barriles[2].rect.centery-80<=self.rect.centery<=barriles[2].rect.centery:
                                        SCORE+=100
                        if barriles[3].rect.centerx<=self.rect.centerx<=barriles[3].rect.centerx+1:
                                if barriles[3].rect.centery-80<=self.rect.centery<=barriles[3].rect.centery:
                                        SCORE+=100
                        if barriles[4].rect.centerx<=self.rect.centerx<=barriles[4].rect.centerx+1:
                                if barriles[4].rect.centery-80<=self.rect.centery<=barriles[4].rect.centery:
                                        SCORE+=100
                        if barriles[5].rect.centerx<=self.rect.centerx<=barriles[5].rect.centerx+1:
                                if barriles[5].rect.centery-80<=self.rect.centery<=barriles[5].rect.centery:
                                        SCORE+=100
                
class Barril1 (pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Barriles1_001.png",True)
                self.image_inv = pygame.transform.flip(self.image,True,False)
                self.rect = self.image.get_rect()
                self.time = 0
                #Barril1
                self.rect.x=0
                self.rect.y=-50
                self.caidabarril=False
                self.ladosbarrild=False
                self.ladosbarrili=False
        def IA(self):
                global WIDTH,HEIGHT
                global Barro1
                if Barro1==True:
                        self.rect.x=100
                        self.rect.y=219
                        Barro1=False
                if self.caidabarril==True:
                        self.rect.y+=1
                if self.ladosbarrild==True:
                        self.ladosbarrili=False
                        self.rect.x+=1
                if self.ladosbarrili==True:
                        self.ladosbarrild=False
                        self.rect.x-=1
                iY=-31
                iX=29
                f2=67
                f3=93
                f4=49
                f5=116
                f6=477
                f7=137
                #Floor1
                if WIDTH>self.rect.x>0 and self.rect.y==708+iY:
                        self.caidabarril=False
                if self.rect.x==WIDTH-iX and self.rect.y==708+iY:
                        self.caidabarril=True
                if self.rect.x==0 and self.rect.y==708+iY:
                        self.caidabarril=True        
                if self.rect.y==HEIGHT:
                        self.rect.x=100
                        self.rect.y=219
                #Floor2
                if f2>self.rect.x>0 and self.rect.y==662+iY:#Ubicación del Sprite en X+Ancho en pixeles del sprite>MposX>Ubicacion del Sprite, Pos Y del sprite
                        self.caidabarril=False
                if self.rect.x==f2+1 and self.rect.y==662+iY:
                        self.caidabarril=True
                if f2>self.rect.x>0 and self.rect.y==548+iY:
                        self.caidabarril=False
                if f2>self.rect.x>0 and self.rect.y==388+iY:
                        self.caidabarril=False
                if 181+f2>self.rect.x>181-iX and self.rect.y==592+iY:
                        self.caidabarril=False
                if 341+f2>self.rect.x>341-iX and self.rect.y==662+iY:
                        self.caidabarril=False
                if 568+f2>self.rect.x>568-iX and self.rect.y==592+iY:
                          self.caidabarril=False
                if 365+f2>self.rect.x>365-iX and self.rect.y==366+iY:
                        self.caidabarril=False
                if self.rect.x==365-iX and self.rect.y==366+iY:
                        self.caidabarril=True
                if self.rect.x==365+f2+1 and self.rect.y==366+iY:
                        self.caidabarril=True
                #Floor3
                if 158+f3>self.rect.x>158-iX and self.rect.y==388+iY:
                        self.caidabarril=False
                if self.rect.x==158-iX and self.rect.y==388+iY:
                        self.caidabarril=True
                if self.rect.x==158+f4+1 and self.rect.y==388+iY:
                        self.caidabarril=True
                #Floor4
                f4y=22
                #1
                if 430+f4>self.rect.x>430-iX and self.rect.y==638+iY:
                        self.caidabarril=False
                #2
                if 499+f4>self.rect.x>499-iX and self.rect.y==616+iY:
                        self.caidabarril=False
                #3
                if 589+f4>self.rect.x>589-iX and self.rect.y==524+iY:
                        self.caidabarril=False
                #4
                if 523+f4>self.rect.x>523-iX and self.rect.y==504+iY:
                        self.caidabarril=False
                #5
                if 453+f4>self.rect.x>453-iX and self.rect.y==478+iY:
                        self.caidabarril=False
                #6
                if 385+f4>self.rect.x>385-iX and self.rect.y==456+iY:
                        self.caidabarril=False
                #7
                if 454+f4>self.rect.x>454-iX and self.rect.y==342+iY:
                        self.caidabarril=False
                if self.rect.x==454-iX and self.rect.y==342+iY:
                        self.caidabarril=True
                if self.rect.x==454+f4+1 and self.rect.y==342+iY:
                        self.caidabarril=True
                if self.rect.x==454-iX and 342+iY<=self.rect.y<=342+f4y+iY:
                        self.ladosbarrild=False
                        self.ladosbarrili=True
                #8
                if 523+f4>self.rect.x>523-iX and self.rect.y==320+iY:
                        self.caidabarril=False
                if self.rect.x==523-iX and self.rect.y==320+iY:
                        self.caidabarril=True
                if self.rect.x==523+f4+1 and self.rect.y==320+iY:
                        self.caidabarril=True
                if self.rect.x==523-iX and 320+iY<=self.rect.y<=320+f4y+iY:
                        self.ladosbarrild=False
                        self.ladosbarrili=True
                
                #9
                if 592+f4>self.rect.x>592-iX and self.rect.y==298+iY:
                        self.caidabarril=False
                if self.rect.x==592-iX and 298+iY<=self.rect.y<=298+f4y+iY:
                        self.ladosbarrild=False
                        self.ladosbarrili=True
                #Floor5
                f5y=24
                if 520+f5>self.rect.x>520-iX and self.rect.y==410+iY:
                        self.caidabarril=False
                if self.rect.x==520-1-iX and self.rect.y==410+iY:
                        self.caidabarril=True
                #Floor6
                if f6>self.rect.x>0 and self.rect.y==250+iY:
                        self.caidabarril=False
                        self.ladosbarrild=True
                if self.rect.x==f6+1 and self.rect.y==250+iY:
                        self.caidabarril=True
                #Floor7
                if f7+250>self.rect.x>250-iX and self.rect.y==160+iY:
                        self.caidabarril=False
                if self.rect.x==250-iX and self.rect.y==160+iY:
                        self.caidabarril=True
                if self.rect.x==250+f7+1 and self.rect.y==160+iY:
                        self.caidabarril=True
                #Marcos de la Pantalla
                if self.rect.x<=0:
                        self.ladosbarrili=False
                        self.ladosbarrild=True
                if self.rect.x>=WIDTH-iX:
                        self.ladosbarrild=False
                        self.ladosbarrili=True
        def sprites(self):
                global cont3
                p=6
                if cont3==p:
                        self.image=load_image("images/Barriles1_001.png",True)
                if cont3==p*2:
                        self.image=load_image("images/Barriles1_002.png",True)
                if cont3==p*3:
                        self.image=load_image("images/Barriles1_003.png",True)
                if cont3==p*4:
                        self.image=load_image("images/Barriles1_004.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_001.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_002.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_003.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_004.png",True)
                        cont3=0   
                return
        def colisiones(self,protagonista):
                if pygame.sprite.collide_rect(self, protagonista):
                        global cont4
                        cont4=6
                        #print (0)
                        return vidas()
class Barril2 (pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Barriles1_001.png",True)
                self.image_inv = pygame.transform.flip(self.image,True,False)
                self.rect = self.image.get_rect()
                #Barril2
                self.rect.x=0
                self.rect.y=-50
                self.caidabarril2=False
                self.ladosbarrild2=False
                self.ladosbarrili2=False
        def IA2(self):
                global Barro2
                if Barro2==True:
                        self.rect.x=100
                        self.rect.y=219
                        Barro2=False
                if self.caidabarril2==True:
                        self.rect.y+=1
                if self.ladosbarrild2==True:
                        self.ladosbarrili2=False
                        self.rect.x+=1
                if self.ladosbarrili2==True:
                        self.ladosbarrild2=False
                        self.rect.x-=1
                iY=-31
                iX=29
                f2=67
                f3=93
                f4=49
                f5=116
                f6=477
                f7=137
                #Floor1
                if WIDTH>self.rect.x>0 and self.rect.y==708+iY:
                        self.caidabarril2=False
                if self.rect.x==WIDTH-iX and self.rect.y==708+iY:
                        self.caidabarril2=True
                if self.rect.x==0 and self.rect.y==708+iY:
                        self.caidabarril2=True        
                if self.rect.y==HEIGHT:
                        self.rect.x=100
                        self.rect.y=219
                #Floor2
                if f2>self.rect.x>0 and self.rect.y==662+iY:#Ubicación del Sprite en X+Ancho en pixeles del sprite>MposX>Ubicacion del Sprite, Pos Y del sprite
                        self.caidabarril2=False
                if self.rect.x==f2+1 and self.rect.y==662+iY:
                        self.caidabarril2=True
                if f2>self.rect.x>0 and self.rect.y==548+iY:
                        self.caidabarril2=False
                if f2>self.rect.x>0 and self.rect.y==388+iY:
                        self.caidabarril2=False
                if 181+f2>self.rect.x>181-iX and self.rect.y==592+iY:
                        self.caidabarril2=False
                if 341+f2>self.rect.x>341-iX and self.rect.y==662+iY:
                        self.caidabarril2=False
                if 568+f2>self.rect.x>568-iX and self.rect.y==592+iY:
                          self.caidabarril2=False
                if 365+f2>self.rect.x>365-iX and self.rect.y==366+iY:
                        self.caidabarril2=False
                if self.rect.x==365-iX and self.rect.y==366+iY:
                        self.caidabarril2=True
                if self.rect.x==365+f2+1 and self.rect.y==366+iY:
                        self.caidabarril2=True
                #Floor3
                if 158+f3>self.rect.x>158-iX and self.rect.y==388+iY:
                        self.caidabarril2=False
                if self.rect.x==158-iX and self.rect.y==388+iY:
                        self.caidabarril2=True
                if self.rect.x==158+f4+1 and self.rect.y==388+iY:
                        self.caidabarril2=True
                #Floor4
                f4y=22
                #1
                if 430+f4>self.rect.x>430-iX and self.rect.y==638+iY:
                        self.caidabarril2=False
                #2
                if 499+f4>self.rect.x>499-iX and self.rect.y==616+iY:
                        self.caidabarril2=False
                #3
                if 589+f4>self.rect.x>589-iX and self.rect.y==524+iY:
                        self.caidabarril2=False
                #4
                if 523+f4>self.rect.x>523-iX and self.rect.y==504+iY:
                        self.caidabarril2=False
                #5
                if 453+f4>self.rect.x>453-iX and self.rect.y==478+iY:
                        self.caidabarril2=False
                #6
                if 385+f4>self.rect.x>385-iX and self.rect.y==456+iY:
                        self.caidabarril2=False
                #7
                if 454+f4>self.rect.x>454-iX and self.rect.y==342+iY:
                        self.caidabarril2=False
                if self.rect.x==454-iX and self.rect.y==342+iY:
                        self.caidabarril2=True
                if self.rect.x==454+f4+1 and self.rect.y==342+iY:
                        self.caidabarril2=True
                if self.rect.x==454-iX and 342+iY<=self.rect.y<=342+f4y+iY:
                        self.ladosbarrild2=False
                        self.ladosbarrili2=True
                #8
                if 523+f4>self.rect.x>523-iX and self.rect.y==320+iY:
                        self.caidabarril2=False
                if self.rect.x==523-iX and self.rect.y==320+iY:
                        self.caidabarril2=True
                if self.rect.x==523+f4+1 and self.rect.y==320+iY:
                        self.caidabarril2=True
                if self.rect.x==523-iX and 320+iY<=self.rect.y<=320+f4y+iY:
                        self.ladosbarrild2=False
                        self.ladosbarrili2=True
                
                #9
                if 592+f4>self.rect.x>592-iX and self.rect.y==298+iY:
                        self.caidabarril2=False
                if self.rect.x==592-iX and 298+iY<=self.rect.y<=298+f4y+iY:
                        self.ladosbarrild2=False
                        self.ladosbarrili2=True
                #Floor5
                f5y=24
                if 520+f5>self.rect.x>520-iX and self.rect.y==410+iY:
                        self.caidabarril2=False
                if self.rect.x==520-1-iX and self.rect.y==410+iY:
                        self.caidabarril2=True
                #Floor6
                if f6>self.rect.x>0 and self.rect.y==250+iY:
                        self.caidabarril2=False
                        self.ladosbarrild2=True
                if self.rect.x==f6+1 and self.rect.y==250+iY:
                        self.caidabarril2=True
                #Floor7
                if f7+250>self.rect.x>250-iX and self.rect.y==160+iY:
                        self.caidabarril2=False
                if self.rect.x==250-iX and self.rect.y==160+iY:
                        self.caidabarril2=True
                if self.rect.x==250+f7+1 and self.rect.y==160+iY:
                        self.caidabarril2=True
                #Marcos de la Pantalla
                if self.rect.x<=0:
                        self.ladosbarrili2=False
                        self.ladosbarrild2=True
                if self.rect.x>=WIDTH-iX:
                        self.ladosbarrild2=False
                        self.ladosbarrili2=True
        def sprites(self):
                global cont3
                p=6
                if cont3==p:
                        self.image=load_image("images/Barriles1_001.png",True)
                if cont3==p*2:
                        self.image=load_image("images/Barriles1_002.png",True)
                if cont3==p*3:
                        self.image=load_image("images/Barriles1_003.png",True)
                if cont3==p*4:
                        self.image=load_image("images/Barriles1_004.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_001.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_002.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_003.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_004.png",True)
                        cont3=0   
                return
        def colisiones(self,protagonista):
                if pygame.sprite.collide_rect(self, protagonista):
                        global cont4
                        #print (0)
                        cont4=6
                        return vidas()
class Barril3 (pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Barriles1_001.png",True)
                self.image_inv = pygame.transform.flip(self.image,True,False)
                self.rect = self.image.get_rect()
                self.time = 0
                #Barril3
                self.rect.x=0
                self.rect.y=-50
                self.caidabarril3=False
                self.ladosbarrild3=False
                self.ladosbarrili3=False
        def IA3(self):
                global Barro3
                if Barro3==True:
                        self.rect.x=100
                        self.rect.y=219
                        Barro3=False
                if self.caidabarril3==True:
                        self.rect.y+=1
                if self.ladosbarrild3==True:
                        self.ladosbarrili3=False
                        self.rect.x+=1
                if self.ladosbarrili3==True:
                        self.ladosbarrild3=False
                        self.rect.x-=1
                iY=-31
                iX=29
                f2=67
                f3=93
                f4=49
                f5=116
                f6=477
                f7=137
                #Floor1
                if WIDTH>self.rect.x>0 and self.rect.y==708+iY:
                        self.caidabarril3=False
                if self.rect.x==WIDTH-iX and self.rect.y==708+iY:
                        self.caidabarril3=True
                if self.rect.x==0 and self.rect.y==708+iY:
                        self.caidabarril3=True        
                if self.rect.y==HEIGHT:
                        self.rect.x=100
                        self.rect.y=219
                #Floor2
                if f2>self.rect.x>0 and self.rect.y==662+iY:#Ubicación del Sprite en X+Ancho en pixeles del sprite>MposX>Ubicacion del Sprite, Pos Y del sprite
                        self.caidabarril3=False
                if self.rect.x==f2+1 and self.rect.y==662+iY:
                        self.caidabarril3=True
                if f2>self.rect.x>0 and self.rect.y==548+iY:
                        self.caidabarril3=False
                if f2>self.rect.x>0 and self.rect.y==388+iY:
                        self.caidabarril3=False
                if 181+f2>self.rect.x>181-iX and self.rect.y==592+iY:
                        self.caidabarril3=False
                if 341+f2>self.rect.x>341-iX and self.rect.y==662+iY:
                        self.caidabarril3=False
                if 568+f2>self.rect.x>568-iX and self.rect.y==592+iY:
                          self.caidabarril3=False
                if 365+f2>self.rect.x>365-iX and self.rect.y==366+iY:
                        self.caidabarril3=False
                if self.rect.x==365-iX and self.rect.y==366+iY:
                        self.caidabarril3=True
                if self.rect.x==365+f2+1 and self.rect.y==366+iY:
                        self.caidabarril3=True
                #Floor3
                if 158+f3>self.rect.x>158-iX and self.rect.y==388+iY:
                        self.caidabarril3=False
                if self.rect.x==158-iX and self.rect.y==388+iY:
                        self.caidabarril3=True
                if self.rect.x==158+f4+1 and self.rect.y==388+iY:
                        self.caidabarril3=True
                #Floor4
                f4y=22
                #1
                if 430+f4>self.rect.x>430-iX and self.rect.y==638+iY:
                        self.caidabarril3=False
                #2
                if 499+f4>self.rect.x>499-iX and self.rect.y==616+iY:
                        self.caidabarril3=False
                #3
                if 589+f4>self.rect.x>589-iX and self.rect.y==524+iY:
                        self.caidabarril3=False
                #4
                if 523+f4>self.rect.x>523-iX and self.rect.y==504+iY:
                        self.caidabarril3=False
                #5
                if 453+f4>self.rect.x>453-iX and self.rect.y==478+iY:
                        self.caidabarril3=False
                #6
                if 385+f4>self.rect.x>385-iX and self.rect.y==456+iY:
                        self.caidabarril3=False
                #7
                if 454+f4>self.rect.x>454-iX and self.rect.y==342+iY:
                        self.caidabarril3=False
                if self.rect.x==454-iX and self.rect.y==342+iY:
                        self.caidabarril3=True
                if self.rect.x==454+f4+1 and self.rect.y==342+iY:
                        self.caidabarril3=True
                if self.rect.x==454-iX and 342+iY<=self.rect.y<=342+f4y+iY:
                        self.ladosbarrild3=False
                        self.ladosbarrili3=True
                #8
                if 523+f4>self.rect.x>523-iX and self.rect.y==320+iY:
                        self.caidabarril3=False
                if self.rect.x==523-iX and self.rect.y==320+iY:
                        self.caidabarril3=True
                if self.rect.x==523+f4+1 and self.rect.y==320+iY:
                        self.caidabarril3=True
                if self.rect.x==523-iX and 320+iY<=self.rect.y<=320+f4y+iY:
                        self.ladosbarrild3=False
                        self.ladosbarrili3=True
                
                #9
                if 592+f4>self.rect.x>592-iX and self.rect.y==298+iY:
                        self.caidabarril3=False
                if self.rect.x==592-iX and 298+iY<=self.rect.y<=298+f4y+iY:
                        self.ladosbarrild3=False
                        self.ladosbarrili3=True
                #Floor5
                f5y=24
                if 520+f5>self.rect.x>520-iX and self.rect.y==410+iY:
                        self.caidabarril3=False
                if self.rect.x==520-1-iX and self.rect.y==410+iY:
                        self.caidabarril3=True
                #Floor6
                if f6>self.rect.x>0 and self.rect.y==250+iY:
                        self.caidabarril3=False
                        self.ladosbarrild3=True
                if self.rect.x==f6+1 and self.rect.y==250+iY:
                        self.caidabarril3=True
                #Floor7
                if f7+250>self.rect.x>250-iX and self.rect.y==160+iY:
                        self.caidabarril3=False
                        self.ladosbarrild3=True
                if self.rect.x==250-iX and self.rect.y==160+iY:
                        self.caidabarril3=True
                if self.rect.x==250+f7+1 and self.rect.y==160+iY:
                        self.caidabarril3=True
                #Marcos de la Pantalla
                if self.rect.x<=0:
                        self.ladosbarrili3=False
                        self.ladosbarrild3=True
                if self.rect.x>=WIDTH-iX:
                        self.ladosbarrild3=False
                        self.ladosbarrili3=True
        def sprites(self):
                global cont3
                p=6
                if cont3==p:
                        self.image=load_image("images/Barriles1_001.png",True)
                if cont3==p*2:
                        self.image=load_image("images/Barriles1_002.png",True)
                if cont3==p*3:
                        self.image=load_image("images/Barriles1_003.png",True)
                if cont3==p*4:
                        self.image=load_image("images/Barriles1_004.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_001.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_002.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_003.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_004.png",True)
                        cont3=0   
                return
        def colisiones(self,protagonista):
                if pygame.sprite.collide_rect(self, protagonista):
                        global cont4
                        cont4=6
                        #print (0)
                        return vidas()
class Barril4 (pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Barriles1_001.png",True)
                self.image_inv = pygame.transform.flip(self.image,True,False)
                self.rect = self.image.get_rect()
                self.time = 0
                #Barril4
                self.rect.x=0
                self.rect.y=-50
                self.caidabarril4=False
                self.ladosbarrild4=False
                self.ladosbarrili4=False
        def IA4(self):
                global Barro4
                if Barro4==True:
                        self.rect.x=100
                        self.rect.y=219
                        Barro4=False
                if self.caidabarril4==True:
                        self.rect.y+=1
                if self.ladosbarrild4==True:
                        self.ladosbarrili4=False
                        self.rect.x+=1
                if self.ladosbarrili4==True:
                        self.ladosbarrild4=False
                        self.rect.x-=1
                iY=-31
                iX=29
                f2=67
                f3=93
                f4=49
                f5=116
                f6=477
                f7=137
                #Floor1
                if WIDTH>self.rect.x>0 and self.rect.y==708+iY:
                        self.caidabarril4=False
                if self.rect.x==WIDTH-iX and self.rect.y==708+iY:
                        self.caidabarril4=True
                if self.rect.x==0 and self.rect.y==708+iY:
                        self.caidabarril4=True        
                if self.rect.y==HEIGHT:
                        self.rect.x=100
                        self.rect.y=219
                #Floor2
                if f2>self.rect.x>0 and self.rect.y==662+iY:#Ubicación del Sprite en X+Ancho en pixeles del sprite>MposX>Ubicacion del Sprite, Pos Y del sprite
                        self.caidabarril4=False
                if self.rect.x==f2+1 and self.rect.y==662+iY:
                        self.caidabarril4=True
                if f2>self.rect.x>0 and self.rect.y==548+iY:
                        self.caidabarril4=False
                if f2>self.rect.x>0 and self.rect.y==388+iY:
                        self.caidabarril4=False
                if 181+f2>self.rect.x>181-iX and self.rect.y==592+iY:
                        self.caidabarril4=False
                if 341+f2>self.rect.x>341-iX and self.rect.y==662+iY:
                        self.caidabarril4=False
                if 568+f2>self.rect.x>568-iX and self.rect.y==592+iY:
                          self.caidabarril4=False
                if 365+f2>self.rect.x>365-iX and self.rect.y==366+iY:
                        self.caidabarril4=False
                if self.rect.x==365-iX and self.rect.y==366+iY:
                        self.caidabarril4=True
                if self.rect.x==365+f2+1 and self.rect.y==366+iY:
                        self.caidabarril4=True
                #Floor3
                if 158+f3>self.rect.x>158-iX and self.rect.y==388+iY:
                        self.caidabarril4=False
                if self.rect.x==158-iX and self.rect.y==388+iY:
                        self.caidabarril4=True
                if self.rect.x==158+f4+1 and self.rect.y==388+iY:
                        self.caidabarril4=True
                #Floor4
                f4y=22
                #1
                if 430+f4>self.rect.x>430-iX and self.rect.y==638+iY:
                        self.caidabarril4=False
                #2
                if 499+f4>self.rect.x>499-iX and self.rect.y==616+iY:
                        self.caidabarril4=False
                #3
                if 589+f4>self.rect.x>589-iX and self.rect.y==524+iY:
                        self.caidabarril4=False
                #4
                if 523+f4>self.rect.x>523-iX and self.rect.y==504+iY:
                        self.caidabarril4=False
                #5
                if 453+f4>self.rect.x>453-iX and self.rect.y==478+iY:
                        self.caidabarril4=False
                #6
                if 385+f4>self.rect.x>385-iX and self.rect.y==456+iY:
                        self.caidabarril4=False
                #7
                if 454+f4>self.rect.x>454-iX and self.rect.y==342+iY:
                        self.caidabarril4=False
                if self.rect.x==454-iX and self.rect.y==342+iY:
                        self.caidabarril4=True
                if self.rect.x==454+f4+1 and self.rect.y==342+iY:
                        self.caidabarril4=True
                if self.rect.x==454-iX and 342+iY<=self.rect.y<=342+f4y+iY:
                        self.ladosbarrild4=False
                        self.ladosbarrili4=True
                #8
                if 523+f4>self.rect.x>523-iX and self.rect.y==320+iY:
                        self.caidabarril4=False
                if self.rect.x==523-iX and self.rect.y==320+iY:
                        self.caidabarril4=True
                if self.rect.x==523+f4+1 and self.rect.y==320+iY:
                        self.caidabarril4=True
                if self.rect.x==523-iX and 320+iY<=self.rect.y<=320+f4y+iY:
                        self.ladosbarrild4=False
                        self.ladosbarrili4=True
                
                #9
                if 592+f4>self.rect.x>592-iX and self.rect.y==298+iY:
                        self.caidabarril4=False
                if self.rect.x==592-iX and 298+iY<=self.rect.y<=298+f4y+iY:
                        self.ladosbarrild4=False
                        self.ladosbarrili4=True
                #Floor5
                f5y=24
                if 520+f5>self.rect.x>520-iX and self.rect.y==410+iY:
                        self.caidabarril4=False
                if self.rect.x==520-1-iX and self.rect.y==410+iY:
                        self.caidabarril4=True
                #Floor6
                if f6>self.rect.x>0 and self.rect.y==250+iY:
                        self.caidabarril4=False
                        self.ladosbarrild4=True
                if self.rect.x==f6+1 and self.rect.y==250+iY:
                        self.caidabarril4=True
                #Floor7
                if f7+250>self.rect.x>250-iX and self.rect.y==160+iY:
                        self.caidabarril4=False
                        self.ladosbarrild4=True
                if self.rect.x==250-iX and self.rect.y==160+iY:
                        self.caidabarril4=True
                if self.rect.x==250+f7+1 and self.rect.y==160+iY:
                        self.caidabarril4=True
                #Marcos de la Pantalla
                if self.rect.x<=0:
                        self.ladosbarrili4=False
                        self.ladosbarrild4=True
                if self.rect.x>=WIDTH-iX:
                        self.ladosbarrild4=False
                        self.ladosbarrili4=True
        def sprites(self):
                global cont3
                p=6
                if cont3==p:
                        self.image=load_image("images/Barriles1_001.png",True)
                if cont3==p*2:
                        self.image=load_image("images/Barriles1_002.png",True)
                if cont3==p*3:
                        self.image=load_image("images/Barriles1_003.png",True)
                if cont3==p*4:
                        self.image=load_image("images/Barriles1_004.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_001.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_002.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_003.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_004.png",True)
                        cont3=0   
                return
        def colisiones(self,protagonista):
                if pygame.sprite.collide_rect(self, protagonista):
                        global cont4
                        cont4=6
                        ##print (0)
                        return vidas()
class Barril5 (pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Barriles1_001.png",True)
                self.image_inv = pygame.transform.flip(self.image,True,False)
                self.rect = self.image.get_rect()
                self.time = 0
                #Barril5
                self.rect.x=0
                self.rect.y=-50
                self.caidabarril5=False
                self.ladosbarrild5=False
                self.ladosbarrili5=False
        def IA5(self):
                global Barro5
                if Barro5==True:
                        self.rect.x=100
                        self.rect.y=219
                        Barro5=False
                if self.caidabarril5==True:
                        self.rect.y+=1
                if self.ladosbarrild5==True:
                        self.ladosbarrili5=False
                        self.rect.x+=1
                if self.ladosbarrili5==True:
                        self.ladosbarrild5=False
                        self.rect.x-=1
                iY=-31
                iX=29
                f2=67
                f3=93
                f4=49
                f5=116
                f6=477
                f7=137
                #Floor1
                if WIDTH>self.rect.x>0 and self.rect.y==708+iY:
                        self.caidabarril5=False
                if self.rect.x==WIDTH-iX and self.rect.y==708+iY:
                        self.caidabarril5=True
                if self.rect.x==0 and self.rect.y==708+iY:
                        self.caidabarril5=True        
                if self.rect.y==HEIGHT:
                        self.rect.x=100
                        self.rect.y=219
                #Floor2
                if f2>self.rect.x>0 and self.rect.y==662+iY:#Ubicación del Sprite en X+Ancho en pixeles del sprite>MposX>Ubicacion del Sprite, Pos Y del sprite
                        self.caidabarril5=False
                if self.rect.x==f2+1 and self.rect.y==662+iY:
                        self.caidabarril5=True
                if f2>self.rect.x>0 and self.rect.y==548+iY:
                        self.caidabarril5=False
                if f2>self.rect.x>0 and self.rect.y==388+iY:
                        self.caidabarril5=False
                if 181+f2>self.rect.x>181-iX and self.rect.y==592+iY:
                        self.caidabarril5=False
                if 341+f2>self.rect.x>341-iX and self.rect.y==662+iY:
                        self.caidabarril5=False
                if 568+f2>self.rect.x>568-iX and self.rect.y==592+iY:
                          self.caidabarril5=False
                if 365+f2>self.rect.x>365-iX and self.rect.y==366+iY:
                        self.caidabarril5=False
                if self.rect.x==365-iX and self.rect.y==366+iY:
                        self.caidabarril5=True
                if self.rect.x==365+f2+1 and self.rect.y==366+iY:
                        self.caidabarril5=True
                #Floor3
                if 158+f3>self.rect.x>158-iX and self.rect.y==388+iY:
                        self.caidabarril5=False
                if self.rect.x==158-iX and self.rect.y==388+iY:
                        self.caidabarril5=True
                if self.rect.x==158+f4+1 and self.rect.y==388+iY:
                        self.caidabarril5=True
                #Floor4
                f4y=22
                #1
                if 430+f4>self.rect.x>430-iX and self.rect.y==638+iY:
                        self.caidabarril5=False
                #2
                if 499+f4>self.rect.x>499-iX and self.rect.y==616+iY:
                        self.caidabarril5=False
                #3
                if 589+f4>self.rect.x>589-iX and self.rect.y==524+iY:
                        self.caidabarril5=False
                #4
                if 523+f4>self.rect.x>523-iX and self.rect.y==504+iY:
                        self.caidabarril5=False
                #5
                if 453+f4>self.rect.x>453-iX and self.rect.y==478+iY:
                        self.caidabarril5=False
                #6
                if 385+f4>self.rect.x>385-iX and self.rect.y==456+iY:
                        self.caidabarril5=False
                #7
                if 454+f4>self.rect.x>454-iX and self.rect.y==342+iY:
                        self.caidabarril5=False
                if self.rect.x==454-iX and self.rect.y==342+iY:
                        self.caidabarril5=True
                if self.rect.x==454+f4+1 and self.rect.y==342+iY:
                        self.caidabarril5=True
                if self.rect.x==454-iX and 342+iY<=self.rect.y<=342+f4y+iY:
                        self.ladosbarrild5=False
                        self.ladosbarrili5=True
                #8
                if 523+f4>self.rect.x>523-iX and self.rect.y==320+iY:
                        self.caidabarril5=False
                if self.rect.x==523-iX and self.rect.y==320+iY:
                        self.caidabarril5=True
                if self.rect.x==523+f4+1 and self.rect.y==320+iY:
                        self.caidabarril5=True
                if self.rect.x==523-iX and 320+iY<=self.rect.y<=320+f4y+iY:
                        self.ladosbarrild5=False
                        self.ladosbarrili5=True
                
                #9
                if 592+f4>self.rect.x>592-iX and self.rect.y==298+iY:
                        self.caidabarril5=False
                if self.rect.x==592-iX and 298+iY<=self.rect.y<=298+f4y+iY:
                        self.ladosbarrild5=False
                        self.ladosbarrili5=True
                #Floor5
                f5y=24
                if 520+f5>self.rect.x>520-iX and self.rect.y==410+iY:
                        self.caidabarril5=False
                if self.rect.x==520-1-iX and self.rect.y==410+iY:
                        self.caidabarril5=True
                #Floor6
                if f6>self.rect.x>0 and self.rect.y==250+iY:
                        self.caidabarril5=False
                        self.ladosbarrild5=True
                if self.rect.x==f6+1 and self.rect.y==250+iY:
                        self.caidabarril5=True
                #Floor7
                if f7+250>self.rect.x>250-iX and self.rect.y==160+iY:
                        self.caidabarril5=False
                        self.ladosbarrild5=True
                if self.rect.x==250-iX and self.rect.y==160+iY:
                        self.caidabarril5=True
                if self.rect.x==250+f7+1 and self.rect.y==160+iY:
                        self.caidabarril5=True
                #Marcos de la Pantalla
                if self.rect.x<=0:
                        self.ladosbarrili5=False
                        self.ladosbarrild5=True
                if self.rect.x>=WIDTH-iX:
                        self.ladosbarrild5=False
                        self.ladosbarrili5=True
        def sprites(self):
                global cont3
                p=6
                if cont3==p:
                        self.image=load_image("images/Barriles1_001.png",True)
                if cont3==p*2:
                        self.image=load_image("images/Barriles1_002.png",True)
                if cont3==p*3:
                        self.image=load_image("images/Barriles1_003.png",True)
                if cont3==p*4:
                        self.image=load_image("images/Barriles1_004.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_001.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_002.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_003.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_004.png",True)
                        cont3=0   
                return
        def colisiones(self,protagonista):
                if pygame.sprite.collide_rect(self, protagonista):
                        global cont4
                        cont4=6
                        #print (0)
                        return vidas()
class Barril6 (pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Barriles1_001.png",True)
                self.image_inv = pygame.transform.flip(self.image,True,False)
                self.rect = self.image.get_rect()
                self.time = 0
                #Barril6
                self.caidabarril6=False
                self.ladosbarrild6=False
                self.ladosbarrili6=False
                self.rect.x=0
                self.rect.y=-50
        def IA6(self):
                global Barro6
                if Barro6==True:
                        self.rect.x=100
                        self.rect.y=219
                        Barro6=False
                if self.caidabarril6==True:
                        self.rect.y+=1
                if self.ladosbarrild6==True:
                        self.ladosbarrili6=False
                        self.rect.x+=1
                if self.ladosbarrili6==True:
                        self.ladosbarrild6=False
                        self.rect.x-=1
                iY=-31
                iX=29
                f2=67
                f3=93
                f4=49
                f5=116
                f6=477
                f7=137
                #Floor1
                if WIDTH>self.rect.x>0 and self.rect.y==708+iY:
                        self.caidabarril6=False
                if self.rect.x==WIDTH-iX and self.rect.y==708+iY:
                        self.caidabarril6=True
                if self.rect.x==0 and self.rect.y==708+iY:
                        self.caidabarril6=True        
                if self.rect.y==HEIGHT:
                        self.rect.x=100
                        self.rect.y=219
                #Floor2
                if f2>self.rect.x>0 and self.rect.y==662+iY:#Ubicación del Sprite en X+Ancho en pixeles del sprite>MposX>Ubicacion del Sprite, Pos Y del sprite
                        self.caidabarril6=False
                if self.rect.x==f2+1 and self.rect.y==662+iY:
                        self.caidabarril6=True
                if f2>self.rect.x>0 and self.rect.y==548+iY:
                        self.caidabarril6=False
                if f2>self.rect.x>0 and self.rect.y==388+iY:
                        self.caidabarril6=False
                if 181+f2>self.rect.x>181-iX and self.rect.y==592+iY:
                        self.caidabarril6=False
                if 341+f2>self.rect.x>341-iX and self.rect.y==662+iY:
                        self.caidabarril6=False
                if 568+f2>self.rect.x>568-iX and self.rect.y==592+iY:
                          self.caidabarril6=False
                if 365+f2>self.rect.x>365-iX and self.rect.y==366+iY:
                        self.caidabarril6=False
                if self.rect.x==365-iX and self.rect.y==366+iY:
                        self.caidabarril6=True
                if self.rect.x==365+f2+1 and self.rect.y==366+iY:
                        self.caidabarril6=True
                #Floor3
                if 158+f3>self.rect.x>158-iX and self.rect.y==388+iY:
                        self.caidabarril6=False
                if self.rect.x==158-iX and self.rect.y==388+iY:
                        self.caidabarril6=True
                if self.rect.x==158+f4+1 and self.rect.y==388+iY:
                        self.caidabarril6=True
                #Floor4
                f4y=22
                #1
                if 430+f4>self.rect.x>430-iX and self.rect.y==638+iY:
                        self.caidabarril6=False
                #2
                if 499+f4>self.rect.x>499-iX and self.rect.y==616+iY:
                        self.caidabarril6=False
                #3
                if 589+f4>self.rect.x>589-iX and self.rect.y==524+iY:
                        self.caidabarril6=False
                #4
                if 523+f4>self.rect.x>523-iX and self.rect.y==504+iY:
                        self.caidabarril6=False
                #5
                if 453+f4>self.rect.x>453-iX and self.rect.y==478+iY:
                        self.caidabarril6=False
                #6
                if 385+f4>self.rect.x>385-iX and self.rect.y==456+iY:
                        self.caidabarril6=False
                #7
                if 454+f4>self.rect.x>454-iX and self.rect.y==342+iY:
                        self.caidabarril6=False
                if self.rect.x==454-iX and self.rect.y==342+iY:
                        self.caidabarril6=True
                if self.rect.x==454+f4+1 and self.rect.y==342+iY:
                        self.caidabarril6=True
                if self.rect.x==454-iX and 342+iY<=self.rect.y<=342+f4y+iY:
                        self.ladosbarrild6=False
                        self.ladosbarrili6=True
                #8
                if 523+f4>self.rect.x>523-iX and self.rect.y==320+iY:
                        self.caidabarril6=False
                if self.rect.x==523-iX and self.rect.y==320+iY:
                        self.caidabarril6=True
                if self.rect.x==523+f4+1 and self.rect.y==320+iY:
                        self.caidabarril6=True
                if self.rect.x==523-iX and 320+iY<=self.rect.y<=320+f4y+iY:
                        self.ladosbarrild6=False
                        self.ladosbarrili6=True
                
                #9
                if 592+f4>self.rect.x>592-iX and self.rect.y==298+iY:
                        self.caidabarril6=False
                        self.ladosbarrild6=True
                if self.rect.x==592-iX and 298+iY<=self.rect.y<=298+f4y+iY:
                        self.ladosbarrild6=False
                        self.ladosbarrili6=True
                #Floor5
                f5y=24
                if 520+f5>self.rect.x>520-iX and self.rect.y==410+iY:
                        self.caidabarril6=False
                if self.rect.x==520-1-iX and self.rect.y==410+iY:
                        self.caidabarril6=True
                #Floor6
                if f6>self.rect.x>0 and self.rect.y==250+iY:
                        self.caidabarril6=False
                        self.ladosbarrild6=True
                if self.rect.x==f6+1 and self.rect.y==250+iY:
                        self.caidabarril6=True
                #Floor7
                if f7+250>self.rect.x>250-iX and self.rect.y==160+iY:
                        self.caidabarril6=False
                        self.ladosbarrild6=True
                if self.rect.x==250-iX and self.rect.y==160+iY:
                        self.caidabarril6=True
                if self.rect.x==250+f7+1 and self.rect.y==160+iY:
                        self.caidabarril6=True
                #Marcos de la Pantalla
                if self.rect.x<=0:
                        self.ladosbarrili6=False
                        self.ladosbarrild6=True
                if self.rect.x>=WIDTH-iX:
                        self.ladosbarrild6=False
                        self.ladosbarrili6=True
        def sprites(self):
                global cont3
                p=6
                if cont3==p:
                        self.image=load_image("images/Barriles1_001.png",True)
                if cont3==p*2:
                        self.image=load_image("images/Barriles1_002.png",True)
                if cont3==p*3:
                        self.image=load_image("images/Barriles1_003.png",True)
                if cont3==p*4:
                        self.image=load_image("images/Barriles1_004.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_001.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_002.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_003.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_004.png",True)
                        cont3=0   
                return
        def colisiones(self,protagonista):
                if pygame.sprite.collide_rect(self, protagonista):
                        global cont4
                        cont4=6
                        #print(0)
                        return vidas()
class Stairs1(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Stairs 1.png")
                self.rect = self.image.get_rect()
class Stairs2(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Stairs 2.png")
                self.rect = self.image.get_rect()
class Stairs3(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Stairs 3.png")
                self.rect = self.image.get_rect()
class Stairs4(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Stairs 4.png")
                self.rect = self.image.get_rect()
class Stairs5(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Stairs 5.png")
                self.rect = self.image.get_rect()
class Stairs6(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Stairs 6.png")
                self.rect = self.image.get_rect()
class Floor1(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Floor1.png")
                self.rect = self.image.get_rect()
class Floor2(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Floor2.png")
                self.rect = self.image.get_rect()
class Floor3(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Floor3.png")
                self.rect = self.image.get_rect()
class Floor4(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Floor4.png")
                self.rect = self.image.get_rect()
class Floor5(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Floor5.png")
                self.rect = self.image.get_rect()
class Floor6(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Floor6.png")
                self.rect = self.image.get_rect()
class Floor7(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Floor7.png")
                self.rect = self.image.get_rect()
#Barriles de la pantalla de Inicio
class BarrilIntro1(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Barriles1_001.png",True)
                self.rect = self.image.get_rect()
                self.caidabarril=True
                self.rect.x=0
                self.rect.y=0
        def mov(self):#Movimiento
                if self.caidabarril==True:
                        self.rect.y+=1
                if self.rect.y==HEIGHT:
                        self.rect.y=0
        def sprites(self):#Animación
                global cont3
                p=6
                if cont3==p:
                        self.image=load_image("images/Barriles1_001.png",True)
                if cont3==p*2:
                        self.image=load_image("images/Barriles1_002.png",True)
                if cont3==p*3:
                        self.image=load_image("images/Barriles1_003.png",True)
                if cont3==p*4:
                        self.image=load_image("images/Barriles1_004.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_001.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_002.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_003.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_004.png",True)
                        cont3=0
class BarrilIntro2(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Barriles1_001.png",True)
                self.rect = self.image.get_rect()
                self.caidabarril=True
                self.rect.x=150
                self.rect.y=50
        def mov(self):
                if self.caidabarril==True:
                        self.rect.y+=1
                if self.rect.y==HEIGHT:
                        self.rect.y=0
        def sprites(self):
                global cont3
                p=6
                if cont3==p:
                        self.image=load_image("images/Barriles1_001.png",True)
                if cont3==p*2:
                        self.image=load_image("images/Barriles1_002.png",True)
                if cont3==p*3:
                        self.image=load_image("images/Barriles1_003.png",True)
                if cont3==p*4:
                        self.image=load_image("images/Barriles1_004.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_001.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_002.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_003.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_004.png",True)
                        cont3=0
class BarrilIntro3(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Barriles1_001.png",True)
                self.rect = self.image.get_rect()
                self.caidabarril=True
                self.rect.x=606
                self.rect.y=0
        def mov(self):
                if self.caidabarril==True:
                        self.rect.y+=1
                if self.rect.y==HEIGHT:
                        self.rect.y=0
        def sprites(self):
                global cont3
                p=6
                if cont3==p:
                        self.image=load_image("images/Barriles1_001.png",True)
                if cont3==p*2:
                        self.image=load_image("images/Barriles1_002.png",True)
                if cont3==p*3:
                        self.image=load_image("images/Barriles1_003.png",True)
                if cont3==p*4:
                        self.image=load_image("images/Barriles1_004.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_001.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_002.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_003.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_004.png",True)
                        cont3=0
class BarrilIntro4(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = load_image("images/Barriles1_001.png",True)
                self.rect = self.image.get_rect()
                self.caidabarril=True
                self.rect.x=456
                self.rect.y=50
        def mov(self):
                if self.caidabarril==True:
                        self.rect.y+=1
                if self.rect.y==HEIGHT:
                        self.rect.y=0
        def sprites(self):
                global cont3
                p=6
                if cont3==p:
                        self.image=load_image("images/Barriles1_001.png",True)
                if cont3==p*2:
                        self.image=load_image("images/Barriles1_002.png",True)
                if cont3==p*3:
                        self.image=load_image("images/Barriles1_003.png",True)
                if cont3==p*4:
                        self.image=load_image("images/Barriles1_004.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_001.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_002.png",True)
                if cont3==p*5:
                        self.image=load_image("images/Barriles2_003.png",True)
                if cont3==p*6:
                        self.image=load_image("images/Barriles2_004.png",True)
                        cont3=0 
# Funciones
# ---------------------------------------------------------------------
message="Error"
def load_image(filename, transparent=False):#Llama imagenes
        try: image = pygame.image.load(filename)
        except (pygame.error,message):
                raise (SystemExit, message)
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
def load_music(filename):#Llama Música
        music = pygame.mixer.music.load(filename)
        return music
def comparador_de_lista(lista,valor,cont):#Comparador para subir escaleras
        if lista==[]:
                return 0
        elif lista[0]==valor:
                return valor
        else:
                return comparador_de_lista(lista[1:],valor,cont+1)
def keyboard1():#Teclado del inicio
        global Booleano1, Booleano2 ,Booleano3, Booleano4 , Cunt
        ##print ("Si no imprimo esto, no funciona")
        if Cunt>4:
                Cunt=1
        if Cunt<=0:
                Cunt=4
        if Cunt==1:
                Booleano1=True
                Booleano2=False
                Booleano3=False
                Booleano4=False
        elif Cunt==2:
                Booleano1=False
                Booleano2=True
                Booleano3=False
                Booleano4=False
        elif Cunt==3:
                Booleano1=False
                Booleano2=False
                Booleano3=True
                Booleano4=False
        elif Cunt==4:
                Booleano1=False
                Booleano2=False
                Booleano3=False
                Booleano4=True
def texto(texto, posx, posy, color=(255, 255, 255)):#Textos pequeños
        fuente = pygame.font.Font("Font/Jumpman.ttf",25)
        salida = pygame.font.Font.render(fuente, texto, 1, color)
        salida_rect = salida.get_rect()
        salida_rect.centerx = posx
        salida_rect.centery = posy
        return salida, salida_rect
def texto2(texto, posx, posy, color=(255, 255, 255)):#Textos Grandes
        fuente = pygame.font.Font("Font/Jumpman.ttf",72)
        salida = pygame.font.Font.render(fuente, texto, 1, color)
        salida_rect = salida.get_rect()
        salida_rect.centerx = posx
        salida_rect.centery = posy
        return salida, salida_rect
def texto3(texto, posx, posy, color=(0, 0, 255)):
        fuente = pygame.font.Font("Font/Jumpman.ttf",72)
        salida = pygame.font.Font.render(fuente, texto, 1, color)
        salida_rect = salida.get_rect()
        salida_rect.centerx = posx
        salida_rect.centery = posy
        return salida, salida_rect
def texto4(texto, posx, posy, color=(255, 255, 255)):
        fuente = pygame.font.Font("Font/Jumpman.ttf",25)
        salida = pygame.font.Font.render(fuente, texto, 1, color)
        salida_rect = salida.get_rect()
        salida_rect.centerx = posx
        salida_rect.centery = posy
        return salida, salida_rect
"""
def joystick():
        joysticks = []
        keepPlaying = True
         
        # for al the connected joysticks
        for i in range(0, pygame.joystick.get_count()):
                # create an Joystick object in our list
                joysticks.append(pygame.joystick.Joystick(i))
                # initialize them all (-1 means loop forever)
                joysticks[-1].init()
                # #print a statement telling what the name of the controller is
                #print ("Detected joystick '",joysticks[-1].get_name(),"'")
        while keepPlaying:
                        if event.type == pygame.QUIT:
                                #print ("Received event 'Quit', exiting.")
                                keepPlaying = False
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                #print ("Escape key pressed, exiting.")
                                keepPlaying = False
                        elif event.type == pygame.KEYDOWN:
                                #print ("Keydown,", event.key)
                        elif event.type == pygame.KEYUP:
                                #print ("Keyup,", event.key)
                        #elif event.type == pygame.MOUSEMOTION:
                        #   #print "Mouse movement detected."
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                #print ("Mouse button",event.button,"down at",pygame.mouse.get_pos())
                        elif event.type == pygame.MOUSEBUTTONUP:
                                #print ("Mouse button",event.button,"up at",pygame.mouse.get_pos())
                        elif event.type == pygame.JOYAXISMOTION:
                                #print ("Joystick '",joysticks[event.joy].get_name(),"' axis",event.axis,"motion.")
                        elif event.type == pygame.JOYBUTTONDOWN:
                                #print ("Joystick '",joysticks[event.joy].get_name(),"' button",event.button,"down.")
                                if event.button == 0:
                                        #print ("Hola")
                                elif event.button == 1:
                                        #print("Hola2.0")
                        elif event.type == pygame.JOYBUTTONUP:
                                #print ("Joystick '",joysticks[event.joy].get_name(),"' button",event.button,"up.")
                                if event.button == 0:
                                        #print("Hola")
                                elif event.button == 1:
                                        #print("Hola2.0")
                        elif event.type == pygame.JOYHATMOTION:
                                #print ("Joystick '",joysticks[event.joy].get_name(),"' hat",event.hat," moved.")
"""
def initkeys():#Teclados que retornan a inicio
        global SCORE, life
        keys = pygame.key.get_pressed()
        if keys[K_KP_ENTER]:
                life=2
                SCORE=0
                return inicio()
def initkeys2():#Teclado que Retorna al Main
        keys = pygame.key.get_pressed()
        if keys[K_KP_ENTER]:
                        return main()
def initkeys3():#Teclado que retorna a los puntos más altos
        global SCORE, cunt4
        keys = pygame.key.get_pressed()
        if keys[K_KP_ENTER]:
                life=2
                SCORE=0
                cont4=6
                return Highscores()
def grabartxt_score(name,score):#Grabador de TXT
        archi=open('SCORE.txt','a')
        archi.write(str(score)+"\n")
        archi.close()
def grabartxt_name(purint,score):#Grabador de otro TXT
        archi=open('NAMES.txt','a')
        archi.write(purint+"\n")
        archi.close()
def readtxt():#Lector de TXT
        global Score1, Score2, Score3, Score4, Score5, Score6, Score7, Score8, Score9, Score10
        archis=open('SCORE.txt','r')
        archin=open('NAMES.txt','r')
        linea=archis.readlines()
        linea2=archin.readlines()
        Score1=[(linea[0][:-1]),linea2[0][:-1]]
        Score2=[(linea[1][:-1]),linea2[1][:-1]]
        Score3=[(linea[2][:-1]),linea2[2][:-1]]
        Score4=[(linea[3][:-1]),linea2[3][:-1]]
        Score5=[(linea[4][:-1]),linea2[4][:-1]]
        Score6=[(linea[5][:-1]),linea2[5][:-1]]
        Score7=[(linea[6][:-1]),linea2[6][:-1]]
        Score8=[(linea[7][:-1]),linea2[7][:-1]]
        Score9=[(linea[8][:-1]),linea2[8][:-1]]
        Score10=[(linea[9][:-1]),linea2[9][:-1]]
        print(Score1,Score2,Score3,Score4,Score5)
        archis.close()
        archin.close()
        return redtxtrec(linea,linea2,1)
def redtxtrec(linea,linea2,cont):#Recursiva de la lectora txt
        global Score1, Score2, Score3, Score4, Score5,  Score6, Score7, Score8, Score9, Score10
        if linea==[]:
                Score1=Score1
                Score2=Score2
                Score3=Score3
                Score4=Score4
                Score5=Score5
                Score6=Score6
                Score7=Score7
                Score8=Score8
                Score9=Score9
                Score10=Score10
                print(Score1,Score2,Score3,Score4,Score5,Score6, Score7, Score8, Score9, Score10)
        elif int(linea[0][:-1], base=10)>int(Score1[0], base=10):
                Score10=Score9
                Score9=Score8
                Score8=Score7
                Score7=Score6
                Score6=Score5
                Score5=Score4
                Score4=Score3
                Score3=Score2
                Score2=Score1
                Score1=linea[0][:-1],linea2[0][:-1]
                return redtxtrec(linea[1:],linea2[1:],cont+1)
        elif int(linea[0][:-1], base=10)<=int(Score1[0], base=10):
                if int(linea[0][:-1], base=10)>int(Score2[0], base=10):
                        Score10=Score9
                        Score9=Score8
                        Score8=Score7
                        Score7=Score6
                        Score6=Score5
                        Score5=Score4
                        Score4=Score3
                        Score3=Score2
                        Score2=linea[0][:-1],linea2[0][:-1]
                        return redtxtrec(linea[1:],linea2[1:],cont+1)
                elif int(linea[0][:-1], base=10)<=int(Score2[0], base=10):
                        if int(linea[0][:-1], base=10)>int(Score3[0], base=10):
                                Score10=Score9
                                Score9=Score8
                                Score8=Score7
                                Score7=Score6
                                Score6=Score5
                                Score5=Score4
                                Score4=Score3
                                Score3=linea[0][:-1],linea2[0][:-1]
                                return redtxtrec(linea[1:],linea2[1:],cont+1)
                        elif int(linea[0][:-1], base=10)<=int(Score3[0], base=10):
                                if int(linea[0][:-1], base=10)>int(Score4[0], base=10):
                                        Score10=Score9
                                        Score9=Score8
                                        Score8=Score7
                                        Score7=Score6
                                        Score6=Score5
                                        Score4=Score3
                                        Score4=linea[0][:-1],linea2[0][:-1]
                                        return redtxtrec(linea[1:],linea2[1:],cont+1)
                                elif int(linea[0][:-1], base=10)<=int(Score4[0], base=10):
                                        if int(linea[0][:-1], base=10)>int(Score5[0], base=10):
                                                Score10=Score9
                                                Score9=Score8
                                                Score8=Score7
                                                Score7=Score6
                                                Score6=Score5
                                                Score5=linea[0][:-1],linea2[0][:-1]
                                                return redtxtrec(linea[1:],linea2[1:],cont+1)
                                        elif int(linea[0][:-1], base=10)<=int(Score5[0], base=10):
                                                if int(linea[0][:-1], base=10)>int(Score6[0], base=10):
                                                        Score10=Score9
                                                        Score9=Score8
                                                        Score8=Score7
                                                        Score7=Score6
                                                        Score6=linea[0][:-1],linea2[0][:-1]
                                                        return redtxtrec(linea[1:],linea2[1:],cont+1)
                                                elif int(linea[0][:-1], base=10)<=int(Score6[0], base=10):
                                                        if int(linea[0][:-1], base=10)>int(Score7[0], base=10):
                                                                Score10=Score9
                                                                Score9=Score8
                                                                Score8=Score7
                                                                Score7=linea[0][:-1],linea2[0][:-1]
                                                                return redtxtrec(linea[1:],linea2[1:],cont+1)
                                                        elif int(linea[0][:-1], base=10)<=int(Score7[0], base=10):
                                                                if int(linea[0][:-1], base=10)>int(Score8[0], base=10):
                                                                        Score10=Score9
                                                                        Score9=Score8
                                                                        Score8=linea[0][:-1],linea2[0][:-1]
                                                                        return redtxtrec(linea[1:],linea2[1:],cont+1)
                                                                elif int(linea[0][:-1], base=10)<=int(Score8[0], base=10):
                                                                        if int(linea[0][:-1], base=10)>int(Score9[0], base=10):
                                                                                Score10=Score9
                                                                                Score9=linea[0][:-1],linea2[0][:-1]
                                                                                return redtxtrec(linea[1:],linea2[1:],cont+1)
                                                                        elif int(linea[0][:-1], base=10)<=int(Score9[0], base=10):
                                                                                if int(linea[0][:-1], base=10)>int(Score10[0], base=10):
                                                                                        Score10=linea[0][:-1],linea2[0][:-1]
                                                                                        return redtxtrec(linea[1:],linea2[1:],cont+1)
                                                                                elif int(linea[0][:-1], base=10)<=int(Score10[0], base=10):
                                                                                         return redtxtrec(linea[1:],linea2[1:],cont+1)
                                                                                        
                                                                                         


        
def vidas():#Contador de vidas
        global life
        if life>0:
                life-=1
                return lifescreen()
        else:
                return gameover()
def barrilesDonkey():#Función en la que se permite que se spawneen los barriles de DK
        p=6
        global cont4, Barro1, Barro2, Barro3, Barro4, Barro5, Barro6
        if cont4==p*20:
                Barro1=True
        if cont4==p*40:
                Barro2=True
        if cont4==p*60:
                Barro3=True
        if cont4==p*80:
                Barro4=True
        if cont4==p*100:
                Barro5=True
        if cont4==p*120:
                Barro6=True
        
# ---------------------------------------------------------------------
def win():#Pantalla de Victoria
        screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
        screen.blit(load_image("images/win.png"),(0,0))
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 50)
        while True:
                time = clock.tick(60)
                for event in pygame.event.get():
                        if event.type == QUIT:
                                sys.exit(0)
                        if event.type==pygame.KEYDOWN:
                                global Booleano21,Booleano22,Cunt2,life,name, SCORE
                                if event.unicode.isalpha():
                                        name += event.unicode
                                elif event.key == K_BACKSPACE:
                                        name = name[:-1]
                                elif event.key == K_SPACE:
                                        name += " "
                                elif event.key==pygame.K_KP_ENTER:
                                        grabartxt_score(name,SCORE)
                                        if name=="":
                                                grabartxt_name("Unknown",SCORE)
                                        else:
                                                grabartxt_name(name,SCORE)
                                        return win2()
                block = font.render(name, True, (255, 255, 255))
                score,score_rect=texto2(("Score:"+str(SCORE)) , WIDTH/2 ,HEIGHT/4 )
                camb,camb_rect=texto("Please enter your name:" , WIDTH/2 ,HEIGHT/3 )
                screen.blit(block, (WIDTH/3 ,HEIGHT/2))
                screen.blit(score,score_rect)
                screen.blit(camb,camb_rect)
                pygame.display.flip()
        return 0
def win2():#Pantalla de Victoria con Retry
        screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
        screen.blit(load_image("images/win.png"),(0,0))
        clock = pygame.time.Clock()
        letrero1=Yes()
        letrero2=No()
        global Booleano21,Booleano22,Cunt2,life,name, SCORE
        while True:
                time = clock.tick(60)
                for event in pygame.event.get():
                        if event.type == QUIT:
                                sys.exit(0)
                        if event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_s:
                                                Cunt2+=1
                                                #print (Cunt)
                                if event.key==pygame.K_w:
                                        Cunt2-=1
                                        #print (Cunt)
                                if Cunt2>=3:
                                        Cunt2=1
                                if Cunt2<1:
                                        Cunt2=2
                                if Cunt2==1:
                                        Booleano21=True
                                        Booleano22=False
                                if Cunt2==2:
                                        Booleano21=False
                                        Booleano22=True
                                if event.key==pygame.K_KP_ENTER and Booleano21==True: 
                                        life=2
                                        SCORE=0
                                        cont3=0
                                        Write=True
                                        name=""
                                        return main()
                                        
                                if event.key==pygame.K_KP_ENTER and Booleano22==True:
                                        life=2
                                        SCORE=0
                                        cont3=0
                                        Write=True
                                        name=""
                                        return inicio()
                score,score_rect=texto2(("Score:"+str(SCORE)) , WIDTH/2 ,HEIGHT/4 )
                camb,camb_rect=texto2("Retry?" , WIDTH/2 ,HEIGHT/3 )
                letrero1.update()
                letrero2.update()
                screen.blit(letrero1.image,(200,400))
                screen.blit(letrero2.image,(200,550))
                screen.blit(score,score_rect)
                screen.blit(camb,camb_rect)
                pygame.display.flip()
        return 0
def gameover():#Pantalla de Game Over
        screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
        screen.blit(load_image("images/GameOver.png"),(0,0))
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 50)
        while True:
                time = clock.tick(60)
                for event in pygame.event.get():
                        if event.type == QUIT:
                                sys.exit(0)
                        if event.type==pygame.KEYDOWN:
                                global Booleano21,Booleano22,Cunt2,life,name, SCORE
                                if event.unicode.isalpha():
                                        name += event.unicode
                                elif event.key == K_BACKSPACE:
                                        name = name[:-2]
                                elif event.key == K_SPACE:
                                        name += " "
                                elif event.key==pygame.K_KP_ENTER:
                                        grabartxt_score(name,SCORE)
                                        if name=="":
                                                grabartxt_name("Unknown",SCORE)
                                        else:
                                                grabartxt_name(name,SCORE)
                                        return gameover2()
                block = font.render(name, True, (255, 255, 255))
                score,score_rect=texto2(("Score:"+str(SCORE)) , WIDTH/2 ,HEIGHT/4 )
                camb,camb_rect=texto("Please enter your name:" , WIDTH/2 ,HEIGHT/3 )
                screen.blit(block, (WIDTH/3 ,HEIGHT/2))
                screen.blit(score,score_rect)
                screen.blit(camb,camb_rect)
                pygame.display.flip()
        return 0
def gameover2():#Pantalla de Game Over con Retry
        screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
        screen.blit(load_image("images/GameOver.png"),(0,0))
        clock = pygame.time.Clock()
        letrero1=Yes()
        letrero2=No()
        global Booleano21,Booleano22,Cunt2,life,name, SCORE
        while True:
                time = clock.tick(60)
                for event in pygame.event.get():
                        if event.type == QUIT:
                                sys.exit(0)
                        if event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_s:
                                                Cunt2+=1
                                                #print (Cunt)
                                if event.key==pygame.K_w:
                                        Cunt2-=1
                                        #print (Cunt)
                                if Cunt2>=3:
                                        Cunt2=1
                                if Cunt2<1:
                                        Cunt2=2
                                if Cunt2==1:
                                        Booleano21=True
                                        Booleano22=False
                                if Cunt2==2:
                                        Booleano21=False
                                        Booleano22=True
                                if event.key==pygame.K_KP_ENTER and Booleano21==True: 
                                        life=2
                                        SCORE=0
                                        cont3=0
                                        Write=True
                                        name=""
                                        return main()
                                        
                                if event.key==pygame.K_KP_ENTER and Booleano22==True:
                                        life=2
                                        SCORE=0
                                        cont3=0
                                        Write=True
                                        name=""
                                        return inicio()
                score,score_rect=texto2(("Score:"+str(SCORE)) , WIDTH/2 ,HEIGHT/4 )
                camb,camb_rect=texto2("Retry?" , WIDTH/2 ,HEIGHT/3 )
                letrero1.update()
                letrero2.update()
                screen.blit(letrero1.image,(200,400))
                screen.blit(letrero2.image,(200,550))
                screen.blit(score,score_rect)
                screen.blit(camb,camb_rect)
                pygame.display.flip()
        return 0
def lifescreen():#pantalla que muestra las vidas antes de iniciar le nivel
        screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
        screen.blit(load_image("images/LifeScreen.png"),(0,0))
        clock = pygame.time.Clock()
        while True:
                time = clock.tick(60)
                for eventos in pygame.event.get():
                        if eventos.type == QUIT:
                                sys.exit(0)
                vida,vida_rect = texto2(str(life+1) , WIDTH/2 , HEIGHT/2)
                initkeys2()
                screen.blit(vida,vida_rect)
                pygame.display.flip()
        return 0
def about():#Pantala de Información
        screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
        screen.blit(load_image("images/About2.png"),(0,0))
        clock = pygame.time.Clock()
        while True:
                time = clock.tick(60)
                for eventos in pygame.event.get():
                        if eventos.type == QUIT:
                                sys.exit(0)
                initkeys()
                pygame.display.flip()
        return 0
def instrucciones():#Pantalla de Instrucciones
        screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
        screen.blit(load_image("images/Instructions.jpeg"),(0,0))
        clock = pygame.time.Clock()
        while True:
                time = clock.tick(60)
                for eventos in pygame.event.get():
                        if eventos.type == QUIT:
                                sys.exit(0)
                initkeys3()
                pygame.display.flip()
        return 0
def Highscores():#Pantalla de Highscore
        screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
        screen.blit(load_image("images/Highscores.png"),(0,0))
        clock = pygame.time.Clock()
        global Score1, Score2, Score3, Score4,Score5
        readtxt()
        while True:
                time = clock.tick(60)
                for eventos in pygame.event.get():
                        if eventos.type == QUIT:
                                sys.exit(0)
                #Llama cada Score
                first,first_rect=texto4("1. "+Score1[1]+" "+Score1[0] , WIDTH/2 , HEIGHT/2-120)
                second,second_rect=texto4("2. "+Score2[1]+" "+Score2[0] , WIDTH/2 , HEIGHT/2-96)
                third,third_rect=texto4("3. "+Score3[1]+" "+Score3[0] , WIDTH/2 , HEIGHT/2-72)
                forth,forth_rect=texto4("4. "+Score4[1]+" "+Score4[0] , WIDTH/2 , HEIGHT/2-48)
                fifth,fifth_rect=texto4("5. "+Score5[1]+" "+Score5[0] , WIDTH/2 , HEIGHT/2-24)
                line,line_rect=texto4("-------------------------------------------------------------------------------------" , WIDTH/2 , HEIGHT/2)
                six,six_rect=texto4("6. "+Score6[1]+" "+Score6[0] , WIDTH/2 , HEIGHT/2+24)
                seven,seven_rect=texto4("7. "+Score7[1]+" "+Score7[0] , WIDTH/2 , HEIGHT/2+48)
                eight,eight_rect=texto4("8. "+Score8[1]+" "+Score8[0] , WIDTH/2 , HEIGHT/2+72)
                nine,nine_rect=texto4("9. "+Score9[1]+" "+Score9[0] , WIDTH/2 , HEIGHT/2+96)
                ten,ten_rect=texto4("10. "+Score10[1]+" "+Score10[0] , WIDTH/2 , HEIGHT/2+120)
                screen.blit(first,first_rect)
                screen.blit(second,second_rect)
                screen.blit(third,third_rect)
                screen.blit(forth,forth_rect)
                screen.blit(fifth,fifth_rect)
                screen.blit(line,line_rect)
                screen.blit(six,six_rect)
                screen.blit(seven,seven_rect)
                screen.blit(eight,eight_rect)
                screen.blit(nine,nine_rect)
                screen.blit(ten,ten_rect)
                initkeys()
                pygame.display.flip()
        return 0
def salir():#Salida
        sys.exit(0)
def inicio():#Pantalla de Inicio
        screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
        background_image = Inicio()
        barril1=BarrilIntro1()
        barril2=BarrilIntro2()
        barril3=BarrilIntro3()
        barril4=BarrilIntro4()
        letrero1=Starto()
        letrero2=Instructions()
        letrero3=About()
        letrero4=Exit()
        clock = pygame.time.Clock()
        background_music = load_music("Music/Intro.ogg")
        global cont3,Cunt
        if True:
                pygame.mixer.init()
                pygame.mixer.music.play(-1)
                pygame.event.wait()
        while True:
                cont3+=1
                time = clock.tick(60)
                for event in pygame.event.get():
                        if event.type == QUIT:
                                sys.exit(0)
                        if event.type==pygame.KEYDOWN:
                                #print (event.key)
                                if event.key==pygame.K_s:
                                        Cunt+=1
                                        #print ("presion s", Cunt)
                                if event.key==pygame.K_w:
                                        Cunt-=1
                                        #print ("presion w",Cunt)
                                if event.key==K_KP_ENTER and Booleano1==True:
                                        return main()
                                if event.key==K_KP_ENTER and Booleano2==True:
                                        return instrucciones()
                                if event.key==K_KP_ENTER and Booleano3==True:
                                        return about()
                                if event.key==K_KP_ENTER and Booleano4==True:
                                        return salir()
                keyboard1()
                letrero1.update()
                letrero2.update()
                letrero3.update()
                letrero4.update()
                barril1.mov()
                barril1.sprites()
                barril2.mov()
                barril2.sprites()
                barril3.mov()
                barril3.sprites()
                barril4.mov()
                barril4.sprites()
                screen.blit(background_image.image,(0,0))
                screen.blit(barril4.image,barril4.rect)
                screen.blit(barril3.image,barril3.rect)
                screen.blit(barril2.image,barril2.rect)
                screen.blit(barril1.image,barril1.rect)
                screen.blit(letrero1.image,(220,250))
                screen.blit(letrero2.image,(220,350))
                screen.blit(letrero3.image,(220,450))
                screen.blit(letrero4.image,(220,550))
                pygame.display.flip()
        return 0

def main():#Nivel del Juego
    screen = pygame.display.set_mode((WIDTH, HEIGHT),FULLSCREEN)
    background_image = Background()
    music=load_music
    #Llama las clases
    Donkey = DK()
    pauline=Pauline()
    protagonista=Mario()
    barril1=Barril1()
    barril2=Barril2()
    barril3=Barril3()
    barril4=Barril4()
    barril5=Barril5()
    barril6=Barril6()
    stairs1=Stairs1()
    stairs2=Stairs2()
    stairs3=Stairs3()
    stairs4=Stairs4()
    stairs5=Stairs5()
    stairs6=Stairs6()
    floor1=Floor1()
    floor2=Floor2()
    floor3=Floor3()
    floor4=Floor4()
    floor5=Floor5()
    floor6=Floor6()
    floor7=Floor7()
    menupausa=Pausa()
    barriles=[barril1,barril2,barril3,barril4,barril5,barril6]
    
    

    clock = pygame.time.Clock()
    
    global cont4,cont3,cont2,pause,BooleanoP1,BooleanoP2,BooleanoP3,Vol_off,on_off
    if True:#Música
        background_music = load_music("Music/Level1.ogg")
        pygame.mixer.init()
        pygame.mixer.music.play(-1)
        pygame.event.wait()
    while True:#Loop del juego
        time = clock.tick(60)
        cont2+=0.5
        cont3+=1
        cont4+=0.5
        protagonista.sprite()
        Donkey.spriteDK()
        Donkey.colisiones(protagonista)
        protagonista.movimiento_Y()
        barrilesDonkey()
        protagonista.puntos(barriles)
        barril1.IA()
        barril2.IA2()
        barril3.IA3()
        barril4.IA4()
        barril5.IA5()
        barril6.IA6()
        barril1.sprites()
        barril2.sprites()
        barril3.sprites()
        barril4.sprites()
        barril5.sprites()
        barril6.sprites()
        menupausa.update()
        protagonista.sprites()
        if pause==False:
                protagonista.keyboard()
                Return,Return_rect=texto("Return" , 80000 , 80000)
                MusicOnorOf,MusicOnorOff_rect=texto("Music:"+on_off , 80000 , 80000)
                Exit,Exit_rect=texto("Exit", 80000 , 80000)
        elif pause==True:
                Return,Return_rect=texto("Return" , WIDTH/2 , HEIGHT/2-20)
                MusicOnorOf,MusicOnorOff_rect=texto("Music:"+on_off , WIDTH/2 , HEIGHT/2)
                Exit,Exit_rect=texto("Exit" , WIDTH/2 , HEIGHT/2+20)
                if BooleanoP1==True:
                         Return,Return_rect=texto3("Return" , WIDTH/2 , HEIGHT/2-40)
                if BooleanoP2==True:
                        MusicOnorOf,MusicOnorOff_rect=texto3("Music:"+on_off , WIDTH/2 , HEIGHT/2)
                if BooleanoP3==True:
                        Exit,Exit_rect=texto3("Exit" , WIDTH/2 , HEIGHT/2+40)
        barril1.colisiones(protagonista)
        barril2.colisiones(protagonista)
        barril3.colisiones(protagonista)
        barril4.colisiones(protagonista)
        barril5.colisiones(protagonista)
        barril6.colisiones(protagonista)
        pauline.colisiones(protagonista)
        global i2,i3, SCORE,life,ContP
        for event in pygame.event.get():#Teclado para la Pausa
                if event.type == QUIT:
                        sys.exit(0)
                if event.type==pygame.KEYDOWN:
                        if event.key == K_KP_ENTER:
                                if pause==False:
                                        pause=True
                                if pause==True:
                                        pause=True
                        if event.key==K_w:
                                if pause==True:
                                        ContP-=1
                                        #print(ContP)
                        if event.key==K_s:
                                if pause==True:
                                        ContP+=1
                                        #print(ContP)
                        if event.key==K_KP_ENTER and BooleanoP1==True:#Return
                                 if pause==True:
                                        BooleanoP1=False
                                        pause=False
                        if event.key==K_KP_ENTER and BooleanoP2==True:
                                if Vol_off==True:#Music On
                                        #print ("Music On")
                                        if pause==True:
                                                on_off="off"
                                                pygame.mixer.music.set_volume(1.0)
                                                Vol_off=False
                                elif Vol_off==False:#Music Off
                                        #print ("Music Off")
                                        if pause==True:
                                                on_off="on"
                                                pygame.mixer.music.set_volume(0.0)
                                                Vol_off=True
                        if event.key==K_KP_ENTER and BooleanoP3==True:#Exit
                                if pause==True:
                                        life=2
                                        SCORE=0
                                        cont3=0
                                        pause=False
                                        BooleanoP3=False
                                        BooleanoP1=True
                                        return inicio()
        score,score_rect=texto(str(SCORE) , WIDTH/8 , 40)
        vida,vida_rect = texto(str(life+1) , WIDTH/4 , 40)
        #Imagenes
        screen.blit(background_image.image,(0,0))
        screen.blit(Donkey.image,Donkey.rect)
        screen.blit(score,score_rect)
        screen.blit(vida,vida_rect)
        screen.blit(stairs1.image,(44,412))
        screen.blit(stairs2.image,(21,572))
        screen.blit(stairs3.image,(181,410))
        screen.blit(stairs3.image,(227,410))
        screen.blit(stairs3.image,(181,68))
        screen.blit(stairs3.image,(227,68))
        screen.blit(stairs4.image,(591,548))
        screen.blit(stairs5.image,(522,434))
        screen.blit(stairs5.image,(385,388))
        screen.blit(stairs5.image,(454,276))
        screen.blit(stairs5.image,(362,184))
        screen.blit(stairs6.image,(591,322))
        screen.blit(floor1.image,(0,708))
        screen.blit(floor2.image,(0,662))
        screen.blit(floor2.image,(0,548))
        screen.blit(floor2.image,(0,388))
        screen.blit(floor2.image,(181,592))
        screen.blit(floor2.image,(341,662))
        screen.blit(floor2.image,(568,592))
        screen.blit(floor2.image,(365,366))
        screen.blit(floor3.image,(158,388))
        screen.blit(floor4.image,(430,638))#4,0
        screen.blit(floor4.image,(499,616))#4,1
        screen.blit(floor4.image,(589,524))#4,2
        screen.blit(floor4.image,(523,504))#4,3
        screen.blit(floor4.image,(453,478))#4,4
        screen.blit(floor4.image,(385,456))#4,5
        screen.blit(floor4.image,(454,342))#4,6
        screen.blit(floor4.image,(523,320))#4,7
        screen.blit(floor4.image,(592,298))#4,8
        screen.blit(floor5.image,(520,410))
        screen.blit(floor6.image,(0,250))
        screen.blit(floor7.image,(250,160))
        screen.blit(pauline.image,pauline.rect)
        screen.blit(barril1.image,(barril1.rect))
        screen.blit(barril2.image,(barril2.rect))
        screen.blit(barril3.image,(barril3.rect))
        screen.blit(barril4.image,(barril4.rect))
        screen.blit(barril5.image,(barril5.rect))
        screen.blit(barril6.image,(barril6.rect))
        screen.blit(menupausa.image,menupausa.rect)
        screen.blit(protagonista.image,(protagonista.rect))
        screen.blit(Return,Return_rect)
        screen.blit(MusicOnorOf,MusicOnorOff_rect)
        screen.blit(Exit,Exit_rect)
        
        pygame.display.flip()
        
    
       
                
    return 0
#Función que inicia el juego
if __name__ == '__main__':
        pygame.init()
        inicio()
