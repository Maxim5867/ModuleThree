import pygame
from pygame.sprite import Sprite

class Background(Sprite):
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load('images/phon.jpg')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
       
        
