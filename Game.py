import pygame
import random
from Player1 import Baby
from Enemy import WhiteVan
pygame.init()

screen_info = pygame.display.Info()

screen_size = (screen_width, screen_height) = \
    (int(screen_info.current_w * 1),
     int(screen_info.current_h * 1))

screen = pygame.display.set_mode(screen_size)

clock = pygame.time.Clock()

character = Baby((120, 120))
WhiteVans = pygame.sprite.Group()

font = pygame.font.SysFont(None, 30)


def init():
    WhiteVans.empty()
    for i in range (6):
        WhiteVans.add(WhiteVan((random.randint(50, screen_width - 50),
                          random.randint(50, screen_height - 50))))
def main():
    dead = False
    score = 0
    init()
    while True:
        score += 1/60
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    character.accel.x += 0.1
                if event.key == pygame.K_LEFT:
                    character.accel.x -= 0.1
                if event.key == pygame.K_UP:
                    character.accel.y -= 0.1
                if event.key == pygame.K_DOWN:
                    character.accel.y += 0.1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    character.accel.x -= 0.1
                if event.key == pygame.K_LEFT:
                    character.accel.x += 0.1
                if event.key == pygame.K_UP:
                    character.accel.y += 0.1
                if event.key == pygame.K_DOWN:
                    character.accel.y -= 0.1
        character.update()
        WhiteVans.update()

        player_hit = pygame.sprite.spritecollide(character, WhiteVans, False)

        if player_hit:
            init()
            character.reset((150, 150))
            dead = True

        screen.fill((90, 127, 255))
        if not dead:
            character.draw(screen)
        WhiteVans.draw(screen)

        text = font.render("Time Survived: " + str(int(score)) + " seconds", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (200, 45)
        screen.blit(text, text_rect)
        pygame.display.flip()
        if dead:
            dead = False
            pygame.time.delay(1000)
            score = 0;

if __name__=="__main__":
    main()
