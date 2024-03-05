from random import randrange
from secrets import choice, randbelow
import pygame
from pygame.locals import *
from pygame import mixer
import sys
import os
import time

#Ancho y alto de la ventana del juego
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 625

class nave(pygame.sprite.Sprite): # Clase que va a tener las caracterissticas de las naves

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Snake/medios/rocket_up.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = 550
        self.rect.left = 500

class Estrella(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Snake/medios/resizeimagestar.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = choice([i*5 for i in range(6,100)])
        self.rect.left = choice([i*5 for i in range(1,190)])

class Meteoro(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Snake/medios/meteoro2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = choice([i*5 for i in range(6,100)])
        self.rect.left = choice([i*5 for i in range(1,190)])

def play_background_music():
    # Comprueba si la canción ya está reproduciéndose
    if not pygame.mixer.get_busy():
        songback = pygame.mixer.Sound("Snake/Stay-Inside-Me.ogg")
        songback.set_volume(0.1)
        songback.play(-1)

def Main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))  #Tamaño de la ventana del juego
    pygame.display.set_caption("Space Game")#Nombre del juego
    icono = pygame.image.load("Snake/medios/reicono.png").convert()
    pygame.display.set_icon(icono)

    mixer.init()
    play_background_music()
   
    #Las 3 clases del juego
    meteoros = pygame.sprite.Group()
    estrellas = pygame.sprite.Group()
    nave1 = nave()
    #Imagenes de la Pantalla de inicio
    wallpaperblur = pygame.image.load("Snake/medios/image.png").convert()
    logo1 = pygame.image.load("Snake/medios/Logo2.png").convert_alpha()
    logo2 = pygame.image.load("Snake/medios/win.png").convert_alpha()
    logo3 = pygame.image.load("Snake/medios/GameOver.png").convert_alpha()
    waifu = pygame.image.load("Snake/medios/top3.png").convert_alpha()
    waifu3 = pygame.image.load("Snake/medios/top33.png").convert_alpha()
    boton = pygame.image.load("Snake/medios/Botonrere.png").convert_alpha()
    naveblur = pygame.image.load("Snake/medios/blur.png").convert_alpha()
    #Fin Imagenes de la Pantalla de inicio
    waifuwin = pygame.image.load("Snake/medios/YorXD.png").convert_alpha()
    wallpaper = pygame.image.load("Snake/medios/8bitspace.jpg").convert()
    atras = pygame.image.load("Snake/medios/backbutton.png").convert_alpha()
    clock = pygame.time.Clock()
    
    pygame.display.flip()
    
    #Variables de los cohetes de la pantalla de inicio
    mov1 = 700
    mov2 = 900
    mov3 = 1200
    mov4 = 1500

    logopos1 = 120
    logopos2 = 90
    botonpos1 = 330
    botonpos2 = 290 
    
    for _ in range(0,10):
        estrella2 = Estrella() 
        estrellas.add(estrella2)
    for _ in range(0,5):
        meteoro2 = Meteoro()
        meteoros.add(meteoro2)

    contador = 0
    
    
#Bucle principal del juego (Pantalla de inicio)
    main = True
    Inicio = True
    run = False
    win = False
    gameOver = False
    while main:
        while Inicio:
            pygame.mouse.set_visible(True)
            pos_mouse = pygame.mouse.get_pos()
            screen.blit(wallpaperblur,(0,0))
            screen.blit(naveblur,(100,mov1))
            screen.blit(naveblur,(300,mov3))
            screen.blit(naveblur,(500,mov4))
            screen.blit(naveblur,(800,mov2))
            screen.blit(logo1,(logopos1,logopos2))
            screen.blit(boton,(botonpos1,botonpos2))
                       
            mov1 -= 0.5
            mov2 -= 0.5
            mov3 -= 0.5
            mov4 -= 0.5
            
            if mov1 < -50 :
                mov1 = 700
            if mov2 < -50:
                mov2 = 900
            if mov3 < -50:
                mov3 = 1200
            if mov4 < -50:
                mov4 = 1500
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif pos_mouse[0] > 331 and pos_mouse[0] < 612 and pos_mouse[1] > 375 and pos_mouse[1] < 489:
                    boton = pygame.image.load("Snake/medios/Botonpressed.png").convert_alpha()
                    if event.type == pygame.MOUSEBUTTONUP:
                        run = True
                        Inicio = False
                elif pos_mouse[0] < 331 or pos_mouse[0] > 612 or pos_mouse[1] < 375 or pos_mouse[1] > 489:
                    boton = pygame.image.load("Snake/medios/Botonrere.png").convert_alpha()
            pygame.display.flip()
        
        # Comienzo del juego
        while run:
            estrellasenmapa = len(estrellas)
            print(estrellasenmapa)
            pygame.mouse.set_visible(False)
            if nave1.rect.left > 960: #Esto hace que el jugador no se salga de la pantalla
                nave1.rect.left = 960
            elif nave1.rect.left < 0:
                nave1.rect.left = 0
            elif nave1.rect.top < 0:
                nave1.rect.top = 0
            elif nave1.rect.top > 585:
                nave1.rect.top = 585 #Esto hace que el jugador no se salga de la pantalla

            fuente = pygame.font.Font("Snake/New_Wild_Words.ttf", 18)
            mensaje = fuente.render("Puntaje: "+str(contador), True, (255, 255, 255))
            clock.tick(60) #Esto son los fps del juego
            pygame.key.set_repeat(1, 25) # Esto permite que el juego funcione si el jugador deja un tecla presionada
            screen.blit(wallpaper,(0,0))
            estrellas.draw(screen) 
            meteoros.draw(screen)    
            screen.blit(nave1.image,(nave1.rect.left,nave1.rect.top))
            pygame.draw.rect(screen,(128,0,128),(0,0,120,20))
            screen.blit(mensaje, (0, 0))
            
            estrellas.update()
            meteoros.update()
            colision = pygame.sprite.spritecollide(nave1, estrellas, True)
            muerte = pygame.sprite.spritecollide(nave1,meteoros,False)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_UP or event.key == K_w:
                        nave1.rect.top -= 5
                        nave1.image = pygame.image.load("Snake/medios/rocket_up.png").convert_alpha()
                        if estrellasenmapa == 0:
                                run = False
                                win = True
                        if colision:
                            contador += 1
                            if estrellasenmapa == 0:
                                run = False
                                win = True
                        elif muerte:
                            run = False
                            gameOver = True
                    elif event.key == K_DOWN or event.key == K_s:
                        nave1.rect.top += 5
                        nave1.image = pygame.image.load("Snake/medios/rocket_down.png").convert_alpha()  
                        if estrellasenmapa == 0:
                                run = False
                                win = True
                        if colision:
                            contador += 1
                            if estrellasenmapa == 0:
                                run = False
                                win = True
                        elif muerte:
                            run = False
                            gameOver = True                 
                    elif event.key == K_LEFT or event.key == K_a:
                        nave1.rect.left -= 5
                        nave1.image = pygame.image.load("Snake/medios/rocket_left.png").convert_alpha()
                        if estrellasenmapa == 0:
                                run = False
                                win = True
                        if colision:
                            contador += 1
                            if estrellasenmapa == 0:
                                run = False
                                win = True
                        elif muerte:
                            run = False
                            gameOver = True                   
                    elif event.key == K_RIGHT or event.key == K_d:
                        nave1.rect.left += 5
                        nave1.image = pygame.image.load("Snake/medios/rocket_right.png").convert_alpha()
                        if estrellasenmapa == 0:
                                run = False
                                win = True
                        if colision:
                            contador += 1
                            if estrellasenmapa == 0:
                                run = False
                                win = True
                        elif muerte:
                            run = False
                            gameOver = True         
        while win:
            pos_mouse = pygame.mouse.get_pos()
            pygame.mouse.set_visible(True)
            screen.blit(wallpaperblur,(0,0))
            screen.blit(logo2,(90,logopos2))
            screen.blit(waifuwin,(0,400))
            screen.blit(waifuwin,(860,400))
            screen.blit(atras,(400,400))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif pos_mouse[0] > 402 and pos_mouse[0] < 525 and pos_mouse[1] > 402 and pos_mouse[1] < 523:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Inicio = True
                        win = False
                        Main()
        while gameOver:
            pos_mouse = pygame.mouse.get_pos()
            pygame.mouse.set_visible(True)
            screen.blit(wallpaperblur,(0,0))
            screen.blit(logo3,(100,logopos2))
            screen.blit(waifu,(0,400))
            screen.blit(waifu3,(750,400))
            screen.blit(atras,(400,400))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif pos_mouse[0] > 402 and pos_mouse[0] < 525 and pos_mouse[1] > 402 and pos_mouse[1] < 523:
                    if event.type == pygame.MOUSEBUTTONUP:
                        Inicio = True
                        gameOver = False
                        Main()
                                           
if __name__ == "__main__":
    Main()
