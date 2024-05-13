import pygame
from pygame.locals import *
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
IMAGES = BASE_PATH / 'images'
SOUNDS = BASE_PATH / 'sounds'

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

FRAMES_PER_SECOND = 60
