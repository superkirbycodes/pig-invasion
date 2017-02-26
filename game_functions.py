import sys
import pygame

def check_keydown_events(event, pig):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        pig.moving_right = True
    elif event.key == pygame.K_LEFT:
        pig.moving_left = True

def check_keyup_events(event, pig):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        pig.moving_right = False
    if event.key == pygame.K_LEFT:
        pig.moving_left = False

def check_events(pig):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, pig)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, pig)

def update_screen(ai_settings, screen, pig):
    """Update Images"""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    pig.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
