class Setting():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 10
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed_factor = 12
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 166, 23, 194
        self.bullets_allowed = 22

        #外星人设置
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

