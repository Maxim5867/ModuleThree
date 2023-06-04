class GameStats():
    #отслеживает статистику игры

    def __init__(self,ai_game):
        #получим настройки игры
        self.settings = ai_game.settings
        self.reset_stats()

        #игра будет запускаться в активном состоянии
        self.game_active = False

    def reset_stats(self):
        #инициализирую статистику, которая изменяется в процессе игры
        self.ships_lifes = self.settings.ship_limit
        self.score = 0
