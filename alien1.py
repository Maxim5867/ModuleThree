import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #Класс, представляющий одного пришельца

    def __init__(self,ai_game):
        #инициализирует пришельца и задает его начальную позицию
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #загружаем изображение пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/alien.jpg')
        self.rect = self.image.get_rect()

        #каждый новый пришелец появляется в верхнем левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #сохранение точной горизонтальной позиции пришельца
        self.y = float(self.rect.y)

    def check_edges(self):
        #возвращает True, если пришелец находится у края экрана
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        #перемещаем корабли пришельцев вправо или влево
        self.y += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.y = self.y
