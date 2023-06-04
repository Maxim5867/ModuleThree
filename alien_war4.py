import sys
import pygame
from setting4 import Setting
from ship4 import Ship
from bullet4 import Bullet
from alien4 import Alien
from game_stats4 import GameStats
from scoreboard4 import Scoreboard
from button4 import Button

class AlienInvasion:
    #класс для управления русурсами и поведениями игр

    def __init__ (self):
        #инициализируем игру и создаем игровые ресурсы
        pygame.init()
        self.settings = Setting()

        Vopr = input('''В каком режиме вы хотите играть:
        в полноэкранном(1) или в оконном(0)''')
        if Vopr == '1':
            self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        elif Vopr == '0':
            self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        else:
            Vopr = input('''В каком режиме вы хотите играть:
            в полноэкранном(1) или в оконном(0)''')

        pygame.display.set_caption('Инопланетное вторжение')

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        #Создание кнопки Play
        self.play_button = Button(self, "Play")

    def run_game(self):
        #запуск одного цикла игры
         while True:
            self._check_event()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
    
    def _create_fleet(self):
        #создание флота пришельцев

        #создание пришельца и вычисление количества пришельцев в ряду
        #интервал между соседними пришельцами равен ширине пришельца
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        available_space_x = self.settings.screen_width + self.settings.screen_height
        number_aliens_x = available_space_x // (alien_width)

        #определим количество рядов, которые помещаются на экране
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (2*alien_height)-ship_height)
        number_rows = available_space_y // (2*alien_height)

        #создание флота пришельцев
        for row_number in range(number_rows):
            # создание ряда пришельцев
            for alien_number in range(number_aliens_x):
                #создаем пришельца и размещаем его в ряду
                self._create_alien(alien_number,row_number)
            

    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = 8*alien_width + 10*alien_width
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height+alien.rect.height*row_number
        self.aliens.add(alien)
    
    def _update_aliens(self):
        #обновляет позиции всех пришельцев
        self._check_fleet_edges()
        self.aliens.update()

        #проверка столкновения корабля одного из кораблей пришельцев с нашим кораблем (коллизия)
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            print('Пришельцы победили')
            sys.exit()

    def _check_fleet_edges(self):
        #реагирует на достижение пришельцем края
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._check_fleet_direction()
                break
    
    def _check_fleet_direction(self):
        #опускает весь флот и меняет направление бокового движения 
        for alien in self.aliens.sprites():
            alien.rect.x == self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_bullets(self):
        #обновляет позиции снаядов и унчтожает старые снаряды
        #обновление позиции снарядов
        self.bullets.update()
        #удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.x > 1400:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()
        
        
        
    def _check_bullet_alien_collision(self):
        #проверка попадания в пришельца
        #при попадании удаляем снаряд и пришельца
        collision = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if not self.aliens:
            #уничтожим все снаряды
            self.bullets.empty()
            #создаем новый флот
            self._create_fleet()

    def _check_event(self):
        #отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        #переместить корабль вправо
                        self.ship.moving_up = True
                    elif event.key == pygame.K_w:
                        #переместить корабль влево
                        self.ship.moving_under = True  
                    elif event.key == pygame.K_q:
                        sys.exit() 
                    elif event.key == pygame.K_SPACE:
                        self._fire_bullet()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        #конец перемещения корабля вправо
                        self.ship.moving_up = False  
                    if event.key == pygame.K_s:
                        #конец перемещения корабля вправо
                        self.ship.moving_under = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos) 
                    
    def _check_play_button(self,mouse_pos):
        #запускает новую игру при нажатии на кнопку Play
        button_clicket = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicket and not self.stats.game_active:
            #сброс игровых настроек
            self.settings.initialize_dynamic_settings()
            #сбрасываю статистику
            self.stats.reset_stats()
            #запускаем
            self.stats.game_active = True

            #очистить списки пришельцев и снарядом
            self.aliens.empty()
            self.bullets.empty()

            #создаем новый флот и размещае корабль по центру
            self._create_fleet()
            self.ship.center_ship()

            #указатель мыши скрываем(делаем невидимым)
            pygame.mouse.set_visible(False)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

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

        self.aliens.draw(self.screen)

        #вывод информации о счете
        self.sb.show_score()
        
        #кнопка Play будет отобржаться тогда, когда игра не активна
        if not self.stats.game_active:
            self.play_button.draw_button()

        #отображение последнего прорисованного экрана
        pygame.display.flip()

if __name__ == '__main__':
    #создаем экземпляр и запускаем игру
    aw = AlienInvasion()
    aw.run_game()
