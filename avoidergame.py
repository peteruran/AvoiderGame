import pygame
import random
import math
from mobs import *
from gamescore import *

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

# Ads key repetition, for smooth movement
pygame.key.set_repeat(60,20)

# Create the avatar, along with a list to store enemies
avatar = Avatar(display_width * 0.5, display_height * 0.8, avatar_speed, "player1.gif")
army = []

# Creates a score board
game_score = GameScore(text_size=40, text_color=black, x=15, y=15)

# Updates graphics of all mobs, along with despawning enemies and checking for collisions
def update_mobs():
    gameDisplay.blit( avatar.sprite, avatar.get_coordinates() )

    for enemy in army:
        enemy.move_a_bit(0,1)
        gameDisplay.blit( enemy.sprite, enemy.get_coordinates() )
        if enemy.y > display_height:
            army.remove(enemy)
            game_score.add_to_value(10)

        # Checking for collisions with the avatar
        if enemy.rect.colliderect(avatar.rect):
            game_over = True
            print("collision")

# Spawning new enemies and adds them to the list
def spawn_mobs():
    if random.random() < 0.1:
        random_x = random.random() * display_width
        new_enemy = Enemy(random_x, -20, enemy_speed, "enemy1.gif")
        army.append(new_enemy)

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

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
    gameDisplay.blit( game_score.get_string(), game_score.get_position() )
    pygame.display.update()
    clock.tick(70)

pygame.quit()
quit()
