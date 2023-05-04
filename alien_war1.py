import sys
import pygame
from setting import Setting
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    #класс для управления русурсами и поведениями игр

    def __init__ (self):
        #инициализируем игру и создаем игровые ресурсы
        pygame.init()
        self.settings = Setting()
        

        Vopr = input('''В каком режиме вы хотите играть:
        в полноэкранном(G) или в оконном(O)''')
        if Vopr == 'G':
            self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        elif Vopr == 'O':
            self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        pygame.display.set_caption('Инопланетное вторжение')
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        

    def run_game(self):
        #запуск одного цикла игры
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
    
    def _update_bullets(self):
        #обновляет позиции снаядов и унчтожает старые снаряды
        #обновление позиции снарядов
        self.bullets.update()
        #удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.x > 1600:
                self.bullets.remove(bullet)
        
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
                    elif event.key == pygame.K_q:
                        sys.exit() 
                    elif event.key == pygame.K_SPACE:
                        self._fire_bullet()
                    #elif event.key == pygame.K_DOWN:
                        #переместить корабль наверх
                        #self.ship.moving_up = True
                    #elif event.key == pygame.K_UP:
                        #переместить корабль вниз
                        #self.ship.moving_under = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        #конец перемещения корабля вправо
                        self.ship.moving_right = False  
                    if event.key == pygame.K_LEFT:
                        #конец перемещения корабля вправо
                        self.ship.moving_left = False 
                    #if event.key == pygame.K_DOWN:
                        #конец перемещения корабля наверх
                        #self.ship.moving_up = False
                    #if event.key == pygame.K_UP:
                        #конец перемещения корабля вниз
                        #self.ship.moving_under = False
            

    def _fire_bullet(self):
        #создание нового снаряда и включение его в группу
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #отображение последнего прорисованного экрана
        pygame.display.flip()

if __name__ == '__main__':
    #создаем экземпляр и запускаем игру
    aw = AlienInvasion()
    aw.run_game()
