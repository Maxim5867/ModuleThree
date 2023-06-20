import pygame

class Ship():
    #класс для управления кораблем
    def __init__(self,ai_game):
        #инициализировать корабль и задать его первоначальную позицию
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #загрузит изображение корабля и получить прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        angle = -90#потом убрать
        #потом убрать 
        self.image = pygame.transform.rotate(self.image,angle)
        #каждый  новый корабль появляется у нижней границы экрана
        self.rect.midleft = self.screen_rect.midleft


        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #флаги перемещения
        #self.moving_right = False
        #self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        #обновляет позицию корабля с учетом флага
        if self.moving_up and self.rect.bottom < self.screen_rect.bottom :
            self.y += self.setting.ship_speed
        if self.moving_down and self.rect.top > 0:
            self.y -= self.setting.ship_speed
        #if self.moving_up:
            #self.y += self.setting.ship_speed
        #if self.moving_under:
            #self.y -= self.setting.ship_speed
        
        self.rect.y = self.y
        #self.rect.y = self.y
    
    def center_ship(self):
        #размещает корабль в центре нижней части экрана
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

    def blitme(self):
        #рисуем корабль в текущей позиции
        self.screen.blit(self.image,self.rect)
