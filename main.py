import pygame
import sys
from settings import *
from level import Level

from pygame.locals import *
from screeninfo import get_monitors

pygame.init()

screen = pygame.display.set_mode((get_monitors()[0].width, get_monitors()[0].height), FULLSCREEN)
clock = pygame.time.Clock()
level = Level(map, screen)

bg = pygame.image.load('assets/City Background/Sky.png').convert()
bg = pygame.transform.scale(bg, (get_monitors()[0].width * 1.5, get_monitors()[0].height * 1.5))
bg1 = pygame.image.load('assets/City Background/City Background.png').convert_alpha()
bg1 = pygame.transform.scale(bg1, (get_monitors()[0].width * 1.5, get_monitors()[0].height * 1.5))
bg2 = pygame.image.load('assets/City Background/City Foreground.png').convert_alpha()
bg2 = pygame.transform.scale(bg2, (get_monitors()[0].width * 1.5, get_monitors()[0].height * 1.5))

while True:
    for event in pygame.event.get():
        # x button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    screen.blit(bg, (0, 0))
    screen.blit(bg1, (0, 0))
    screen.blit(bg2, (0, 0))
    level.run()
    pygame.display.update()
    clock.tick(60)

