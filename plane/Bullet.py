#-*- coding:utf-8 -*-
import pygame


class Bullet(object):
    def __init__ (self, screen_temp, x, y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen_temp
        self.img_load()

    def img_load(self):
        self.image = pygame.image.load("./resource/bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 20

    def judge(self):
        if self.y < 200:
            return True
        else:
            return False
