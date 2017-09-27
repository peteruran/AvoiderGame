import pygame

class GameScore:
    def __init__(self, text_size, text_color, x, y):
        # Variable to hold game score
        self.score = 0

        # Stores the position of the score board
        (self.x, self.y) = (x, y)

        # Defining font, text size and a message
        self.font = pygame.font.SysFont(None, text_size)
        self.text_color = text_color
        self.text = "Score: "

    # Adds points to the score
    def add_to_value(self, points):
        self.score += points

    # Creates the string which will be displayed on screen
    def get_string(self):
        string = self.text + str(self.score)
        return self.font.render(string, True, self.text_color)

    # Returns the position of the score board
    def get_position(self):
        return (self.x, self.y)
