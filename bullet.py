"""Define the Bullet class used in the Alien invasion game.
Bullets are fired from ship and travel horizontally across 
the screen to hit aliens.
"""
import pygame
from pygame.sprite import Sprite

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """Represents a bullet fired from the ship."""
    
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize a bullet at the ship's current position.

        Args:
            game (AlienInvasion): The main game instance.
        """
        
        super().__init__()
        
        # store a reference to the game instance and its settings and screen attributes
        self.screen = game.screen
        self.settings = game.settings

        # Load the bullet image and scale it to the specified width and height from settings.
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_width, self.settings.bullet_height)
            )
        # Rotate the bullet image 90 degrees counterclockwise to point it to the right.
        self.image = pygame.transform.rotate(self.image, -90)
        
        # start the bullet at ship's right edge and centered vertically on the ship
        self.rect = self.image.get_rect()
        self.rect.midleft = game.ship.rect.midright

        # Store the bullet's horizontal position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet horizontally across the screen."""
        # Move the bullet horizontally.
        self.x += self.settings.bullet_speed
        # Update the rect position.
        self.rect.x = int(self.x)

    def draw_bullet(self):
        """Draw the bullet at its current position."""
        self.screen.blit(self.image, self.rect)
        

