import pygame

from Object import Object

class Baby(Object):
    def __init__(self, pos):
        super().__init__("B.png", pos)
        self.image = pygame.transform.smoothscale(self.image, (70, 70))
        self.accel = pygame.math.Vector2()



    def update(self):
        self.speed += self.accel
        screeninfo = pygame.display.Info()
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
        super().update()


    def reset(self, pos):
        self.rect.center = pos
        self.image.set_alpha(0)
        pygame.time.delay
