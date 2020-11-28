import sys
import pygame as pg

from sprite import Spaceship

class MyGame:
    """My first practice at making the pygame myself"""

    def __init__(self):
        """First game window generation"""
        pg.init()
        self.screen = pg.display.set_mode((1200, 800))
        pg.display.set_caption('My Game')
        #Set background color
        self.bg_color = (150, 230, 230)
        self.sprite = Spaceship(self)

    def run_game(self):
        while True:
            self._update_screen()
            self._check_events()
        

    
    def _check_events(self):
        #Watch for keyboard and mouse events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            #Redraw the screen during each pass through
            self.screen.fill(self.bg_color)
            #Make the most recently drawn screen visible.
            pg.display.flip()


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #Redraw the screen during each pass through
        self.screen.fill(self.bg_color)
        self.sprite.blitme()
        #Make the most recently drawn screen visible.
        pg.display.flip()


if __name__ == '__main__':
    #Make a game instace, and run the game
    ai = MyGame()
    ai.run_game()