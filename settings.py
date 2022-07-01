class Settings:
    """ As class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize ths game's settings"""
        # Screen Setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship setting
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet Settings:
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Alien Setting
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represent right; -1 represents left.
        self.fleet_direction = 1
