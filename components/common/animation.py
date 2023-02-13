import pygame
from dataclasses import dataclass, field


@dataclass
class Animation:
    sprite_list: list = field(default_factory=list)
    coolldown: int = 100
    frame: int = 0
    current_tick: int = 0
    previous_tick: int = 0

    def __post_init__(self):
        self.n_frames = len(self.sprite_list)

    def update(self):
        self.current_tick = pygame.time.get_ticks()

        if self.current_tick - self.previous_tick > self.coolldown:
            self.previous_tick = self.current_tick
            self.frame += 1

            if self.frame >= self.n_frames:
                self.frame = 0

    def draw(self, screen, x, y):
        pos = pygame.mouse.get_pos()
        is_collide = self.sprite_list[self.frame][0].get_rect()

        if is_collide.collidepoint(pos):
            screen.blit(self.sprite_list[self.frame][1], (x, y))
            print(is_collide)

        screen.blit(self.sprite_list[self.frame][0], (x, y))

    def reset(self):
        self.frame = 0
        self.previous_tick = pygame.time.get_ticks()
