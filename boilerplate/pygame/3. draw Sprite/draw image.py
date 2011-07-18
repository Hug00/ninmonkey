WINDOW_TITLE = "pygame boilerplate - draw image "

import pygame
from pygame.locals import * 
from pygame.sprite import Sprite
import random
import os
# ( draw image edit: 2011/06/30 ) jake

class Snake(Sprite):
    """Derives from Sprite().
    
    this gives us a Surface() and a Rect() to store a loaded image.
    """
    def __init__(self, file=None):
        """create surface"""
        Sprite.__init__(self)
        # get main screen, save for later
        self.screen = pygame.display.get_surface()                
        
        if file is None: file = os.path.join('data', 'pygame_logo.gif')
        self.load(file)
        
    def draw(self):
        """draw to screen"""
        self.screen.blit(self.image, self.rect)
    
    def load(self, filename):
        print "Snake.loading: ", filename
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()	

class GameMain(object):
    """game Main entry point. handles intialization of game and graphics, as well as game loop"""    
    done = False
    color_bg = Color('seagreen') # or also: Color(50,50,50) , or: Color('#fefefe')
    
    def __init__(self, width=800, height=600):
        """Initialize PyGame window.
        
        variables:
            width, height = screen width, height
            screen = main video surface, to draw on
            
            fps_max     = framerate limit to the max fps
            limit_fps   = boolean toggles capping FPS, to share cpu, or let it run free.
            color_bg    = backround color, accepts many formats. see: pygame.Color() for details
        """
        pygame.init()

        # save w, h, and screen
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode(( self.width, self.height ))
        pygame.display.set_caption( WINDOW_TITLE )        

        # fps clock, limits max fps
        self.clock = pygame.time.Clock()
        self.limit_fps = True
        self.fps_max = 40        

        self.snake = Snake()

    def main_loop(self):
        """Game() main loop.
        Normally goes like this:
        
            1. player input
            2. move stuff
            3. draw stuff
        """
        while not self.done:
            # get input            
            self.handle_events()
            
            # move stuff            
            # self.update()
            
            # draw stuff
            self.draw()
            
            # cap FPS if: limit_fps == True
            if self.limit_fps: self.clock.tick( self.fps_max )
            else: self.clock.tick()
    
    def draw(self):
        """draw screen"""
        # clear screen."
        self.screen.fill( self.color_bg )
        
        # draw code
        self.snake.draw()
        
        # update / flip screen.
        pygame.display.flip()
        
    def update(self):
        """move guys."""
        pass

    def handle_events(self):
        """handle events: keyboard, mouse, etc."""
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.QUIT: self.done = True
            # event: keydown
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE: self.done = True
                    
if __name__ == "__main__":         
    print """Keys:
    ESC    = quit
"""
    
    game = GameMain()
    game.main_loop()    
