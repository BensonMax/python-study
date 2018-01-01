#-*- coding=utf-8 -*-
import os

str_name = input('请你输入要处理的字符串名称:')

folder_name = input('请你输入要处理的目录:')

# 获取某个目录下的所有文件名称
old_file_names = os.listdir(folder_name)

for name in old_file_names:
    print(name.rfind(str_name))
    # if name.find(str_name):


