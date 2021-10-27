import pygame as pg

import color
import options

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(color.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (options.WIDTH//2, options.HEIGHT//2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > options.WIDTH:
            self.rect.right = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_SPACE]:
            self.rect.y -= 5
