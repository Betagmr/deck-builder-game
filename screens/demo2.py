import pygame

from settings import *
from utils import load_animations


def demo_2():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    sprite_sheet_image = pygame.image.load(
        "./assets/character1/NightBorne.png"
    ).convert_alpha()

    BG = (50, 50, 50)
    BLACK = (0, 0, 0)

    metadata = {
        "idle": 9,
        "run": 6,
        "attack": 12,
        "hit": 5,
        "death": 23,
    }

    selector = 0
    animation_list = load_animations(sprite_sheet_image, 70, 70, 10, metadata)

    run = True
    while run:

        dt = clock.tick(60)

        # update background
        screen.fill(BG)

        animation_list[selector].update()
        animation_list[selector].draw(screen, 100, 100)

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    selector += 1
                    if selector >= len(animation_list):
                        selector = 0

                    animation_list[selector].reset()

        pygame.display.update()
