import random

import pygame
from pygame.locals import *
import sys
from pathlib import Path
from Ball import *

# define constants
BASE_PATH = Path(__file__).resolve().parent
BLACK = (0, 0, 0)
WINDOW_WIDTH = 1024 * 2
WINDOW_HEIGHT = int(768 * 1.3)
FRAMES_PER_SECOND = 60
N_PIXELS_TO_MOVE = 10
N_BALLS = 10

# initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets:

# Initialize Variables:
balls = []
for n in range(N_BALLS):
    balls.append(Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT))

# run main loop:
while True:

    # check for events:
    for event in pygame.event.get():
        print(str(event))
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            # mouseX, mouseY = event.pos

    # do "per frame actions"
    for ball in balls:
        ball.update()

    # clear the window
    window.fill(BLACK)

    # draw all window elements
    for ball in balls:
        ball.draw()

    # update the window
    pygame.display.update()

    # slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
