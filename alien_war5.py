import sys
from time import sleep
import pygame
from game_stats5 import GameStats
from scoreboard5 import Scoreboard
from setting5 import Setting
from ship5 import Ship
from bullet5 import Bullet
from alien5 import Alien
from button5 import Button
import pickle


class AlienInvasion:
    #класс для управления русурсами и поведениями игр

####### ИГРА
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

        #создаем экземпляр для хранения игровой статистики 
        #и панели результатов
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.stats.score = 0

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        #создание кнопки Play
        self.play_button = Button(self, "Play")

    def load_game(self):
        with open("game.txt", "rb") as load_file:
            self.settings = pickle.load(load_file)

    def save_game(self):
        with open("game.txt", "wb") as save_file:
            pickle.dump(self.settings, save_file)
        
        game = AlienInvasion()
        game.save_game("game.txt")

        loaded_game = AlienInvasion.load_game("game.txt")
        print(loaded_game.score)  
        print(loaded_game.level)        
    
    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.sb.high_score()

    def run_game(self):
        #запуск одного цикла игры
        while True:
            self._check_event()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
    
    def _check_event(self):
        #отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        #переместить корабль вправо
                        self.ship.moving_down = True
                    elif event.key == pygame.K_DOWN:
                        #переместить корабль влево
                        self.ship.moving_up = True  
                    elif event.key == pygame.K_q:
                        file_rec = open("record.txt", "w")
                        file_rec.write(str(self.stats.high_score))
                        sys.exit() 
                    elif event.key == pygame.K_p:
                        self.start_game()
                    elif event.key == pygame.K_n:
                        self.reset_game()
                    elif event.key == pygame.K_l:
                        self.load_game()
                    elif event.key == pygame.K_s:
                        self.save_game()
                    elif event.key == pygame.K_SPACE:
                        self._fire_bullet()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        #конец перемещения корабля вправо
                        self.ship.moving_down = False  
                    if event.key == pygame.K_DOWN:
                        #конец перемещения корабля вправо
                        self.ship.moving_up = False 
                    
                
                #elif event.type == pygame.MOUSEBUTTONDOWN:
                    #mouse_pos = pygame.mouse.get_pos()
                    #self._check_play_button(mouse_pos) 

    #def _check_play_button(self,mouse_pos):
        #запускает новую игру при нажатии на кнопку Play
        #button_clicket = self.play_button.rect.collidepoint(mouse_pos)
        #if button_clicket and not self.stats.game_active:
            #сброс игровых настроек
            #self.settings.initialize_dynamic_settings()
            #сбрасываю статистику
            #self.stats.reset_stats()
            #запускаем
            #self.stats.game_active = True

            #очистить списки пришельцев и снарядом
            #self.aliens.empty()
            #self.bullets.empty()

            #создаем новый флот и размещае корабль по центру
            #self._create_fleet()
            #self.ship.center_ship()

            #указатель мыши скрываем(делаем невидимым)
            #pygame.mouse.set_visible(False)
        #else:
            #self.stats.game_active = False
            #pygame.mouse.set_visible(True)
    def reset_game(self):
        self.settings.initialize_dynamic_settings()
        #сбрасываю статистику
        self.stats.reset_stats()
        #запускаем
        self.stats.game_active = True

        #очистить списки пришельцев и снарядом
        self.aliens.empty()
        self.bullets.empty()
        self.stats.score = 0
        self.settings.level = 1

        #создаем новый флот и размещае корабль по центру
        self._create_fleet()
        self.ship.center_ship()

        #указатель мыши скрываем(делаем невидимым)
        pygame.mouse.set_visible(False)
    
    def start_game(self):
        #button_clicket = self.play_button.rect.collidepoint()
        if self.stats.game_active == False:
            self.settings.initialize_dynamic_settings()
            #сбрасываю статистику
            self.stats.reset_stats()
            #запускаем
            self.stats.game_active = True

            #очистить списки пришельцев и снарядом
            self.aliens.empty()
            self.bullets.empty()
            self.stats.score = 0
            self.settings.level = 1

            #создаем новый флот и размещае корабль по центру
            self._create_fleet()
            self.ship.center_ship()

            #указатель мыши скрываем(делаем невидимым)
            pygame.mouse.set_visible(False)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
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
    
####### КОРАБЛЬ
    def _ship_hit(self):
        #обрабатывает столкновение кораблей с пришельцем
        
        if self.stats.ships_lifes > 0:
            #уменьшаем количество наших кораблей на 1
            self.stats.ships_lifes -= 1
            
            
            #очищаем группы пришельцев и снарядов
            self.bullets.empty()
            self.aliens.empty()
            #self.prep_ship()

            #создадим новый флот пришельцев и вернем наш корабль на начальное положение
            self._create_fleet()
            self.ship.center_ship()

            #пауза
            sleep(0.5)
        else:
            self.stats.game_active = False



####### ПРОТИВНИК
    def _create_fleet(self):
        #создание флота пришельцев

        #создание пришельца и вычисление количества пришельцев в ряду
        #интервал между соседними пришельцами равен ширине пришельца
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (13*alien_width)
        number_aliens_x = available_space_x // (alien_width)

        #определим количество рядов, которые помещаются на экране
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3*alien_height)- ship_height)
        number_rows = available_space_y // (3*alien_height)

        #создание флота пришельцев
        for row_number in range(number_rows):
            # создание ряда пришельцев
            for alien_number in range(number_aliens_x):
                #создаем пришельца и размещаем его в ряду
                self._create_alien(alien_number,row_number)
            

    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = 5*alien_width + 2*alien_width*alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height+ 3*alien.rect.height*row_number
        self.aliens.add(alien)
    
    def _update_aliens(self):
        #обновляет позиции всех пришельцев
        self._check_fleet_edges()
        self.aliens.update()

        #проверка столкновения корабля одного из кораблей пришельцев с нашим кораблем (коллизия)
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        
        #проверяет не добрался ли пришелец до нижнего края экран
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        #проверяет не добрался ли пришелец до нижнего края экран
        screen_rect = self.screen.get_rect()
        #ЗДЕСЬ ДЗ ПРО КАПЛИ ДОЖДЯ!
        #for alien in self.aliens.sprites():
            #if alien.rect.bottom >= screen_rect.bottom:
                #то же самое, что и столкновение пришельца с кораблем
                #self._ship_hit()
                #break

    def _check_fleet_edges(self):
        #реагирует на достижение пришельцем края
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._check_fleet_direction()
                break
    
    def _check_fleet_direction(self):
        #опускает весь флот и меняет направление бокового движения 
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

####### СНАРЯДЫ
    def _update_bullets(self):
        #обновляет позиции снаядов и унчтожает старые снаряды
        #обновление позиции снарядов
        self.bullets.update()
        #удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.right > 1400:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()
    
    def _check_bullet_alien_collision(self):
        collision = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collision:
            self.stats.score += self.settings.score_image_factor
            self.sb.prep_score()
            for aliens in collision.values():
                self.stats.score == self.settings.score_image_factor + len(aliens)
                self.sb.prep_score()
                self.check_high_score()
                
        if not self.aliens:
            #уничтожим все снаряды
            self.bullets.empty()
            #создаем новый флот
            self._create_fleet()
            self.settings.increase_speed()
            self.settings.level == self.settings.level_factor
            self.sb.prep_level()
            
            
    def _fire_bullet(self):
        #создание нового снаряда и включение его в группу
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == '__main__':
    #создаем экземпляр и запускаем игру
    aw = AlienInvasion()
    aw.run_game()
