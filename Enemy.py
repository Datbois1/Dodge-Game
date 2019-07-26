import pygame
import random

from Object import Object

class WhiteVan(Object):
    def __init__(self, pos):
        super().__init__("black-and-white-van-png--964.png", pos)
        self.image = pygame.transform.smoothscale(self.image, (140, 80))
        self.acce1 = pygame.math.Vector2()



    def update(self):
        screeninfo = pygame.display.Info()
        self.rect.move_ip(self.speed)
        screenwidth = screeninfo.current_w
        if self.rect.right > screenwidth:
            self.speed.x *= -1
        if self.rect.left < 0:
            self.speed.x *= -1
        screenheight = screeninfo.current_h
        if self.rect.top < 0:
            self.speed.y *= -1
        if self.rect.bottom > screenheight:
            self.speed.y *= -1
        self.accel = (random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1))
        self.speed += self.accel
        super().update()
