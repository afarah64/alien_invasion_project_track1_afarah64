import pygame
from alien import Alien

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class AlienFleet:
    """A class to manage the fleet of aliens in the Alien Invasion game.
    handles fleet creation, movement, and collision detection.
    and fleet state updates.
    """

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the alien fleet.

        Args:
            game (AlienInvasion): the main game instance.
        """
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_shift_left_speed = self.settings.fleet_shift_left_speed  

        self.create_fleet()

    def create_fleet(self):
        """Create a grid-based fleet of aliens positioned on the screen.
        """
        alien_height = self.settings.alien_height
        alien_width = self.settings.alien_width
        screen_height = self.settings.screen_height
        screen_width = self.settings.screen_width
        
        fleet_height, fleet_width = self.calculate_fleet_size(
            alien_height, screen_height, alien_width, screen_width)

        y_offset, x_offset = self.calculate_offsets(
            alien_height, alien_width, screen_height, screen_width, fleet_height, fleet_width)
        
        
        self.create_rectangle_fleet(
            alien_height, alien_width, fleet_height, fleet_width, y_offset, x_offset)

    
    def create_rectangle_fleet(self, alien_height, alien_width, 
                               fleet_height, fleet_width, 
                               y_offset, x_offset):
        """Populate the fleet with aliens in a rectangular grid

        Args:
            alien_height (int): height of each alien
            alien_width (int): width of each alien
            fleet_height (int): number of rows
            fleet_width (int): number of colums
            y_offset (int): vertical starting offset
            x_offset (int): Horizontal starting offset.
        """
        for col in range(fleet_width):
            for row in range(fleet_height): 
                current_y = alien_height * row + y_offset
                current_x = alien_width * col + x_offset
                if row % 2 ==0 or col % 2 ==0:   
                    continue
            
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_height, alien_width, screen_height, screen_width, fleet_height, fleet_width):
        """Calculate offsets to position the fleet on the screen.

        Args:
            alien_height (int): Height of each alien
            alien_width (int): Width of each alien
            screen_height (int): Height of the screen
            screen_width (int): Width of the screen
            fleet_height (int): Number of rows in the fleet
            fleet_width (int): Number of columns in the fleet

        Returns:
            tuple[int, int]: (y_offset, x_offset) for positioning the fleet
        """
        fleet_vertical_spacing = fleet_height * alien_height

        fleet_horizontal_spacing = fleet_width * alien_width
        
        y_offset = int((screen_height - fleet_vertical_spacing) // 2)
        
        x_offset = int(screen_width - fleet_horizontal_spacing - self.settings.alien_width)
        return y_offset,x_offset

    def calculate_fleet_size(self, alien_height, screen_height, alien_width, screen_width):
        """Determine how many aliens fit on the screen.
        Args:
            alien_height (int): Height of each alien
            screen_height (int): Height of the screen
            alien_width (int): Width of each alien
            screen_width (int): Width of the screen

        Returns:
            tuple[int, int]: Number of rows and columns in the fleet.
        """
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
        """Create a single alien and add it to the fleet.

        Args:
            current_x (int): Horizontal position of the alien
            current_y (int): vertical position of the alien
        """
        new_alien = Alien(self, current_x, current_y)
        
        self.fleet.add(new_alien)

    def check_fleet_edges(self):
        """Detect if any alien has reached a screen edge.
        if so, move the fleet left and reverse direction.
        """
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        """Move the entire fleet to the left"""
        for alien in self.fleet:
            alien.x -= self.settings.fleet_shift_left_speed
            alien.rect.x = int(alien.x)
    
    def update_fleet(self):
        """Update all aliens in the fleet."""
        self.check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """Draw all aliens in the fleet."""
        alien = 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """Check for collisions between aliens and another sprite group.

        Args:
            other_group (pygame.sprite.Group): Group to check collisions with.

        Returns:
            dict: Collision dictionary from pygame.groupcollide.
        """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_left_edges(self):
        """Check if any alien has reached the left edge of the screen.

        Returns:
            bool: True if an alien touches the left boundary
        """
        alien = 'Alien'
        for alien in self.fleet:  
            if alien.rect.left <= 0:
                return True
        return False
    
    def check_destroyed_status(self):
        """Check whether all aliens have destroyed.

        Returns:
            bool: True if the fleet is empty.
        """
        return not self.fleet
    
   