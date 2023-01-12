import pygame


class Text:
    def __init__(self, font, size, color):
        self.name = font
        self.size = size
        self.color = color
        self.font = pygame.font.SysFont(font, size)

    def draw(self, screen, text, x, y):
        text = self.font.render(text, True, self.color)
        screen.blit(text, (x, y))
