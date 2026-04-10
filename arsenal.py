import pygame
from bullet import Bullet

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Arsenal:
    """A class to manage the ship's arsenal."""
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the arsenal."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Update the positions of the bullets and get rid of old bullets."""
        self.arsenal.update()
        self.remove_bullets_offscreen()
    
    def remove_bullets_offscreen(self):
        """Remove bullets that have disappeared off the top of the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw the bullets to the screen."""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """Create a new bullet and add it to the arsenal."""
        if len(self.arsenal) < self.settings.bullets_amount:
            new_bullet = Bullet(self.game)  
            self.arsenal.add(new_bullet)
            return True
        return False