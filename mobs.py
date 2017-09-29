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
        self.sprites = [pygame.image.load("sprites/" + img) for img in sprites]
        self.sprite_index = 0
        self.next_sprite()
        self.sprite_facing_right = True
        self.mob_facing_right = True

        # Keeping track of time for sprite update
        self.sprite_timer = 0

    def flip_sprite(self):
        if self.x_direction == 1:
            self.mob_facing_right = True
        elif self.x_direction == -1:
            self.mob_facing_right = False

        if not (self.sprite_facing_right == self.mob_facing_right):
            self.sprite_facing_right = not self.sprite_facing_right
            self.sprite = pygame.transform.flip(self.sprite, True, False)

        # Increment lifetime on each time
        self.sprite_timer += 1
        if self.sprite_timer > 100:
            self.next_sprite()
            self.sprite_timer = 0

    def move_a_bit(self):
        self.flip_sprite()
        # Diagonal movement
        if abs(self.x_direction) == 1 and abs(self.y_direction) == 1:
            self.x_direction *= 0.7
            self.y_direction *= 0.7

        # Updating mob coordinates
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
        self.sprite = self.sprites[self.sprite_index]
        self.rect = self.sprite.get_rect()
        self.width, self.height = self.sprite.get_size()
        self.sprite_index = ( self.sprite_index + 1 ) % len(self.sprites)
        self.sprite_facing_right = True


# Subclass for the avatar
class Avatar(Mobile):
    pass

# Subclass for enemies
class Enemy(Mobile):
    pass
