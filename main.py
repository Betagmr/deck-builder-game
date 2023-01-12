import pygame

from settings import *
from screens.demo import demo_screen
from screens.demo2 import demo_2

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)

    # Run the current demo
    if False:
        demo_2()
    else:
        demo_screen()

    pygame.quit()
