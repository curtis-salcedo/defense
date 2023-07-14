import pygame as pg
import constants as c

class Turret(pg.sprite.Sprite):
    def __init__(self, image, position, tile_x, tile_y):
        pg.sprite.Sprite.__init__(self)
        self.tile_x = tile_x
        self.tile_y = tile_y
        # Calculate center coordinates of the turret
        self.x = self.tile_x * c.TILE_SIZE + (c.TILE_SIZE // 2)
        self.y = self.tile_y * c.TILE_SIZE + (c.TILE_SIZE // 2)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.angle = 0