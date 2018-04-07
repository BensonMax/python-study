#-*- coding:utf-8 -*-
import pygame


class HeroPlane(object):
    direction = 'right'

    def __init__ (self, screen_temp, x, y):
        self.screen = screen_temp
        self.x = x
        self.y = y
        self.img_load()

    def img_load (self):
        self.image = pygame.image.load("./resource/enemy-1.gif")

    def display (self):
        self.screen.blit(self.image, (self.x, self.y))

    def move (self):
        if self.direction == 'right':
            self.x += 5
        elif self.direction == 'left':
            self.x -= 5

        if self.x > 480 - 50:
            self.direction = 'left'
        elif self.x <= 0:
            self.direction = 'right'
