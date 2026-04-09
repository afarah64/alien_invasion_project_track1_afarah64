import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Ship:
    """A class to manage the ship."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the ship and set its starting position."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
                (self.settings.ship_width, self.settings.ship_height)
                )
        # Get the rect of the ship image and the screen.
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def draw(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)    