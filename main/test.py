#coding: utf-8
import pygame
from pygame.locals import *
import math
import sys

SCREEN_SIZE = (400, 300)
SCREEN_COLOR = (0, 0, 122)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("PyGame")

    while(1):
        screen.fill(SCREEN_COLOR)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    main()
