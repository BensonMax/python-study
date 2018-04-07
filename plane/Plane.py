# -*- coding:utf-8 -*-
from Bullet import Bullet
from BasePlane import BasePlane


class Plane(BasePlane):

    # 储存子弹对象
    bullet_list = []

    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 210, 700, "./resource/hero1.png")

    # 飞机向左移动偏移量
    def move_left(self):
        self.x -= 10

    # 飞机向右移动偏移量
    def move_right(self):
        self.x += 10

    # 将飞机创建的子弹对象存储进 bullet_list 列表中
    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))
        print(self.bullet_list)
