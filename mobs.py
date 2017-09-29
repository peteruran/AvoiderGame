import pygame

# Parent class for all mobs
class Mobile:
    def __init__(self, start_x, start_y, speed, sprites):
        # Setting initial conditions
        self.x = start_x
        self.y = start_y

        # Variables for storing speed and movement directions
        self.speed = speed
        self.x_direction = 0
        self.y_direction = 0

        # Handling sprites
        self.sprites = sprites
        self.current_sprite_name = sprites[0]
        self.next_sprite()

    # Updating mob coordinates
    def move_a_bit(self):
        # Diagonal movement
        if abs(self.x_direction) == 1 and abs(self.y_direction) == 1:
            self.x_direction *= 0.7
            self.y_direction *= 0.7

        self.x += self.x_direction * self.speed
        self.y += self.y_direction * self.speed

    # Getting coordinates as a tuple
    def get_coordinates(self):
        return (self.x, self.y)

    # Checking for collisions with other mobs
    def is_colliding(self, mobile):
        x_collide = False
        y_collide = False
        # Check for collision horizontally
        if self.x < mobile.x < (self.x + self.width) or ( self.x < (mobile.x + mobile.width) < (self.x + self.width) ):
            x_collide = True
        # Check for collision vertically
        if self.y < mobile.y < (self.y + self.height) or ( self.y < (mobile.y + mobile.height) < (self.y + self.height) ):
            y_collide = True
        return ( x_collide and y_collide )

    # Load next sprite and update dimensions
    def next_sprite(self):
        self.current_sprite_name = self.sprites[ self.sprites.index(self.current_sprite_name) + 1 % (len(self.sprites) - 1) ]
        self.sprite = pygame.image.load("./sprites/" + str(self.sprites[0]) )
        self.rect = self.sprite.get_rect()
        self.width, self.height = self.sprite.get_size()

# Subclass for the avatar
class Avatar(Mobile):
    pass

# Subclass for enemies
class Enemy(Mobile):
    pass
