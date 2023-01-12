import pygame

from settings import *
from interface import Cursor
from utils import load_animations
from components import Card, Bar, Button, Deck, Text, Character


def prepare_player():
    deck_cards = [Card(color=(90, 30, 180)) for _ in range(15)]
    sprite_sheet_image = pygame.image.load(
        "./assets/character1/NightBorne.png"
    ).convert_alpha()

    metadata = {
        "idle": 9,
        "run": 6,
        "attack": 12,
        "hit": 5,
        "death": 23,
    }

    animation_list = load_animations(sprite_sheet_image, 70, 70, 10, metadata)
    return Character(Deck(deck_cards), animation_list)


def demo_screen():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    cursor = Cursor("./assets/cursor.png")

    # Player
    player_heal = Bar()

    # Draw text to screen
    sm = Text(NORMAL_TEXT, NORMAL_TEXT_SIZE, WHITE)

    # Animations
    sprite_sheet_image2 = pygame.image.load(
        "./assets/character2/npc.png"
    ).convert_alpha()
    metadata2 = {"idle": 4, "attack": 8, "recover": 8, "hit": 3}
    animation_list2 = load_animations(sprite_sheet_image2, 45, 45, 3, metadata2)

    # Player character
    player = prepare_player()

    # Game loop
    running = True
    while running:
        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for card in player.hand:
                        if card.is_selected(x, y):
                            player.active = card
                            break

            elif event.type == pygame.MOUSEBUTTONUP:
                player.active = None

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    print("Has jugado una carta")
                    # player_deck.play_card(player_hand.pop())

                if event.key == pygame.K_f:
                    print("Has pasado tu turno")
                    # player_deck.discard_hand(player_hand)
                    # player_hand = player_deck.draw()

        screen.fill((50, 50, 50))

        player_heal.draw(screen)
        sm.draw(screen, "Dark Night", 10, 10)
        sm.draw(screen, f"Mano: {len(player.hand)}", 10, 50)
        sm.draw(screen, f"Deck: {len(player.deck.remaining_cards)}", 10, 90)
        sm.draw(screen, f"Disc: {len(player.deck.discarted_cards)}", 10, 130)
        sm.draw(screen, f"Selc: {player.active != None}", 10, 170)

        # Drawing animations
        player.update()
        player.draw(screen)
        animation_list2[0].update()
        animation_list2[0].draw(screen, 800, 150)

        clock.tick(144)
        pygame.display.update()
