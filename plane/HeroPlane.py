# -*- coding:utf-8 -*-
import random
from BasePlane import BasePlane
from EnemyBullet import EnemyBullet


class HeroPlane(BasePlane):
    # 定义一个类属性用来保存
    direction = 'right'

    # 储存子弹对象
    bullet_list = []

    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 0, 0, "./resource/enemy-1.gif")

    # 敌机移动轨迹
    def move(self):
        # 敌机创建的子弹默认向右移动
        if self.direction == 'right':
            self.x += 5  # 每次向右移动增加 5px 的步长
        elif self.direction == 'left':  # 向左移动
            self.x -= 5  # 每次向左移动减少 5px 的步长

        # 当敌机向右移动到了边界就向左移动
        if self.x > 480 - 50:  # 480 是界面总宽度; 50 是飞机宽度. 所以敌机移动的距离应该是界面宽度-敌机宽度  ( 移动距离 = 界面宽度 - 敌机宽度 )
            self.direction = 'left'
        elif self.x <= 0:  # 当敌机移动到了最左边就会继续向右移动
            self.direction = 'right'

    # 开火
    def fire(self):
        random_temp = random.randint(1, 100)  # 随机生成 1 - 100的随机数
        if (random_temp == 20) or (random_temp == 78):  # 随机数概率
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))  # 创建敌机子弹对象
