from importlib.util import set_loader


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
        self.bullet_allowed = 10

        # Alien Setting
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represent right; -1 represents left.
        self.fleet_direction = 1

        # How quickly the alien points value increase
        self.score_scale = 1.5
        # How Quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """Initialize setting that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Fleet direction of 1 represent right; -1 represent left.
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed setting"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
