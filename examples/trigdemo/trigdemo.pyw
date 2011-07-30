'''
Created on Jul 18, 2011
about:
    visualize trig
    
1: angle to coord:
    from center of circle, to mouse, get angle
2:
'''

import pygame
from pygame.locals import *
from pygame import Color, Rect, Surface
import numpy as np
import math

pygame.init()
# not normally all global, but simplified demo
color_bg = Color("gray20")    
color_fg = Color("gray80")
clock = pygame.time.Clock()   
font_path = pygame.font.match_font('arial')
screen = pygame.display.set_mode((600,400))

class Text():
    """spartan text class. Does not cache surface."""
    def __init__(self, text=None):
        self.font = pygame.font.Font(font_path, 20)
        if text is None: text = "default text"
        self._text = text
        self.rect = Rect(0,0,0,0)
        self.render()
        
    def text(self, text):
        """change text"""
        self.render(text)
                
    def render(self, text=None):
        if text is None: text = self._text
        self._text = text
        self.surface = self.font.render( self._text, True, color_fg )
        self.rect.size = self.surface.get_rect().size
                
    def draw(self):
        screen.blit(self.surface,self.rect)


class Game():
    def __init__(self):
        self.mouse_loc = (0,0)
        self.txt1 = Text("loc")

    def draw(self):                
            screen.fill( color_bg )
            
            # unit circle
            center = screen.get_rect().center
            pygame.draw.circle( screen,color_fg, center , 100, 2) 
            
            self.txt1.draw()
            
            #line to mouse
            pygame.draw.aaline(screen, color_fg, center, self.mouse_loc)            
            pygame.display.flip()
            
            # [1] angle to mouse
            dx = center[0] - self.mouse_loc[0]
            dy = center[1] - self.mouse_loc[1]
            rad = math.atan2(dy, dx)
            
            self.txt1.text(  "angle to mouse, from center = deg: {deg}, rad: {rad} ".format(rad=rad,
                                                         deg=int(math.degrees(rad))) ) 
            clock.tick(80)
    
    def loop(self):
        done=False
    #    pygame.init()
    
    
        while not done:
            events = pygame.event.get()
            
            for event in events:
                if event.type == pygame.QUIT: done = True
                # event: keydown
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE or event.key == K_SPACE: done = True
                elif event.type == MOUSEMOTION:
                    self.mouse_loc = event.pos

            self.draw()
            
g = Game()
g.loop()