# -*- coding:utf-8 -*-
from Base import Base


class BaseBullet(Base):
    def __init__(self, screen_temp, x, y, image_path):
        Base.__init__(self, screen_temp, x, y, image_path)

    # 子弹背景
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
