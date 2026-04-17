import pygame
from pygame.sprite import Sprite

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """Defines the Alien class used in the Alien Invasion game.
    Each alien is a sprite that moves horizontally and interacts 
    with screen boundaries.
    """

    def __init__(self, fleet: 'AlienFleet', x: float, y: float) -> None:
        """Initialize the alien at a specific position."""
        super().__init__()
        
        self.fleet = fleet

        # store a reference to the game instance and its settings and screen attributes
        self.screen = fleet.game.screen
        #get the boundaries of the screen to ensure the alien stays within them
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.settings

        # Load the bullet image and scale it to the specified width and height from settings.
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_width, self.settings.alien_height)
            )
        # rotate the image 
        self.image = pygame.transform.rotate(self.image, -90)

        # Get the rect of the image
        self.rect = self.image.get_rect()
        # Set the position of the alien
        self.rect.x = x
        self.rect.y = y
        
        #store vertical and horizontal position as float for movement
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Update the alien's position.
        Moves the alien top and bottom depending on the fleet direction.
        """
        temp_speed = self.settings.fleet_speed

        self.y += temp_speed * self.fleet.fleet_direction
        self.rect.y = int(self.y)
        self.rect.x = int(self.x)
        


    def check_edges(self):
        """Check whether the alien has reached screen edge.

        Returns:
            _bool_: True if the alien touches the top or bottom edge.
        """
        return (self.rect.bottom >= self.boundaries.bottom or self.rect.top <= 0)


    def draw_alien(self):
        """Draw the alien to the screen.
        """
        self.screen.blit(self.image, self.rect)
        
