import pygame

# Parent class for all mobs
class Mobile:
    def __init__(self, start_x, start_y, speed, sprite):
        # Setting initial conditions
        self.x = start_x
        self.y = start_y

        self.speed = speed

        # Handling sprites
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()
        self.width, self.height = self.sprite.get_size()

    # Updating mob coordinates
    def move_a_bit(self, x_change, y_change):
        self.x += x_change * self.speed
        self.y += y_change * self.speed

    # Getting coordinates as a tuple
    def get_coordinates(self):
        return (self.x, self.y)

# Subclass for the avatar
class Avatar(Mobile):
    pass

# Subclass for enemies
class Enemy(Mobile):
    pass
