"""
处理画布中的事件
"""
import sys
from time import sleep

import pygame
from bullet import Bullet
from alien import Alien


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
    elif event.key == pygame.K_q:  # 如果按了q键那么退出
        sys.exit()


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_setting, screen, ship, aliens, bullets):
    screen.fill(ai_setting.bg_color)  # 每次刷新前都先添加背景色
    for bullet in bullets:
        bullet.draw_bullet()  # 绘画子弹
    ship.blit_ship()
    aliens.draw(screen)
    pygame.display.flip()  # 每次循环都会更新屏幕（类似刷新）


def check_bullet_alien_collisions(setting, screen, ship, aliens, bullets):
    # 检查是否有子弹击中了外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(setting, screen, ship, aliens)


def update_bullets(setting, screen, ship, aliens, bullets):
    bullets.update()  # # 组调用会将组内的每个元素都执行update更新子弹位置
    for bullet in bullets.copy():  # 超出界外时删除消失的子弹
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(setting, screen, ship, aliens, bullets)


def fire_bullets(setting, screen, ship, bullets):
    if len(bullets) < setting.bullets_allowed:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)


def get_number_alien_x(setting, alien_width):
    available_space_x = setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_alien_y(setting, ship_height, alien_height):
    available_space_y = (setting.screen_height - ((3 * alien_height) - ship_height))
    number_aliens_x = int(available_space_y / (2 * alien_height))
    return number_aliens_x


# 创建外星人
def creat_alien(setting, screen, aliens, alien_number, row_number):
    alien = Alien(setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(setting, screen, ship, aliens):
    alien = Alien(setting, screen)
    number_aliens_x = get_number_alien_x(setting, alien.rect.width)
    number_rows = get_number_alien_y(setting, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(setting, screen, aliens, alien_number, row_number)


def update_aliens(setting, stats, screen, ship, aliens, bullets):
    check_fleet_edges(setting, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(setting, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(setting, stats, screen, ship, aliens, bullets)


def ship_hit(setting, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(setting, screen, ship, aliens)
        ship.blit_ship()
        sleep(0.5)
    else:
        stats.game_active = False


def change_fleet_direction(setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += setting.fleet_drop_speed
    setting.fleet_direction *= -1


def check_fleet_edges(setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(setting, aliens)
            break


def check_aliens_bottom(setting, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(setting, stats, screen, ship, aliens, bullets)
            break
