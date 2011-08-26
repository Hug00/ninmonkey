import pygame
from pygame.locals import *
from pygame import Rect

import numpy as np
from random import randint
import os

debug = False # display map as text

TILE_W = 32
TILE_H = 32
TILE_ID_ROAD = 3
TILE_ID_GROUND = 2

class Map():
    """stores map info, and draws tiles.
    Map is stored as an array of int's which correspond to the tile id."""
    def __init__(self,game):
        """set default map"""
        self.game = game
        self.screen = game.screen
        self.load_tileset("tileset.bmp")
        
        
        self.reset()
        self.randomize()
    
    def load_tileset(self, image="tileset.bmp"):        
        """load tileset image"""
        self.tileset = pygame.image.load(os.path.join("images", image)).convert()
        self.rect = self.tileset.get_rect()
        
    def reset(self):
        """clear map, reset to defaults."""
        # calculate number of tiles to fill the screen
        self.tiles_x = self.game.width / TILE_W
        self.tiles_y = self.game.height / TILE_H

        # create empty array, fill with zeros.                  array[tiles_x, tiles_y]
        self.tiles = np.zeros( (self.tiles_x, self.tiles_y ), dtype=int)        
        if debug: print "\n-- self.tiles = --\n", self.tiles
            
    def randomize(self):
        """sets tiles to random values"""

        # randomize all tiles
        for y in range(self.tiles_y):
            for x in range(self.tiles_x):
                    self.tiles[x,y] = randint(0,TILE_ID_GROUND)

        # example of 2d array slicing, ex: slicing whole column or row
        # set a couple roads: one horizontal, one vertical.
        self.tiles[1,:] = TILE_ID_ROAD
        self.tiles[:,2] = TILE_ID_ROAD
        if debug: print "\n-- self.tiles = --\n", self.tiles
            
    def draw(self):
        # loop all tiles, and draw
        
        for y in range( self.tiles_y ):
                for x in range( self.tiles_x ):
                    # draw tile at (x,y)
                    id = self.tiles[x,y]

                    # get rect() to draw only tile from the tileset that we want
                    destRect = Rect( x * TILE_W, y * TILE_H, TILE_W, TILE_H )
                    srcRect = Rect( id * TILE_W, 0, TILE_W, TILE_H )

                    self.screen.blit( self.tileset, destRect, srcRect )
        
