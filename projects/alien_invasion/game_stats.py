"""
统计飞船信息
"""


class GameStats:
    def __init__(self, setting):
        self.setting = setting
        self.ships_left = self.setting.ship_limit
        self.game_active = True
