import pygame
import random
import math
from mobs import *

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode( (display_width, display_height) )
pygame.display.set_caption('Avoider Game')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
game_over = False
game_score = 0

avatar_speed = 5
enemy_speed = 2

avatar = Avatar((display_width - avatar.width) * 0.5,display_height * 0.8, avatar_speed, "player1.gif")
army = []

def update_mobs():
    gameDisplay.blit( avatar.sprite, avatar.get_coordinates() )

    for enemy in army:
        enemy.move_a_bit(0,1)
        gameDisplay.blit( enemy.sprite, enemy.get_coordinates() )
        if enemy.y > display_height:
            army.remove(enemy)
            game_score += 10

def spawn_mobs():
    if random.random() < 0.1:
        random_x = random.random() * display_width
        new_enemy = Enemy(random_x, -new_enemy.height, enemy_speed, "enemy1.gif")
        army.append(new_enemy)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

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

        if x_change != 0 and y_change != 0:
            x_change *= 0.7
            y_change *= 0.7

        avatar.move_a_bit(x_change, y_change)


    gameDisplay.fill(white)
    spawn_mobs()
    update_mobs()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
