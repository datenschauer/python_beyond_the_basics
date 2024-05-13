import random

import pygame
from pygame.locals import *
import sys
from pathlib import Path

# define constants
BASE_PATH = Path(__file__).resolve().parent
BLACK = (0, 0, 0)
WINDOW_WIDTH = 1024 * 2
WINDOW_HEIGHT = int(768 * 1.3)
FRAMES_PER_SECOND = 60
N_PIXELS_TO_MOVE = 10

# initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets:
pathToImages = BASE_PATH / 'images'
pathToSounds = BASE_PATH / 'sounds'
ballImage = pygame.image.load(pathToImages / 'ball.png')
bounceSound = pygame.mixer.Sound(pathToSounds / 'boing.wav')

# Initialize Variables:
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_TO_MOVE
ySpeed = N_PIXELS_TO_MOVE

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
    if (ballRect.left <= 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed
        bounceSound.play()

    if (ballRect.top <= 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed
        bounceSound.play()

    ballRect.left += xSpeed
    ballRect.top += ySpeed

    # clear the window
    window.fill(BLACK)

    # draw all window elements
    window.blit(ballImage, ballRect)

    # update the window
    pygame.display.update()

    # slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
