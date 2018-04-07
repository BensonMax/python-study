# -*- coding:utf-8 -*-
from Base import Base


class Screen(Base):
    def __init__(self, screen_temp):
        Base.__init__(self, screen_temp, 0, 0, "./resource/background.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
