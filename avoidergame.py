import pygame
import random
import math
from mobs import *
from gamescore import *

class AvoiderGame:

    def __init__(self, game_display, clock, display_width, display_height):
        self.game_display = game_display
        self.clock = clock
        self.display_width = display_width
        self.display_height = display_height

        # Useful colors
        self.black = (0,0,0)
        self.white = (255,255,255)

        self.game_over = False

        # Set mob speeds
        self.avatar_speed = 2
        self.enemy_speed = 1

        # Handing lists of sprite graphics
        self.avatar_sprites = ['player1.gif', 'player2.gif']
        self.enemy_sprites = ['enemy1.gif', 'enemy2.gif']

        # Set spawn rate per tick
        self.spawn_rate = 0.05

        # Create the avatar, along with a list to store enemies
        self.avatar = Avatar(self.display_width * 0.5, self.display_height * 0.8, self.avatar_speed, self.avatar_sprites)
        self.army = []

        # Creates a score board
        self.game_score = GameScore(text_size=40, text_color=self.black, x=15, y=15)

    # Updates graphics of all mobs, along with despawning enemies and checking for collisions
    def update_mobs(self):
        self.game_display.blit( self.avatar.sprite, self.avatar.get_coordinates() )

        # Enemy movement, collision, sprite update and despawning
        for enemy in self.army:
            enemy.y_direction = 1
            enemy.move_a_bit()
            self.game_display.blit( enemy.sprite, enemy.get_coordinates() )

            # Despawn enemy and increment score
            if enemy.y > self.display_height:
                self.army.remove(enemy)
                self.game_score.add_to_value(10)

            # Checking for collisions with the avatar
            if enemy.is_colliding(self.avatar):
                self.game_over = True

    # Spawning new enemies and adds them to the list
    def spawn_mobs(self):
        if random.random() < self.spawn_rate:
            random_x = random.random() * self.display_width
            new_enemy = Enemy(random_x, -20, self.enemy_speed, self.enemy_sprites)
            self.army.append(new_enemy)

    # Main game loop
    def on_tick(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True

                # Register key presses and control movement direction
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.avatar.x_direction = 0
                    if event.key == pygame.K_RIGHT:
                        self.avatar.x_direction = 0
                    if event.key == pygame.K_UP:
                        self.avatar.y_direction = 0
                    if event.key == pygame.K_DOWN:
                        self.avatar.y_direction = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.avatar.x_direction = -1
                    if event.key == pygame.K_RIGHT:
                        self.avatar.x_direction = 1
                    if event.key == pygame.K_UP:
                        self.avatar.y_direction = -1
                    if event.key == pygame.K_DOWN:
                        self.avatar.y_direction = 1

            self.avatar.move_a_bit()
            
            # Refresh the display, along with updating mobs
            self.game_display.fill(self.white)
            self.spawn_mobs()
            self.update_mobs()
            self.game_display.blit( self.game_score.get_string(), self.game_score.get_position() )
            pygame.display.update()
