"""Track statistics for the Alien Invasion game.
This class store and manages game-related state information, 
such as the number of remaining ships (lives).
"""
class GameStats():

    def __init__(self, ship_limit):
        """Initialize game statistics.

        Args:
            ship_limit (int): The number of ships the player stars with
        """
        self.ships_left = ship_limit
        
        
    
    