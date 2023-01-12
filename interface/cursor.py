import pygame


class Cursor:
    def __init__(self, image):
        self.image = pygame.image.load(image).convert_alpha()
        self.image.set_colorkey((0, 255, 0))

        # Rendering the cursor
        surf = pygame.Surface((45, 45), pygame.SRCALPHA)
        surf.blit(self.image, (0, 0))
        self.cursor = pygame.cursors.Cursor((0, 0), surf)

        pygame.mouse.set_cursor(self.cursor)
