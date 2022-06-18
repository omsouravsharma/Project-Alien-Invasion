import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """
    Overall class to manage game asset and behavior. 
    """

    def __init__(self):
        """Initialize the game, and create game resource"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Set the background color
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to right
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        # Redraw the screen each pass throught the loop
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        # Make the most recent drawn screen visisble.
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()