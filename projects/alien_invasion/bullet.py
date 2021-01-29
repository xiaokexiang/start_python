"""
子弹相关的类
"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, setting, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        # 设置子弹的属性，默认在0,0坐标处，每次子弹的位置都是基于飞船的横坐标
        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)  # 创建矩形0,0位置长宽指定
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = setting.bullet_color
        self.speed_factor = setting.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor  # 更新数值
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)  # 屏幕上绘制子弹
