class GameStats():
    """Track stats for Alien invasion"""

    def __init__(self, ai_game):
        """Initialize game stats"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.ships_left = self.settings.ship_limit