import pygame

class Baby(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__("B.png", pos)



    def update(self):
        self.rect.move_ip(self.speed)
