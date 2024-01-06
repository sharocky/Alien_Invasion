import sys
import pygame

from settings import Settings

def run_game():
    #Intialize pygame, settings and screen object.
    pygame.init()
    a1_settings = Settings()
    screen = pygame.display.set_mode(a1_settings.screen_width, a1_settings.screen_height)
    pygame.display.set_caption("Alien Invasion")

    # Start the main loop for the game.
    while True:
        # Wath for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        

        # Set the background color.
        bg_color = (230, 230, 230)

        # Start the main loop for the game.
        while True:
            # Watch for keyboard and mouse events.
    
            # Redraw the screen during each pass through the loop.
            screen.fill(a1_settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

run_game()


