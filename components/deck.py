import random
from components import Card


class Deck:
    def __init__(self, cards: list[Card] = [], hand_size: int = 6):
        self.cards = cards
        self.hand_size = hand_size

        self.remaining_cards = random.sample(cards, len(cards))
        self.discarted_cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card: Card):
        self.cards.remove(card)

    def shuffle(self):
        return random.sample(self.discarted_cards, len(self.discarted_cards))

    def draw(self):
        hand = []

        if len(self.remaining_cards) < self.hand_size:
            hand += self.remaining_cards
            self.remaining_cards = self.shuffle()
            self.discarted_cards = []

        extra_cards = self.remaining_cards[0 : self.hand_size - len(hand)]
        hand += extra_cards
        self.remaining_cards = self.remaining_cards[len(extra_cards) :]

        for i in range(len(hand)):
            hand[i].set_pos(x=110 * i + 80, y=620)

        return hand

    def play_card(self, card: Card):
        self.discarted_cards.append(card)

    def discard_hand(self, hand: list[Card]):
        self.discarted_cards += hand
