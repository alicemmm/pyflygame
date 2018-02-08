import pygame
from pygame.sprite import Group

from game_stats import GameStats
from settings import Setting
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Setting()

    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_setting)

    myship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_setting, screen, myship, aliens)

    # alien = Alien(ai_setting, screen)

    while True:
        gf.check_event(ai_setting, screen, myship, bullets)
        if stats.game_active:
            myship.update()
            gf.update_bullets(ai_setting, screen, myship, aliens, bullets)
            gf.update_aliens(ai_setting, stats, screen, myship, aliens, bullets)

        gf.update_screen(ai_setting, screen, myship, aliens, bullets)

run_game()