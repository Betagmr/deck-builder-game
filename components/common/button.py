import pygame
from dataclasses import dataclass


@dataclass
class Button:
    width: int = 100
    height: int = 50
    x: int = 100
    y: int = 600
    color: tuple = (255, 0, 0)
    hover_ratio: float = 0.2
    on_click: callable = lambda: print("Button clicked")

    def __post_init__(self):
        self.button = pygame.Rect(self.x, self.y, self.width, self.height)
        self.hover = pygame.Rect(
            self.x,
            self.y - self.height * self.hover_ratio,
            self.width * (self.hover_ratio + 1),
            self.height * (self.hover_ratio + 1),
        )

    def draw(self, screen):
        if self.is_selected(*pygame.mouse.get_pos()):
            pygame.draw.rect(screen, self.color, self.hover)
        else:
            pygame.draw.rect(screen, self.color, self.button)

    def is_selected(self, x, y) -> bool:
        return self.button.collidepoint(x, y)
