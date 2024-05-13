import random

import pygame
from pygame.locals import *
import sys
from pathlib import Path
from SimpleButton import *
from colors import *
from settings import *

# initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load assets:

# Initialize Variables:
buttonA = SimpleButton(window, (25, 130),
                       BASE_PATH / 'images' / 'buttonAUp.png',
                       BASE_PATH / 'images' / 'buttonADown.png')

buttonB = SimpleButton(window, (175, 130),
                       BASE_PATH / 'images' / 'buttonBUp.png',
                       BASE_PATH / 'images' / 'buttonBDown.png')

buttonC = SimpleButton(window, (325, 130),
                       BASE_PATH / 'images' / 'buttonCUp.png',
                       BASE_PATH / 'images' / 'buttonCDown.png')

# run main loop:
while True:

    # check for events:
    for event in pygame.event.get():
        print(str(event))
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if buttonA.handle_event(event):
            print('User has clicked the button A!')
        elif buttonB.handle_event(event):
            print('User has clicked the button B!')
        elif buttonC.handle_event(event):
            print('User has clicked the button C!')

    # do "per frame actions"

    # clear the window
    window.fill(GRAY)

    # draw all window elements
    buttonA.draw()
    buttonB.draw()
    buttonC.draw()

    # update the window
    pygame.display.update()

    # slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
