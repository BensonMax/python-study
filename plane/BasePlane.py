# -*- coding:utf-8 -*-
from Base import Base


class BasePlane(Base):
    def __init__(self, screen_temp, x, y, image_path):
        Base.__init__(self, screen_temp, x, y, image_path)

    # 显示飞机
    def display(self, bullet_list):

        self.screen.blit(self.image, (self.x, self.y))  # 显示飞机

        for bullet in bullet_list:  # 循环取出子弹对象
            # 判断子弹是否越界
            if bullet.judge():
                bullet_list.remove(bullet)  # 如果子弹越界就删除子弹

            bullet.display()  # 显示子弹
            bullet.move()  # 子弹移动步长
