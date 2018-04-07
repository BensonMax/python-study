#-*- coding:utf-8 -*-
import pygame
from Bullet import Bullet

class Plane(object):

    image = None

    bullet_list = []

    def __init__(self, screen_temp, x, y):
        self.screen = screen_temp
        self.x = x
        self.y = y
        self.img_load()

    def img_load(self):
        self.image = pygame.image.load("./resource/hero1.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            # 判断子弹是否越界
            if bullet.judge():
                self.bullet_list.remove(bullet) # 如果子弹越界就删除子弹
            bullet.display()
            bullet.move()

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))