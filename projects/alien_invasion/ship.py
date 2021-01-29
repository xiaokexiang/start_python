"""
处理飞船在画布上的相关内容
画布的坐标：
0,0 —————————————————————————>
   |
   |
   |
   |                         1200,800
"""
import pygame


class Ship:

    def __init__(self, setting, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')  # 加载飞船图像
        self.rect = self.image.get_rect()  # 获取飞船的属性(长宽坐标)
        self.screen_rect = screen.get_rect()  # 获取屏幕(画布)的属性，画布左上角为0,0 右下角为1200,800
        self.rect.centerx = self.screen_rect.centerx  # 设置飞船在画布的底部中央
        self.rect.bottom = self.screen_rect.bottom  # 最终坐标为(600,800)
        self.moving_right = False  # 标记飞船是否向右移动
        self.moving_left = False  # 标记飞船是否向左移动
        self.setting = setting
        self.center = float(self.rect.centerx)  # centerx只能存储整数，所以用center存储小数

    """
    根据坐标修改飞船的位置
    """

    def blit_ship(self):
        self.screen.blit(self.image, self.rect)

    """
    根据键盘的event修改飞船的位置
    防止飞船超出边界
    """

    def update_ship(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.setting.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.setting.ship_speed_factor
        self.rect.centerx = self.center  # centerx 只存储center的整数部分！！！
