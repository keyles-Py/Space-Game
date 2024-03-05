import pygame
from secrets import choice

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