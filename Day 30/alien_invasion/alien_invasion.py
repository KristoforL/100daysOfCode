import sys
import pygame as pg

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to handle game assets and behavior"""

    def __init__(self):
        """Initialize the game and create resources."""
        pg.init()
        self.settings = Settings()
        
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN) 
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pg.display.set_caption("Alien Invasion")
        self.ship = Ship(self) 
        self.bullets = pg.sprite.Group()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

            #Get rid of bullets that have disappeared
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))
            

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        #Watch for keyboard and mouse events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        #Responds to keypresses
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pg.K_q:
            sys.exit()
        elif event.key == pg.K_SPACE:
            self._fire_bullet()

        
    def _check_keyup_events(self, event):
        #Responds to Key release
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Creates new bullet and adds it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #Redraw the screen during each pass through
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #Make the most recently drawn screen visible.
        pg.display.flip()
        

    
if __name__ == '__main__':
    #Make a game instace, and run the game
    ai = AlienInvasion()
    ai.run_game()
    

