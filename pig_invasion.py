import pygame

from settings import Settings
from pig import Pig
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    # Creates a windows 1200 pixels wide by 800 pixels high
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Pig Invasion")

    # Make a pig.
    pig = Pig(ai_settings, screen)

    # Start the main loop for the game
    while True:
        gf.check_events(pig)
        pig.update()
        gf.update_screen(ai_settings, screen, pig)

run_game()
