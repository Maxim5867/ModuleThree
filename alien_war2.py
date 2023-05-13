import sys
import pygame
from setting2 import Setting
from ship2 import Ship
from bullet2 import Bullet
from alien2 import Alien
from bg2 import Background
import random

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

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        

        #self._create_fleet()
        #self._create_stars()

    def run_game(self):
        #запуск одного цикла игры
        while True:
            self._check_event()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
    
    #def _create_fleet(self):
        #создание флота пришельцев

        #создание пришельца и вычисление количества пришельцев в ряду
        #интервал между соседними пришельцами равен ширине пришельца
        #alien = Alien(self)
        #alien_width,alien_height = alien.rect.size
        #available_space_x = self.settings.screen_width - (2*alien_width)
        #number_aliens_x = available_space_x // (2*alien_width)

        #определим количество рядов, которые помещаются на экране
        #ship_height = self.ship.rect.height
        #available_space_y = (self.settings.screen_height - (3*alien_height)-ship_height)
        #number_rows = available_space_y // (2*alien_height)

        #создание флота пришельцев
        #for row_number in range(number_rows):
            # создание ряда пришельцев
            #for alien_number in range(number_aliens_x):
                #создаем пришельца и размещаем его в ряду
                #elf._create_alien(alien_number,row_number)
    
    #def _create_stars(self):
        star = Star(self)
        star_width,star_height = star.rect.size
        avai_space_x = self.settings.screen_width - (4*star_width)
        number_star_x = avai_space_x // (4*star_width)

        ship_height = self.ship.rect.height
        avai_space_y = (self.settings.screen_height - (6*star_height)-ship_height)
        number_row = avai_space_y // (6*star_height)
        for row_number in range(number_row):
            for alien_number in range(number_star_x):
                #number_star_x = random.randint(0,100)
                number_row = random.randint(-10,50)
                self._create_star(alien_number,row_number)
        
        
    
    #def _create_star(self,star_number,rows_number):
        star = Star(self)
        star_width,star_height = star.rect.size
        star.x = star_width + 4*star_width*star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height+6*star.rect.height*rows_number
        self.aliens.add(star)
            

    #def _create_alien(self,alien_number,row_number):
        #alien = Alien(self)
        #alien_width,alien_height = alien.rect.size
        #alien.x = alien_width + 2*alien_width*alien_number
        #alien.rect.x = alien.x
        #alien.rect.y = alien.rect.height+2*alien.rect.height*row_number
        #self.aliens.add(alien)

    def _update_bullets(self):
        #обновляет позиции снаядов и унчтожает старые снаряды
        #обновление позиции снарядов
        self.bullets.update()
        #удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
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
        background = pygame.image.load('images/phon.jpg')
        self.screen.blit(background, (0,0))
        self.ship.blitme()
        

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)
        self.stars.draw(self.screen)
        
        

        #отображение последнего прорисованного экрана
        pygame.display.flip()

if __name__ == '__main__':
    #создаем экземпляр и запускаем игру
    aw = AlienInvasion()
    aw.run_game()