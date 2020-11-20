import sys
import pygame as pg

class AlienInvasion:
    """Overall class to handle game assets and behavior"""

    def __init__(self):
        """Initialize the game and create resources."""
        pg.init()
        self.screen = pg.display.set_mode((1200, 800))
        pg.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                    #Make the most recently drawn screen visible.
                    pg.display.flip()
    
if __name__ == '__main__':
    #Mkae a game instace, and run the game
    ai = AlienInvasion()
    ai.run_game()
