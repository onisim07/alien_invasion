class GameStats():
    '''Отслеживание статистики для игры.'''

    def __init__(self, ai_game):
        '''Инициализирует статистику.'''
        self.settings = ai_game.settings
        self.reset_status()

        # Игра запускается в неактивном состоянии
        self.game_active = False

        # Игра запускается в активном состоянии:
        self.game_active = True

        # Рекорд не должен сбрасываться.
        self.high_score = 0
    def reset_status(self):
        '''Инициализирует статистику, изменяющуюся в ходе игры.'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1