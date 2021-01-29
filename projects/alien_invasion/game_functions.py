"""
处理画布中的事件
"""
import sys

import pygame
from bullet import Bullet


def check_events(setting, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 注意判断是左右方向用key属性比较
            check_keydown_event(setting, event, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def check_keydown_event(setting, event, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:  # 创建子弹并加入组
        fire_bullets(setting, screen, ship, bullets)


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_setting, screen, ship, bullets):
    screen.fill(ai_setting.bg_color)  # 每次刷新前都先添加背景色
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blit_ship()
    pygame.display.flip()  # 每次循环都会更新屏幕（类似刷新）


def update_bullets(bullets):
    bullets.update()  # # 组调用会将组内的每个元素都执行update更新子弹位置
    for bullet in bullets.copy():  # 删除消失的子弹
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullets(setting, screen, ship, bullets):
    if len(bullets) < setting.bullets_allowed:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)
