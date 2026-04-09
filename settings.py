from pathlib import Path

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        self.name = "Alien Invasion"

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        # Frames per second setting
        self.FPS = 60
        
        # Background settings
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'