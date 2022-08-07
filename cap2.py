#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mi_fuente=pygame.font.Font(None,20)

"""
import os 
from time import sleep as tm 
from pygame.locals import *
import pygame,sys
from pygame.sprite import Sprite
from os import getcwd as ruta
WID=1000
HEIG=300
class goku(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.goku= pygame.image.load(str(ruta())+"/gokuCar/gokri.png")
        self.rect=self.goku.get_rect()
        self.rect.centerx=WID/2
        self.rect.centery=HEIG/2       
        self.velocidad_movimiento=30
        self.puntos_limite=20

    def limites_goku(self):
        ##limites superiores
        if self.rect.centerx>=WID-10:
            self.rect.centerx=WID-13
        elif self.rect.centery>=WID-10:
            self.rect.centery=WID-20
        
        ##limites inferiores
        elif self.rect.centerx<11:
            self.rect.centerx=11
        elif self.rect.centery<11:
            self.rect.centery=11        
    def mover_solo_goku(self,detener_si_se_dipara):
        if detener_si_se_dipara:
            self.rect.centerx=self.rect.centerx  
            self.rect.centery=self.rect.centery
        else:
            self.rect.centerx+=1

    def dibujar(self,teclas,ventana):

        for teclas_precionadas in teclas:
            if teclas_precionadas==K_LEFT:
                self.rect.centerx-=self.velocidad_movimiento+100
                self.goku=pygame.image.load(str(ruta())+"/gokuCar/gokuleft.png")
            if teclas_precionadas==K_RIGHT:
                self.rect.centerx+=self.velocidad_movimiento+10
                self.goku=pygame.image.load(str(ruta())+"/gokuCar/gokri.png")
            elif teclas_precionadas==K_DOWN:
                self.rect.centery+=self.velocidad_movimiento
                self.goku=pygame.image.load(str(ruta())+"/gokuCar/gokudown.png")
            elif teclas_precionadas==K_UP:
                self.rect.centery-=self.velocidad_movimiento
                self.goku=pygame.image.load(str(ruta())+"/gokuCar/gokuup.png")

            ventana.blit(self.goku,self.rect)
        ventana.blit(self.goku,self.rect)    

class cameHaa(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.came=pygame.image.load(str(ruta())+"/spriteDisparo/kame.gif")
        self.came_haa_imagen=pygame.transform.scale(self.came,(12,12))

        self.rect=self.came_haa_imagen.get_rect()
        self.rect.centerx=x
        self.rect.centery=y
        self.kame_ha_goku_disparo=False
        self.velocidad=2

    def dibujar(self,ventana):
        self.rect.centerx+=self.velocidad
        ventana.blit(self.came_haa_imagen,self.rect)



def main():
    ##VARIABLES DE INICIO DE PYGAME 
    pygame.init()
    ventana=pygame.display.set_mode((WID,HEIG))
    pygame.display.set_caption("dos")

    ##PREDETERMINAMOS UNA FUENTE
    fuente_de_letas=pygame.font.Font(None,20)

    ##pintamos la venta
    ventana.fill((100,100,150))
    #muneco1=goku()
    
    ##fondo de la ventana
    fondo=pygame.image.load("namek.jpg")
    fondo_redimencionado=pygame.transform.scale(fondo,(ventana.get_width(),ventana.get_height()+500))
    muneco1=goku()

    #suelo_juego=suelo()
    
    detener_si_se_dipara=False
    lista_de_disparos=[]
    while True:
        teclas_precionadas=[]
        
        ###posicion actual
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.exit()

            ##teclas presionadas
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    muneco1.goku=pygame.image.load(str(ruta())+"/gokuCar/kame.png")        
                    detener_si_se_dipara=True

                    print(muneco1.rect.centerx,muneco1.rect.centery)
                    kame_kame=cameHaa(muneco1.rect.centerx,muneco1.rect.centery)
                    lista_de_disparos.append(kame_kame)
                
                     

                ##agregamos teclas ala lista
                teclas_precionadas.append(event.key)
            
            ##teclas soltadas 
            elif event.type==pygame.KEYUP:
                muneco1.goku=pygame.image.load(str(ruta())+"/gokuCar/gokri.png")
                
                if event.key==K_SPACE:
                    detener_si_se_dipara=False

        print(detener_si_se_dipara)
        muneco1.dibujar(teclas_precionadas,ventana)
        muneco1.limites_goku()
        muneco1.mover_solo_goku(detener_si_se_dipara)


        #####metodos de la clase disparo
        if len(lista_de_disparos)>0:
            for recorrer_disparos in lista_de_disparos:
                recorrer_disparos.dibujar(ventana)
                ###eliminamso items
                if recorrer_disparos.rect.centerx>=ventana.get_width():
                    lista_de_disparos.remove(recorrer_disparos)

        
        pygame.display.update()
        

        ##fondo map
        ventana.blit(fondo_redimencionado,(0,0))

main()

