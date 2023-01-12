import pygame
from dataclasses import dataclass


@dataclass
class Card:
    width: int = 100
    height: int = 150
    x: int = 0
    y: int = 0
    color: tuple = (255, 0, 0)
    hover_ratio: float = 0.2
    is_hoveing: bool = False

    def __post_init__(self):
        self.card = pygame.Rect(self.x, self.y, self.width, self.height)
        self.hover = pygame.Rect(
            self.x - self.width * self.hover_ratio / 2,
            self.y - self.height * self.hover_ratio,
            self.width * (1 + self.hover_ratio),
            self.height * (1 + self.hover_ratio),
        )

    def draw(self, screen):
        if self.is_selected(*pygame.mouse.get_pos()):
            pygame.draw.rect(screen, self.color, self.hover)
            self.is_hoveing = True
        else:
            pygame.draw.rect(screen, self.color, self.card)
            self.is_hoveing = False

    def set_x(self, x) -> None:
        self.x = x
        self.card.x = x
        self.hover.x = x - self.height * self.hover_ratio / 2

    def set_y(self, y) -> None:
        self.y = y
        self.card.y = y
        self.hover.y = y - self.height * self.hover_ratio

    def set_pos(self, x, y) -> None:
        self.set_x(x - self.width / 2)
        self.set_y(y - self.height / 2)

    def is_selected(self, x, y) -> bool:
        if self.is_hoveing:
            return self.hover.collidepoint(x, y)

        return self.card.collidepoint(x, y)
