import pygame
from pygame.locals import *
import sys
from pathlib import Path

# define constants
BASE_PATH = Path(__file__).resolve().parent
BLACK = (0, 0, 0)
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = 
FRAMES_PER_SECOND = 30

# initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets:
pathToBall = BASE_PATH / 'images/ball.png'

# Initialize Variables:
ballImage = pygame.image.load(pathToBall)

# run main loop:
while True:

    # check for events:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # do "per frame actions"
    # ------

    # clear the window
    window.fill(BLACK)

    # draw all window elements
    window.blit(ballImage, (100, 200))

    # update the window
    pygame.display.update()

    # slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
