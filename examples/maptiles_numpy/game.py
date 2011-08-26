GAME_ABOUT = """about:
    using tileset and numpy 2D array for map data
"""

import pygame
from pygame.locals import *    
from map import Map    

GAME_TITLE = "maptiles numpy {nin.example} "

GAME_HOTKEYS = """== Hotkeys! ===
    space = randomize tiles
    ESC    = quit
"""
    
class Game():
    """game Main entry point. handles intialization of game and graphics.
    
    members:
        map : Map() object
        screen : screen display surface        
    """
    done  = False
    
    
    def __init__(self, width=640, height=480):
        """Initialize PyGame"""        
        pygame.init()
        self.width, self.height = width, height

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(GAME_TITLE)

        print GAME_TITLE
        print GAME_ABOUT
        print GAME_HOTKEYS        
        #  self.fps = FPSText()
        self.map = Map(self)
            
    def main_loop(self):
        """Game() main loop"""        
        while not self.done:
            # get key input
            self.handle_events()
            # move guys
            self.update()            
            # draw guys
            self.draw()
            
            self.clock.tick(60) # set FPS limit to 60
        
    def handle_events(self):
        """do regular events."""
        events = pygame.event.get()
        for event in events:
            
            if event.type == pygame.QUIT: sys.exit()
            
            # event: keydown
            elif event.type == KEYDOWN:
                # exit on 'escape'
                if (event.key == K_ESCAPE):
                    self.done = True
                elif(event.key== K_SPACE): # random map
                    self.map.randomize()    

    def update(self):        
        """move bullets/guys. nothing to do for now."""
        pass        
    
    def draw(self):
        """render screen"""
        self.screen.fill( (150,150,150)) # clear screen, fill screen black
        
        #tiles
        self.map.draw()
        
        # draw guys here

        # fps update
        #  self.fps.draw()
        #  self.fps.tick()

        pygame.display.flip()
