import sys
import pygame

class Setting():
    #Класс для хранения всех настроек игры

    def __init__(self):
        #инициализируем настройки игры

        #параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
