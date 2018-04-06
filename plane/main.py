# -*- coding:utf-8 -*-

import time
import pygame

def main():
    screen = pygame.display.set_model((480,852),0,32)
    background = pygame.image.load("./resource/background.png")

    while True:
        screen.blit(background(0,0))
        pygame.display.update()
        time.sleep(0.1)

if __name__ == '__main__':
    main()
