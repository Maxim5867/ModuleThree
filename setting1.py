import pygame

class Setting():
    #Класс для хранения всех настроек игры

    #инициализируем настройки игры

    #параметры экрана
    screen_width = 800
    screen_height = 600
    bg_color = (250,250,250)

    #настройки корабля
    ship_speed = 1.5

    #параметр снаряда
    bullet_speed = -1
    bullet_width = 15
    bullet_height = 3
    bullet_color = (60,60,60)
    bullets_allowed = 5

    #настройки пришельцев
    alien_speed = 0.2
    fleet_drop_speed = 10
    #fleet_direction = 1 - движение вправо, = -1 - движение влево
    fleet_direction = 1
