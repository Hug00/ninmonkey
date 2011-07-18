'''
@copyright: jake 2011
@author: jake
about: nin: colors example.
@version: 0.1

Note:
    search the code for "Color", "random_color", and "search_color"
    
Usage:
    Feel free to use code as you want!
'''
VERSION = '0.2.1'

from random import choice
import sys
 
import pygame
from pygame.locals import * 
from pygame import Color, Rect
import colors
from colors import random_color, search_color


DEBUG = False
VERBOSE = False

class Thumbnail():
    """Thumbnail that has a surface, with a background color set"""
    def __init__(self, width=64):
        self.surface_thumb = Rect(0,0,width,width)
        self.rect_thumb = Rect(0,0,width,width)
                    
        # ex [1] the standard pygame.Color("white") , same as Color("#ffffff")
        self.color_bg = Color("white")                
        # ex [2] random color with a filter:
        self.color_bg = random_color('light')
        self.color_border = random_color('dark')
        
        # create empty surface;  fill it
        self.surface_thumb = pygame.Surface([width, width])
        self.surface_thumb.fill(self.color_bg)
    
    def fill(self):
        """clear thumb."""
        self.surface_thumb.fill(self.color_bg)

    def move(self, x, y):
        """move all rects/images together"""
        self.rect_thumb.move_ip(x,y)
  
    def draw(self, screen):        
        screen.blit(self.surface_thumb, self.rect_thumb)
                
    def __str__(self): return "<Thumbnail( bg={bg}, rect_thumb={rect_thumb} >".format(bg=self.color_bg, rect_thumb=self.rect_thumb)
 
class Game(object):
    """store Surface's, draw, get user input""" 
    def __init__(self, width=1024, height=768):
        self.screen = None
        self.width = width
        self.height= height
        self.done = False
        self.thumbs = []
        self.thumb_w = 64
        self.screen = pygame.display.set_mode((width, height))        
        self.color_bg = Color("gray20")
        
        pygame.init()
        pygame.display.set_caption("colors.py : ninmonkey v{}".format(VERSION))
        self.clock = pygame.time.Clock()        
    
        
    def start(self, search="light"):
        """creates initial grid, with default search. """
        if VERBOSE: print "start( search={} )".format(search)
        self.thumbs = []
        
        thumb_w, thumb_h = 64, 64
        numx = self.width / thumb_w
        numy = self.height / thumb_h
        self.caption_prepend(search)
        
                
        self.thumbs = []
        for y in range(numy):
            for x in range(numx):
                t = Thumbnail(width=self.thumb_w)                
                if search: t.color_bg = random_color(search)
                # else: t.color_bg = Color('gray')
                
                t.fill()                
                t.move(thumb_w * x, thumb_h * y)                                                
                self.thumbs.append(t)
                    
    def handle_events(self):
        # keypress
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE: self.done = True
                elif event.key == K_SPACE:
                    search = choice(['', 'white', 'purple','green','dark','light','red','blue','orange','gray','blue','green'])
                    self.start(search)
                
                elif event.key == K_1: self.thumb_w = 64
                elif event.key == K_2: self.thumb_w = 32
                elif event.key == K_3: self.thumb_w = 16
                elif event.key == K_4: self.thumb_w = 8
    
    def caption_prepend(self, pre):
        "prepend default window text"
        template1 = "colors.py : ninmonkey v{v}  [thumbs: len()]".format(v=VERSION)
        t = "{} -- {}".format(pre, template1)
        pygame.display.set_caption(t)
    
    def caption(self, text):
        "changes window text"
        pygame.display.set_caption(text)
        
    def loop(self):
        while not self.done:
            self.handle_events()
            self.draw()

    def draw(self):
        """draw; clear, draw, flip."""
        self.screen.fill(self.color_bg)        
        for t in self.thumbs: t.draw(self.screen)        
        pygame.display.flip()
        self.clock.tick(60)
        

if __name__ == '__main__':
    print """colorstest.py [nin]
    w,h = {width}x{height}

Hotkeys:
    Spacebar = random_color(search)
    1, 2, 3, 4 = change square size
    Escape    = exit
    """.format(width=1024, height=768)
    
    g = Game()
    g.start()
    g.loop()
