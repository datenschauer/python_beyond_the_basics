from settings import *
import pygame
from pygame.locals import *
import random

MIN_SPEED = 3
MAX_SPEED = 10


class Ball:
    def __init__(self, window, window_width, window_height):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.image = pygame.image.load(BASE_PATH / Path('images') / 'ball.png')
        self.ball_rect = self.image.get_rect()
        self.width = self.ball_rect.width
        self.height = self.ball_rect.height
        self.max_width = window_width - self.ball_rect.width
        self.max_height = window_height - self.ball_rect.height

        # starting position
        self.x = random.randrange(self.max_width)
        self.y = random.randrange(self.max_height)
        speeds_list = list(range(-MIN_SPEED, -MAX_SPEED + 1)) + list(range(MIN_SPEED, MAX_SPEED + 1))
        self.x_speed = random.choice(speeds_list)
        self.y_speed = random.choice(speeds_list)

    def update(self):
        if self.x <= 0 or self.x >= self.max_width:
            self.x_speed = -self.x_speed
        if self.y <= 0 or self.y >= self.max_height:
            self.y_speed = -self.y_speed

        self.x += self.x_speed
        self.y += self.y_speed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
