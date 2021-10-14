import pygame as pg

import color
import options
import player

pg.init()

screen = pg.display.set_mode([options.WIDTH, options.HEIGHT])
pg.display.set_caption("GAME")
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
cube = player.Player()
all_sprites.add(cube)

running = True
while running:
    
    clock.tick(options.FPS)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    all_sprites.update()

    screen.fill(color.BLACK)

    all_sprites.draw(screen)

    pg.display.flip()

pg.quit()