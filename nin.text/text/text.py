'''
Created on Jul 30, 2011

@author: jake
'''
'''
Created on Jul 28, 2011
@author: jake (ninmonkeys@gmail.com)
@about: text class, easily extendable
@version: 0.0.1

see also:
    ...
    
Other people's projects:
    http://www.pygame.org/project-Reader-1813-.html
    http://www.pygame.org/docs/ref/font.html
    http://www.pygame.org/wiki/SimpleFontManager?parent=CookBook

# Todo: #
    
    [will be when googlecode dir]
        -load from 'demo.py': import text
            !!Todo: !! need move this code to text.py (outside __init__) !!
        -cleanup code comments before posting.
        #Todo: -unit testing
            -done? todo: test exception on bad fontname (load_font)
    (draw like wesnoth)
        bg=black, text_surface opacity = 50%
        
    todo: view sysfont patch fix : https://gist.github.com/1162771
'''
  
#WINDOW_TITLE = "testing nin.text / .font"

print 'hi' 

import logging
import pygame
from pygame.locals import *
from pygame import Color, Rect, Surface

fontnames = dict()
#todo: fontthemes = dict() # "normal", "mono", "sans", "serif", "script", ... 

color_fg = Color("gray80") 
color_bg = Color('gray10')
logging.basicConfig(level=logging.ERROR)
font_ui = None
#Todo: aliases: , fontmanager.alias(...)
    #fontnames = dict()
    #fontnames['ui'] = load_font('consolas', 22) 

def load_font(name=None, size=16):
    """returns valid pygame.font.Font()"""
    if name:
        filename = pygame.font.match_font(name)
        if filename is None:
            logging.warn("load_font(): .match_font() failed! : {}".format(name))
            raise Exception("text.load_font(): filename not found ({}, {})".format(name, size))
                
    logging.info("load_font() loaded! as key = ({}, {})".format(filename, size))
    return pygame.font.Font(filename, size)    

class FontManager(object):
    """maintains list of all pygame.font.Font() instances. And .render()'s pygame.Surface()
    
#TODO:
    `in` operator, ex: if 'arial' in fonts: ...
    """
    
    # logger = logging.getLogger('FontManager') #not right? or valid for self scope?
    def __init__(self):            
        self._fonts = dict()        
        self.color_bg = color_bg
        self.color_fg = color_fg
        #redundant ? TODO: self.default = self.add(None, 14)
        
    #TODO: def alias(self, name, fontkey):
    # # also write .render(alias, text, color_bg)
    # raise NotImplementedError()
        
    def add(self, name, size, bold=False, italic=False):
        """add (font, size) to manager. returns key, to save for use.
        ex:
            uifont = fonts.add("arial", 23)
            fonts.draw(uifont, "hi world")
        """                       
        k = (name, size)
                
        # already in it?
        #        if (name,size) in self._fonts:
        if k in self._fonts:
            logging.debug("FontManager.add: ({}, {}) is already loaded.".format(name, size))
        else:
            logging.debug("FontManager.add: loaded font (size,name) = ({}, {})".format(name, size))                        
            self._fonts[k] = load_font(name, size)        
        
        if bold or italic: logging.warning("Fontmanager.add( ..., bold, italic ) -- not yet implemented")        
        return k #(name, size)
                                
    def render(self, key, text, color_bg=None, color_fg=None, aa=True):
        """render if existing key, and returns pygame.Surface() or None
        
        ex:
            fonts.render(uifont, "hi world")
            fonts.render (('arial',12), "hi 2"))
        """
        if not key in self._fonts:
            logging.warn("warning: .drawing: {} invalid key".format(key))
            
            # autoload if font size/name not in memory            
            #if True: # was: self.load_font_on_bad_key:
            if not key == None: 
                logging.debug("key invalid, but loading font from .render()")                
                self.add(*key)                
                     
        # if key: exists:            
        if not color_bg: color_bg = self.color_bg
        if not color_fg: color_fg = self.color_fg
        
        
        if aa:
            logging.debug(".render(AA) : {}, '{}', AA=True, fg={}, bg={}".format(key, text, self.color_fg, color_bg))
            surf = self._fonts[key].render(text, True, self.color_fg, color_bg)
        else:
            logging.debug(".render(not AA) : {}, '{}', AA=False, {}".format(key, text, self.color_fg))
            surf = self._fonts[key].render(text, False, self.color_fg)            
        return surf
        
    def clear(self):
        """free memory / list"""
        self._fonts = dict()
    def __str__(self):
        return "<FontManager()> Fonts loaded = " + str([k for k in self._fonts.keys()])
        
        
class TextLine(object):
    """
    Todo: cache surface 
    Todo: @Properties + members
        rect
        color
        color_bg
        fontkey(name,size)
        text
        surf?
        dirty?
        
    """
    pass
    def __init__(self, text, topleft=None, fontkey=None, aa=True, color=None, color_bg=None):
        if color: raise NotImplementedError('imp: color set')        
        if color_bg: raise NotImplementedError('imp: color_bg set')
        
        if fontkey is None: fontkey = ('verdana', 24)  #Todo: use global default?
        if topleft is None: rect = Rect(0,0,1,1)
        
        self.fontkey = fontkey
        self.rect = rect
        self.text = text
        self.aa = aa
        
        self.dirty=True
        self.color = Color("purple")
        self.color_bg = color_bg
        self.screen = pygame.display.get_surface()
        self.fonts = fontmanager
        
    def _render(self):
        """forcedraw, if dirty"""
        self.dirty=False
        s = self.fonts.render(self.fontkey, self.text, aa=self.aa)
        r = s.get_rect()
        r.topleft = self.rect.topleft
        self.surf = s
        self.rect = r
        
    def draw(self):
        """call to blit text"""
        if self.dirty: self._render()
        # blit 
        self.screen.blit(self.surf, self.rect)
#        self.screen.blit(s, r)
        
        # surf = self.fonts.render(font_ui, "hi world! moo! [consolas,40], AA=True", aa=False)
#        r = surf.get_rect()
#        r.topleft = (150, 40)
#        self.screen.blit(surf, r)
#        
#        #2                        
#        surf2 = self.fonts.render(('constantia', 17), "[solid bg, no alpha, AA=True]")
##            surf2 = self.fonts.render(('arial', 40), "consolas! bg")
#        r2 = surf2.get_rect()
#        r2.topleft = r.bottomleft        
#        self.screen.blit(surf2, r2)
#        
#        #3
#        surf3 = self.fonts.render(('calibri', 25), "[solid bg, AA=False]", aa=False)
##            surf2 = self.fonts.render(('arial', 40), "consolas! bg")
#        r3 = surf3.get_rect()
#        r3.topleft = r2.bottomleft        
#        self.screen.blit(surf3, r3)
#
#        #4            
#        surf4 = self.fonts.render(('arial', 25), "bg=darkblue [solid bg, AA=False]", aa=True, color_bg=Color("darkblue"))
#        r4 = surf3.get_rect()
#        r4.topleft = r3.bottomleft        
#        self.screen.blit(surf4, r4)
        
    def __str__(self):
        return "<TextLine( rect={}, key={}, text='{}' )>".format(self.rect, self.fontkey, self.text)
    
class TextFPS(object):
    def __init__(self): raise NotImplementedError('nyi')
    