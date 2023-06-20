import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    #класс для вывода игровой информации

    def __init__(self,ai_game):
        #инициализируем атрибуты подсчета очков
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        

        #настроим параметры шрифта для вывода счета 
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        self.image = pygame.image.load('images/ship.jpg')

        #подготовим исходное изображение
        self.prep_score()
        self.high_score()
        self.prep_level()
        #self.prep_ship()

    def prep_score(self):
        #преобразуем текущий счет в графическое изображение
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,self.settings.bg_color)

        #вывод счета в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def high_score(self):
        #преобразуем текущий счет в графическое изображение
        high_score_str = str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        #вывод рекорда в левой верхней части экрана
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.center = self.screen_rect.center 
        self.high_score_rect.top = 20
    
    def prep_level(self):
        #преобразуем текущий уровень в графическое изображение
        level_str = str(self.settings.level)
        self.level_image = self.font.render(level_str, True, self.text_color,self.settings.bg_color)

        #вывод уровня в правой верхней части экрана ниже счета
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 80

    #def prep_ship(self):
        #self.ships = Group()
        #for ship_number in range(self.stats.ships_left):
            #ship = Ship(self.settings, self.screen)
            #ship.rect.x = 10 + ship_number * ship.rect.width
            #ship.rect.y = 10
            #self.ships.add(ship)
    
    def show_score(self):
        #вывод счета на экран
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #self.ships.draw(self.screen)
