import pygame
from alien import Alien

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class AlienFleet:
    """A class to manage the fleet of aliens."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the fleet."""
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_right_speed = self.settings.fleet_right_speed  

        self.create_fleet()

    def create_fleet(self):
        """Create a vertical Column of aliens on the right edge."""
        
        alien_height = self.settings.alien_height
        screen_height = self.settings.screen_height
        
        #Calulate how many aliens fit vertically

        fleet_height = self.calculate_fleet_size(alien_height, screen_height)

        fleet_vertical_spacing = fleet_height * alien_height
        y_offset = int((screen_height - fleet_vertical_spacing) // 2)
        
        right_side_x = self.settings.screen_width - self.settings.alien_width - 20
        
        for row in range(fleet_height): 
            
            current_y = alien_height * row + y_offset
            if row % 2 ==0:
                continue
            
            self._create_alien(right_side_x, current_y)

    def calculate_fleet_size(self, alien_height, screen_height):

        #how many alien fit in the screen height 
        fleet_height = (screen_height // alien_height)

        if fleet_height % 2 == 0:
            fleet_height -= 1
        else:
            fleet_height -= 2

        return fleet_height
        
    def _create_alien(self, right_side_x:int, current_y:int):
        new_alien = Alien(self, right_side_x, current_y)
        
        self.fleet.add(new_alien)

    def draw(self):
        """Draw the fleet of aliens to the screen."""
        alien = 'Alien'
        for alien in self.fleet:
            alien.draw_alien()
