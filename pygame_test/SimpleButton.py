import pygame
from pygame.locals import *

class SimpleButton:
    STATE_IDLE = 'idle'
    STATE_ARMED = 'armed'
    STATE_DISARMED = 'disarmed'

    def __init__(self, window, loc, up, down):
        self.window = window
        self.loc = loc
        self.surface_up = pygame.image.load(up)
        self.surface_down = pygame.image.load(down)

        self.rect = self.surface_up.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        self.state = SimpleButton.STATE_IDLE

    def handle_event(self, event):

        if event.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return False

        event_point_in_button_rect = self.rect.collidepoint(event.pos)

        # press mouse down on button
        if self.state == SimpleButton.STATE_IDLE:
            if event.type == MOUSEBUTTONDOWN and event_point_in_button_rect:
                self.state = SimpleButton.STATE_ARMED

        # release mouse on button
        elif self.state == SimpleButton.STATE_ARMED:
            if event.type == MOUSEBUTTONUP and event_point_in_button_rect:
                self.state = SimpleButton.STATE_IDLE
                return True  # CLICKED ON BUTTON!

            # move away with pressed mouse from button
            if event.type == MOUSEMOTION and not event_point_in_button_rect:
                self.state = SimpleButton.STATE_DISARMED

        # if mouse is outside the button
        elif self.state == SimpleButton.STATE_DISARMED:
            # move back into button rectangle
            if event_point_in_button_rect:
                self.state = SimpleButton.STATE_ARMED
            elif event.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE

        return False

    def draw(self):
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surface_down, self.loc)
        else:
            self.window.blit(self.surface_up, self.loc)
            