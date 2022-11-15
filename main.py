import pygame
from settings import *
from tiles import Tile
from level import Level
import sys
from pygame.locals import *
from screeninfo import get_monitors
import constants


if __name__ == "__main__":
    pygame.init()

    # screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    screen = pygame.display.set_mode((get_monitors()[0].width, get_monitors()[0].height), FULLSCREEN)
    clock = pygame.time.Clock()
    level = Level(map, screen)

    bg = pygame.image.load('assets/City Background/Sky.png')
    bg = pygame.transform.scale(bg, (get_monitors()[0].width * 1.5, get_monitors()[0].height * 1.5))
    bg1 = pygame.image.load('assets/City Background/City Background.png')
    bg1 = pygame.transform.scale(bg1, (get_monitors()[0].width * 1.5, get_monitors()[0].height * 1.5))
    bg2 = pygame.image.load('assets/City Background/City Foreground.png')
    bg2 = pygame.transform.scale(bg2, (get_monitors()[0].width * 1.5, get_monitors()[0].height * 1.5))

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():

            # x button
            if event.type == pygame.QUIT:
                running = False

            # full-screen toggle
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_F11:
            #         if screen.get_flags() & FULLSCREEN:
            #             pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
            #         else:
            #             pygame.display.set_mode((get_monitors()[0].width, get_monitors()[0].height), FULLSCREEN)

        screen.blit(bg, (0, 0))
        screen.blit(bg1, (0, 0))
        screen.blit(bg2, (0, 0))
        level.run()
        pygame.display.update()
        clock.tick(60)

