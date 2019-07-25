import pygame
from player import Player1


pygame.init()
screen_info = pygame.display.Info()

screensize = (screen_width, screen_height) =\
    (int(screen_info.current_w * 0.5),
    int(screen.info_current_h * 0.5))

clock = pygame.time.Clock()
main_character = Player1(120, 120)

def main():
    while True:
        clock.tick(60)

if__name__=="__main__":
    main()