import pygame

class Ship():
    #класс для управления кораблем
    def __init__(self,ai_game):
        #инициализировать корабль и задать его первоначальную позицию
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #загрузит изображение корабля и получить прямоугольник
        self.image = pygame.image.load('images/ship.jpg')
        self.rect = self.image.get_rect()
        #каждый  новый корабль появляется у нижней границы экрана
        self.rect.midbottom = self.screen_rect.midbottom


        self.x = float(self.rect.x)
        #self.y = float(self.rect.y)
        #флаги перемещения
        self.moving_right = False
        self.moving_left = False
        #self.moving_up = False
        #self.moving_under = False

    def update(self):
        #обновляет позицию корабля с учетом флага
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        #if self.moving_up:
            #self.y += self.setting.ship_speed
        #if self.moving_under:
            #self.y -= self.setting.ship_speed
        
        self.rect.x = self.x
        #self.rect.y = self.y


    def blitme(self):
        #рисуем корабль в текущей позиции
        self.screen.blit(self.image,self.rect)
