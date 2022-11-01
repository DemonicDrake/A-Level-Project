import pygame
import sys
from pygame.locals import *
from screeninfo import get_monitors
import constants

bg = pygame.image.load('assets/City Background/Sky.png')

class FpsClock:
    def __init__(self):
        self.frame_duration = 0
        self.this_frame_time = 0
        self.last_frame_time = 0
        return

    def tick(self):
        self.this_frame_time = self.get_current_time()
        self.frame_duration = (self.this_frame_time - self.last_frame_time) / 1000
        self.last_frame_time = self.this_frame_time
        return

    def get_frame_duration(self):
        return self.frame_duration

    def get_current_time(self):
        return pygame.time.get_ticks()

    def begin(self):
        self.last_frame_time = self.get_current_time()
        return


if __name__ == "__main__":
    pygame.init()

    timer = FpsClock()

    timer.begin()

    # screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    screen = pygame.display.set_mode((get_monitors()[0].width, get_monitors()[0].height), FULLSCREEN)

    running = True
    while running:
        timer.tick()

        screen.fill((0, 0, 0))

        for event in pygame.event.get():

            # x button
            if event.type == pygame.QUIT:
                running = False

            # full-screen toggle
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    if screen.get_flags() & FULLSCREEN:
                        pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
                    else:
                        pygame.display.set_mode((get_monitors()[0].width, get_monitors()[0].height), FULLSCREEN)

        # movement check
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            constants.x -= constants.VELOCITY * timer.get_frame_duration()
        if keys[pygame.K_RIGHT]:
            constants.x += constants.VELOCITY * timer.get_frame_duration()
        # if keys[pygame.K_UP]:
        #    constants.y -= constants.VELOCITY * timer.get_frame_duration()
        # if keys[pygame.K_DOWN]:
        #    constants.y += constants.VELOCITY * timer.get_frame_duration()
        # if keys[pygame.K_c]:
        # character jumps



        # screen edge collision check
        if screen.get_flags() & FULLSCREEN:
            if constants.x < 0:
                constants.x = 0
            if constants.x + constants.WIDTH > get_monitors()[0].width:
                constants.x = get_monitors()[0].width - constants.WIDTH
            if constants.y < 0:
                constants.y = 0
            if constants.y + constants.HEIGHT > get_monitors()[0].height:
                constants.y = get_monitors()[0].height - constants.HEIGHT
        else:
            if constants.x < 0:
                constants.x = 0
            if constants.x + constants.WIDTH > constants.SCREEN_WIDTH:
                constants.x = constants.SCREEN_WIDTH - constants.WIDTH
            if constants.y < 0:
                constants.y = 0
            if constants.y + constants.HEIGHT > constants.SCREEN_HEIGHT:
                constants.y = constants.SCREEN_HEIGHT - constants.HEIGHT

        screen.blit(bg, (0, 0))
        pygame.draw.rect(screen, (255, 255, 255), (constants.x, constants.y, constants.WIDTH, constants.HEIGHT))
        pygame.display.update()
