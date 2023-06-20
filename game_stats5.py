class GameStats():
    #отслеживает статистику игры

    def __init__(self,ai_game):
        #получим настройки игры
        self.settings = ai_game.settings
        self.reset_stats()
        #игра будет запускаться в активном состоянии
        self.game_active = False
        with open("record.txt", "r") as rec_file:
            score_file = rec_file.read()
            if score_file != '':
                self.high_score = int(score_file)
            else:
                self.high_score = 0


    def reset_stats(self):
        #инициализирую статистику, которая изменяется в процессе игры
        self.ships_lifes = 3
        self.score = 0
