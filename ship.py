import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship:
    """A class to manage the ship."""

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        """Initialize the ship and set its starting position."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundries = game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
                (self.settings.ship_width, self.settings.ship_height)
                )
        # Rotate the ship image 90 degrees counterclockwise to point it upwards.
        self.image = pygame.transform.rotate(self.image, -90)

        # Get the rect of the ship image and the screen.
        self.rect = self.image.get_rect()
        self.boundaries = game.screen.get_rect()

        self._midleft_ship()


        #moving flags for Up and Down directions
        self.moving_up = False
        self.moving_down = False
        
        # Store the ship's vertical position as a decimal value.
        self.y = float(self.rect.y)

        # Store a reference to the arsenal instance.    
        self.arsenal = arsenal
    
    def _midleft_ship(self):
        """Center the ship on the screen."""
        self.rect.midleft = self.boundaries.midleft
        self.y = float(self.rect.y)

    def update(self):
        """ Update the ship's position and update the arsenal."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """Update the ship's position based on the movement flags."""
          
        temp_speed = self.settings.ship_speed
        # Moving Up wards (Y decreases) and check if it is within the top boundary
        if self.moving_up and self.rect.top > 0:
            self.y -= temp_speed
        
        #Moving Downwards (Y increases) and check if it is within the bottom boundary    
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed
        # Update rect object from self.x.
        self.rect.y = int(self.y)


    def draw(self):
        """Draw the ship at its current location."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect) 
    
    def fire(self):
        """Fire a bullet if limit not reached yet."""
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group):
        if pygame.sprite.spritecollideany(self, other_group):
            self._midleft_ship()
            return True
        return False
        
        