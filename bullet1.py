import pygame
import sys
from pygame.sprite import Sprite


class Bullet(Sprite):
    #класс для управления снарядами, выпущенными кораблем

    def __init__(self,ai_game):
        #создать объект снарядов в текущем положении корабля
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #создание снаряда в позиции (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0,10,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midleft = ai_game.ship.rect.midright
        #позиция снаряда хранится в вещственном формате
        self.x = float(self.rect.x)
        #self.bullet = Bullet(ai_game)
        #angle = -10
        #self.bullet = pygame.transform.rotate(angle,self.bullet)
    
    def update(self):
        #перемещает снаряд вверх по экрану
        #обновляет позиции снаряда в вещественном формате
        self.x -= self.settings.bullet_speed
        
        #обновление позиции прямоугольника
        self.rect.x = self.x
    
    def draw_bullet(self):
        #вывод снаряда на экран
        pygame.draw.rect(self.screen, self.color, self.rect)
