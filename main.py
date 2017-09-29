import pygame
from avoidergame import *

pygame.init()

# Display settings
display_width = 800
display_height = 600
game_display = pygame.display.set_mode( (display_width, display_height) )
pygame.display.set_caption('Avoider Game')

# Set the game clock
clock = pygame.time.Clock()

playscreen = AvoiderGame(game_display, clock, display_width, display_height)

while not playscreen.game_over:
    playscreen.on_tick()
    clock.tick(40)

pygame.quit()
quit()
