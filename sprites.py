import pygame
from settings import *
import random

class Snake(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x, self.y = x, y
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

    def body_collision(self):
        if self.x == self.game.head.x and self.y == self.game.head.y:
            return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class Reward(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x, self.y = x, y
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def reward_collision(self):
        if self.game.head.x == self.x and self.game.head.y == self.y:
            return True
        return False

    def get_new_position(self):
        self.x = random.randint(0, GRIDWIDTH - 1)
        self.y = random.randint(0, GRIDHEIGHT - 1)
        
        for body in self.game.snake_body:
            if body.x == self.x and body.y == self.y:
                self.x, self.y = self.get_new_position()
        return self.x, self.y

    def update(self):
        # self.x = random.randint(0, GRIDWIDTH - 1)
        # self.y = random.randint(0, GRIDHEIGHT - 1)
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE


class UIElement:
    def __init__(self, x, y, text):
        self.x, self.y, self.text = x* TILESIZE, y * TILESIZE, text

    def draw(self, screen, font_size):
        font = pygame.font.SysFont("Arial", font_size)
        # Render the text
        text = font.render(self.text, True, WHITE)
        # Draw the text on the screen
        screen.blit(text, (self.x, self.y))

    def get_text_width(self, font_size):
        font = pygame.font.SysFont("Arial", font_size)
        text = font.render(self.text, True, WHITE)
        return text.get_width()

    def get_text_height(self, font_size):
        font = pygame.font.SysFont("Arial", font_size)
        text = font.render(self.text, True, WHITE)
        return text.get_height()


class Button:
    def __init__(self, game, color, outline, x, y, width, height, text):
        self.game = game 
        self.color, self.outline = color, outline
        self.text = text
        self.x, self.y = x, y 
        self.width, self.height = width, height

    def draw(self, screen, font_size):
        pygame.draw.rect(screen, self.outline, (self.x-2, self.y-2, self.width+4, self.height+4))
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        font = pygame.font.SysFont("Arial", font_size)
        text = font.render(self.text, True, WHITE)

        text_x = self.x + (self.width - text.get_width()) // 2
        text_y = self.y + (self.height - text.get_height()) // 2
        # Draw the text on the screen
        screen.blit(text, (text_x, text_y))

    def is_mouse_over(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height
