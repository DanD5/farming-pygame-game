import pygame
from settings import *

class SoilLayer:
    def __init__(self, all_sprites):
        
        #sprite groups
        self.all_sprites = all_sprites
        self.soil_sprites = pygame.sprite.Group()
        
        #graphics
        self.soil_surf = pygame.image.load('../graphics/soil/o.png')
        
        self.create_soil_grid()
        
    def create_soil_grid(self):
        ground = pygame.image.load('../graphics/world/ground.png')
        h_tiles, v_tiles = ground.get_width() // TITLE_SIZE, ground.get_height() // TITLE_SIZE
        
        self.grid = [ ]
        
        