GAME_ABOUT = """about:
	example of using a tileset to draw a map
"""

import pygame
from pygame.locals import *	
#  import jakelib
#  from jakelib.text import Text, FPSText
from map import Map	

VERSION = "1"
GAME_TITLE = "part5: map tiles v%s" % VERSION

GAME_HOTKEYS = """== Hotkeys! ===
	space = random map
	ESC	= quit
"""
	
class Game():
	"""game Main entry point. handles intialization of game and graphics.
	
	methods:
		__init__(width, height) : just init
	members:
		map : Map() object
		screen : screen display surface		
	"""
	done  = False # controls if you want to quit
	
	
	def __init__(self, width=640, height=480):
		"""Initialize PyGame"""		
		pygame.init()
		self.width, self.height = width, height

		self.clock = pygame.time.Clock()

		self.screen = pygame.display.set_mode(( self.width, self.height ))
		pygame.display.set_caption( "%s%s" % (GAME_TITLE, VERSION) )

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
