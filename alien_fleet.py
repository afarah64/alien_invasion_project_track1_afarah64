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
        self.fleet_shift_left_speed = self.settings.fleet_shift_left_speed  

        self.create_fleet()

    def create_fleet(self):
        """Create a vertical Column of aliens on the right edge."""
        
        alien_height = self.settings.alien_height
        alien_width = self.settings.alien_width
        screen_height = self.settings.screen_height
        screen_width = self.settings.screen_width
        
        fleet_height, fleet_width = self.calculate_fleet_size(alien_height, screen_height, alien_width, screen_width)

        y_offset, x_offset = self.calculate_offsets(alien_height, alien_width, screen_height, screen_width, fleet_height, fleet_width)
        
        
        self.create_rectangle_fleet(alien_height, alien_width, fleet_height, fleet_width, y_offset, x_offset)

    
    def create_rectangle_fleet(self, alien_height, alien_width, fleet_height, fleet_width, y_offset, x_offset):
        for col in range(fleet_width):
            for row in range(fleet_height): 
                current_y = alien_height * row + y_offset
                current_x = alien_width * col + x_offset
                if row % 2 ==0 or col % 2 ==0:   
                    continue
            
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_height, alien_width, screen_height, screen_width, fleet_height, fleet_width):
        fleet_vertical_spacing = fleet_height * alien_height

        fleet_horizontal_spacing = fleet_width * alien_width
        
        y_offset = int((screen_height - fleet_vertical_spacing) // 2)
        
        x_offset = int(screen_width - fleet_horizontal_spacing - self.settings.alien_width)
        return y_offset,x_offset

    def calculate_fleet_size(self, alien_height, screen_height, alien_width, screen_width):

        #how many alien fit in the screen height 
        fleet_height = (screen_height // alien_height)
        fleet_width = ((screen_width/2)//alien_width)
        if fleet_height % 2 == 0:
            fleet_height -= 1
        else:
            fleet_height -= 2

        if fleet_width % 2 == 0:
            fleet_width -= 1
        else:
            fleet_width -= 2
        
        return int(fleet_height), int(fleet_width)
        
    def _create_alien(self, current_x:int, current_y:int):
        new_alien = Alien(self, current_x, current_y)
        
        self.fleet.add(new_alien)

    def check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.fleet:
            alien.x -= self.settings.fleet_shift_left_speed
            alien.rect.x = int(alien.x)
    
    def update_fleet(self):
        """Update the positions of all aliens in the fleet."""
        self.check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """Draw the fleet of aliens to the screen."""
        alien = 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def chech_fleet_left_edges(self):
        alien = 'Alien'
        for alien in self.fleet:  
            if alien.rect.left <= 0:
                return True
        return False
   