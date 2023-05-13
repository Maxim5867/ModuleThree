import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    #Класс, представляющий одного пришельца

    def __init__(self,ai_game):
        #инициализирует пришельца и задает его начальную позицию
        super().__init__()
        self.screen = ai_game.screen

        #загружаем изображение пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/star.jpg')
        self.rect = self.image.get_rect()

        #каждый новый пришелец появляется в верхнем левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)