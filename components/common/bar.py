import pygame
from dataclasses import dataclass


@dataclass
class Bar:
    width: int = 500
    height: int = 10
    x: int = 700
    y: int = 600
    color_primary: tuple = (255, 0, 0)
    color_secondary: tuple = (0, 0, 255)

    def __post_init__(self):
        self.bar_primary = pygame.Rect(self.x, self.y, self.width, self.height)
        self.bar_secondary = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color_secondary, self.bar_secondary)
        pygame.draw.rect(screen, self.color_primary, self.bar_primary)

    def is_selected(self, x, y) -> bool:
        return self.bar.collidepoint(x, y)

    def set_percentage(self, percentage):
        self.bar_primary.width = self.width * percentage

    def inc_precentage(self, percentage):
        inc = self.width * percentage

        if self.bar_primary.width + inc > self.width:
            self.bar_primary.width = self.width
        elif self.bar_primary.width + inc < 0:
            self.bar_primary.width = 0
        else:
            self.bar_primary.width += inc
