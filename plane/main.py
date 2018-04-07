# -*- coding:utf-8 -*-
import pygame, time
from Plane import Plane
from HeroPlane import HeroPlane
from Screen import Screen
from pygame.locals import *


def key_control(plane_temp):
    # 获取事件，比如按键等
    for event in pygame.event.get():

        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                plane_temp.move_left()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                plane_temp.move_right()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                plane_temp.fire()


def main():

    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 创建窗口对象
    screen_temp = Screen(screen)

    # 创建一个飞机对象
    plane = Plane(screen)

    # 创建敌机对象
    enemyPlane = HeroPlane(screen)

    while True:
        screen_temp.display()  # 显示窗口
        plane.display(plane.bullet_list)  # 显示飞机
        enemyPlane.display(enemyPlane.bullet_list)  # 敌机显示
        enemyPlane.move()  # 敌机移动
        enemyPlane.fire()  # 敌机开火
        key_control(plane)  # 键盘事件监听
        pygame.display.update()  # 更新窗口
        time.sleep(0.01)  # 延时0.01秒,防止程序内存溢出


if __name__ == '__main__':
    main()
