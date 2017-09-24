import pygame

class Mobile:
    def __init__(self, start_x, start_y, speed, sprite):
        self.x = start_x
        self.y = start_y

        self.speed = 0

        self.sprite = pygame.image.load(sprite)
        self.rect = sprite.get_rect()
        self.width, self.height = rect.get_size()

    def move_a_bit(self, x, y):
        self.x += x * self.speed
        self.y += y * self.speed

    def get_coordinates(self):
        return (self.x,self.y)

class Avatar(Mobile):
    pass

class Enemy(Mobile):
    pass
