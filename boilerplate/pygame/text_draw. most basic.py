'''
Created on Jul 18, 2011
about:
    draw text using pygame, without extra classes
    (if you need a spartan example)
'''

import pygame
from pygame.locals import *
from pygame import Color, Rect, Surface

def d(c, msg):
    # quick debug
    print """debug: {}
    type: {}
    print: {}""".format(msg, type(c), c)
    
def loop():
    done=False
    pygame.init()
    screen = pygame.display.set_mode((600,400))
    color_bg = Color("gray80")    
    clock = pygame.time.Clock()
    
    #Font = None
    font_obj1 = pygame.font.SysFont(None, 36)
    surf1 = font_obj1.render( "font(): None", False, Color("black"), Color("gray60") )
    rect1 = surf1.get_rect()  # = font_ui.get_rect()
    

    # font= 'arial'
    path = pygame.font.match_font('arial')
    font_obj2 = pygame.font.Font(path, 26)        
    surf2 = font_obj2.render( "Font(): 'arial'", True, Color("darkblue")) #, Color("pink") )        
    rect2 = surf2.get_rect()
    
    #debug
    if True:
        d(font_obj1, 'font1')
        d(surf1, 'surf1')
        d(rect1, 'rect1')
        d(font_obj2, 'font2')
        d(surf2, 'surf2')
        d(rect2, 'rect2')

    while not done:
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.QUIT: done = True
            # event: keydown
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_SPACE: done = True
                
        screen.fill( color_bg )
        
        screen.blit(surf1, Rect(0,0,0,0))
        x,y = rect1.bottomleft
        screen.blit(surf2, Rect(x,y,0,0))
        
        pygame.display.flip()
                
        clock.tick(40)

loop()