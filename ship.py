import pygame

class Ship():
    """初始化飞机并设置其初始位置"""
    def __init__(self, ai_setting, screen):
        self.screen = screen
        self.ai_setting = ai_setting

        self.img = pygame.image.load('images/ship.png')
        self.rect = self.img.get_rect()
        self.screen_rect = self.screen.get_rect()

        #放在屏幕中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.upcenter = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.upcenter -= self.ai_setting.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.upcenter += self.ai_setting.ship_speed_factor

        self.rect.centerx = self.center
        self.rect.centery = self.upcenter

    def blitme(self):
        self.screen.blit(self.img, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx