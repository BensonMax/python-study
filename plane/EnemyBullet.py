# -*- coding:utf-8 -*-
from BaseBullet import BaseBullet


class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x + 30, y + 30, "./resource/bullet-1.gif")

    # 子弹移动步长
    def move(self):
        self.y += 20

    # 判断子弹y轴是否已经越界
    def judge(self):
        if self.y > 890:  # 890 界面总高度
            return True
        else:
            return False
