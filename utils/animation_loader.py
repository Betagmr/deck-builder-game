import pygame

from settings import *
from components import Animation


def compose_animation(sheet, i, width, height, margin, frames_list):
    return [
        get_image(sheet, i, j, width, height, margin) for j in range(frames_list[i])
    ]


def load_animations(sheet, width: int, height: int, margin: int, metadata: dict):
    frames_list = [i for i in metadata.values()]
    n_animations = len(frames_list)

    return [
        Animation(compose_animation(sheet, i, width, height, margin, frames_list))
        for i in range(n_animations)
    ]


def get_image(sheet, animation: int, frame: int, width: int, height: int, margin: int):
    img = pygame.Surface((width, height)).convert_alpha()
    img.blit(
        sheet,
        (0, 0),
        (
            frame * width + margin * frame,
            animation * height + margin * animation,
            width,
            height,
        ),
    )

    img.set_colorkey((0, 255, 0))
    img2 = get_outline(img, WHITE)
    img = pygame.transform.scale(img, (width * 5, height * 5))
    img2 = pygame.transform.scale(img2, (width * 5, height * 5))
    img.set_colorkey((0, 255, 0))

    return img, img2


def get_outline(image, color=WHITE):
    surf = pygame.Surface(image.get_size(), pygame.SRCALPHA)
    surf.set_colorkey((0, 0, 0))

    mask = pygame.mask.from_surface(image)
    pic_mask = mask.to_surface()
    pic_mask.set_colorkey((0, 0, 0))

    surf.blit(pic_mask, (0, 1))
    surf.blit(pic_mask, (0, -1))
    surf.blit(pic_mask, (1, 0))
    surf.blit(pic_mask, (-1, 0))

    surf.blit(image, (0, 0))

    return surf
