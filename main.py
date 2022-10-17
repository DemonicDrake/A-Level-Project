import pygame
import sys
from pygame.locals import *
from screeninfo import get_monitors
import constants


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

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    square_speed = 160
    # Setup for the interval example

    tick_interval = 1.000
    tick_time = 0

    # Change this to see how different framerates result in consistent
    # motion. Try values like 50 or 200

    delay_duration = 5

    running = True
    while running:
        # Interval example

        tick_time += timer.get_frame_duration()
        if tick_time > tick_interval:
            tick_time = 0
            print
            "Tick"

        # Motion example
        # display.blit(black_square, (square_x, 0))
        # square_x += (square_speed * timer.get_frame_duration())
        # if square_x > 320:
        #     square_x = 0
        # display.blit(red_square, (square_x, 0))

        # Insert artificial delay

        pygame.time.delay(delay_duration)

        # Must call this every frame

        timer.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            keys = pygame.key.get_pressed()

            # full-screen toggle (also dont work)
            if keys[pygame.K_F11]:
                if screen.get_flags() & pygame.FULLSCREEN:
                    pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
                else:
                    pygame.display.set_mode((get_monitors()[0].width, get_monitors()[0].height), pygame.FULLSCREEN)

            # dont work
            if keys[pygame.K_LEFT]:
                constants.VELOCITY -= square_speed * timer.get_frame_duration()
            if keys[pygame.K_RIGHT]:
                constants.VELOCITY += square_speed * timer.get_frame_duration()
            if keys[pygame.K_UP]:
                constants.VELOCITY -= square_speed * timer.get_frame_duration()
            if keys[pygame.K_DOWN]:
                constants.VELOCITY += square_speed * timer.get_frame_duration()

        pygame.draw.rect(screen, (255, 0, 0), (constants.x, constants.y, constants.WIDTH, constants.HEIGHT))

        pygame.display.update()
