import pygame
import random
import math
from mobs import *

pygame.init()

# Display settings
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode( (display_width, display_height) )
pygame.display.set_caption('Avoider Game')

black = (0,0,0)
white = (255,255,255)

# Set the game clock
clock = pygame.time.Clock()
game_over = False

# Set mob speeds
avatar_speed = 5
enemy_speed = 2

# Create the avatar, along with a list to store enemies
avatar = Avatar(display_width * 0.5, display_height * 0.8, avatar_speed, "player1.gif")
army = []

# Updates graphics of all mobs, along with despawning enemies
def update_mobs():
    gameDisplay.blit( avatar.sprite, avatar.get_coordinates() )

    for enemy in army:
        enemy.move_a_bit(0,1)
        gameDisplay.blit( enemy.sprite, enemy.get_coordinates() )
        if enemy.y > display_height:
            army.remove(enemy)
            #game_score += 10

# Spawning new enemies
def spawn_mobs():
    if random.random() < 0.1:
        random_x = random.random() * display_width
        new_enemy = Enemy(random_x, -20, enemy_speed, "enemy1.gif")
        army.append(new_enemy)

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

        # Register key presses and refresh coordinates
        keys_pressed = pygame.key.get_pressed()
        x_change = 0; y_change = 0
        if keys_pressed[pygame.K_UP]:
             y_change = -1
        if keys_pressed[pygame.K_DOWN]:
            y_change = 1
        if keys_pressed[pygame.K_LEFT]:
            x_change = -1
        if keys_pressed[pygame.K_RIGHT]:
            x_change = 1

        # Diagonal movement
        if x_change != 0 and y_change != 0:
            x_change *= 0.7
            y_change *= 0.7

        avatar.move_a_bit(x_change, y_change)

    # Refresh the display, along with updating mobs
    gameDisplay.fill(white)
    spawn_mobs()
    update_mobs()
    pygame.display.update()
    clock.tick(100)

pygame.quit()
quit()
