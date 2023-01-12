import pygame
from components import Deck, Bar


class Character:
    def __init__(self, deck, animations) -> None:
        self.deck = deck
        self.hand = self.deck.draw()

        self.animations = animations
        self.health = 100
        self.health_bar = Bar()
        self.mana = 3

        self.active = None

    def draw(self, screen):
        self.animations[0].update()
        self.animations[0].draw(screen, 100, 100)

        for card in reversed(self.hand):
            if card != self.active:
                card.draw(screen)

        if self.active:
            self.active.draw(screen)

    def update(self):
        if self.active:
            self.active.set_pos(*pygame.mouse.get_pos())
