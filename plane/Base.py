# -*- coding:utf-8 -*-
import pygame


class Base(object):
    # 背景图片
    image = None

    def __init__(self, screen_temp, x, y, image_path):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image_load(image_path)

    # 飞机赋值图片对象
    def image_load(self, image_path):
        self.image = pygame.image.load(image_path)
