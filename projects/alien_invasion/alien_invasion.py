"""
pip3 install pygame
"""
from ship import Ship
from setting import Setting
from game_stats import GameStats
from pygame.sprite import Group
import game_functions as gf
import pygame


def run_game():
    # 初始化有游戏并创建屏幕对象
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(setting, screen)
    bullets = Group()  # 基于组的概念管理子弹
    aliens = Group()  # 基于组的概念管理外星人
    gf.create_fleet(setting, screen, ship, aliens)
    stats = GameStats(setting)
    while True:
        gf.check_events(setting, screen, ship, bullets)
        if stats.game_active:
            ship.update_ship()
            gf.update_bullets(setting, screen, ship, aliens, bullets)
            gf.update_aliens(setting, stats, screen, ship, aliens, bullets)
        gf.update_screen(setting, screen, ship, aliens, bullets)


run_game()
