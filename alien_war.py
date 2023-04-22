import sys
import pygame
from setting import Setting
from ship import Ship

class AlienInvasion:
    #класс для управления русурсами и поведениями игр

    def __init__ (self):
        #инициализируем игру и создаем игровые ресурсы
        pygame.init()
        self.settings = Setting()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption('Инопланетное вторжение')

        self.ship = Ship(self)

    def run_game(self):
        #запуск одного цикла игры
        while True:
            self._check_event()
            self.ship.update()
            self._update_screen()
            
    def _check_event(self):
        #отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #переместить корабль вправо
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        #переместить корабль влево
                        self.ship.moving_left = True

                        
                    #elif event.key == pygame.K_UP:
                        #переместить корабль наверх
                      #  self.ship.moving_up = True
                   # elif event.key == pygame.K_DOWN:
                       # #переместить корабль вниз
                       # self.ship.moving_under = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        #конец перемещения корабля вправо
                        self.ship.moving_right = False  
                    if event.key == pygame.K_LEFT:
                        #конец перемещения корабля вправо
                        self.ship.moving_left = False  


                    #if event.key == pygame.K_UP:
                        #конец перемещения корабля наверх
                       # self.ship.moving_up = False
                    #if event.key == pygame.K_DOWN:
                        #конец перемещения корабля вниз
                        #self.ship.moving_under = False

    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #отображение последнего прорисованного экрана
        pygame.display.flip()

if __name__ == '__main__':
    #создаем экземпляр и запускаем игру
    aw = AlienInvasion()
    aw.run_game()

