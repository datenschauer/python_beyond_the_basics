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
BALL_WIDTH_HEIGHT = 256
TARGET_WIDTH_HEIGHT = 128
TARGET_X = int(WINDOW_WIDTH / 2 - TARGET_WIDTH_HEIGHT / 2)
TARGET_Y = int(WINDOW_HEIGHT / 2 - TARGET_WIDTH_HEIGHT / 2)
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
FRAMES_PER_SECOND = 30
N_PIXELS_TO_MOVE = 10

# initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets:
pathToImages = BASE_PATH / 'images'
ballImage = pygame.image.load(pathToImages / 'ball.png')
targetImage = pygame.image.load(pathToImages / 'target.png')

ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

# Initialize Variables:


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
    keyPressedTuple = pygame.key.get_pressed()

    if keyPressedTuple[pygame.K_LEFT]:
        ballX = ballX - N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_RIGHT]:
        ballX = ballX + N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_UP]:
        ballY = ballY - N_PIXELS_TO_MOVE
    if keyPressedTuple[pygame.K_DOWN]:
        ballY = ballY + N_PIXELS_TO_MOVE

    ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    if ballRect.colliderect(targetRect):
        print("Ball is touching the target!")

    # clear the window
    window.fill(BLACK)

    # draw all window elements
    window.blit(targetImage, (TARGET_X, TARGET_Y))
    window.blit(ballImage, (ballX, ballY))

    # update the window
    pygame.display.update()

    # slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
