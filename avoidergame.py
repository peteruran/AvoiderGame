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

        # Set the game clock

        self.game_over = False

        # Set mob speeds
        self.avatar_speed = 5
        self.enemy_speed = 2

        # Handing lists of sprite graphics
        self.avatar_sprites = ['player1.gif', 'player2.gif']
        self.enemy_sprites = ['enemy1.gif', 'enemy.gif']

        # Ads key repetition, for smooth movement
        pygame.key.set_repeat(60,20)

        # Create the avatar, along with a list to store enemies
        self.avatar = Avatar(self.display_width * 0.5, self.display_height * 0.8, self.avatar_speed, self.avatar_sprites)
        self.army = []

        # Creates a score board
        self.game_score = GameScore(text_size=40, text_color=self.black, x=15, y=15)

    # Updates graphics of all mobs, along with despawning enemies and checking for collisions
    def update_mobs(self):
        self.game_display.blit( self.avatar.sprite, self.avatar.get_coordinates() )
        if pygame.time.get_ticks() % 1000 == 0:
            print("update")
            self.avatar.next_sprite()

        # Enemy movement, collision, sprite update and despawning
        for enemy in self.army:
            enemy.move_a_bit(0,1)
            self.game_display.blit( enemy.sprite, enemy.get_coordinates() )
            if pygame.time.get_ticks() % 1000 == 0:
                self.avatar.next_sprite()
            if enemy.y > self.display_height:
                self.army.remove(enemy)
                self.game_score.add_to_value(10)

            # Checking for collisions with the avatar
            if enemy.is_colliding(self.avatar):
                self.game_over = True

    # Spawning new enemies and adds them to the list
    def spawn_mobs(self):
        if random.random() < 0.1:
            random_x = random.random() * self.display_width
            new_enemy = Enemy(random_x, -20, self.enemy_speed, self.enemy_sprites)
            self.army.append(new_enemy)

    # Main game loop
    def on_tick(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True

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

                self.avatar.move_a_bit(x_change, y_change)

            # Refresh the display, along with updating mobs
            self.game_display.fill(self.white)
            self.spawn_mobs()
            self.update_mobs()
            self.game_display.blit( self.game_score.get_string(), self.game_score.get_position() )
            pygame.display.update()
