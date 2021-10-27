import pygame as pg

import color
import options

class Player(pg.sprite.Sprite):
    """Класс игрового персонажа.
    
    Содержит описание повдения персонажа.
    
    """
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.height = 50
        self.width = 50
        self.move_speed = 10
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(color.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = options.WIDTH//2
        self.rect.bottom = options.GROUND_LINE
        self.grounded = None
        self.jump = False
        self.jump_power = 20
        self.max_jump_height = 200

    def update(self):
        keystate = pg.key.get_pressed()
        self.jump_height = options.GROUND_LINE - self.rect.bottom
        
        def move_control(self):
            """Описывает движения персонажа по оси 'x'."""
            if keystate[pg.K_a]:
                self.rect.x -= self.move_speed
            if keystate[pg.K_d]:
                self.rect.x += self.move_speed
            if self.rect.left < 5:
                self.rect.left = 5
            if self.rect.right > options.WIDTH - 5:
                self.rect.right = options.WIDTH - 5
        
        def border_control(self):
            """Контроллирует границы для персонажа."""
            if self.rect.bottom >= options.GROUND_LINE:
                self.rect.bottom = options.GROUND_LINE
                self.grounded = True
            else:
                self.grounded = False
        
        def to_jump(self):
            """Заставляет персонажа прыгать."""
            if keystate[pg.K_SPACE] and self.grounded:
                self.jump = True
            if self.jump:
                self.rect.y -= self.jump_power
                if self.jump_height >= self.max_jump_height:
                    self.jump = False
            else:
                if self.rect.bottom < options.GROUND_LINE:
                    self.rect.y += options.GRAVITY
                else:
                    self.rect.bottom = options.GROUND_LINE
        
        move_control(self)
        border_control(self)
        to_jump(self)