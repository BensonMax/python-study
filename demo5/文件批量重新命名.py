#-*- coding=utf-8 -*-
import os

folder_name = input('请输入操作的文件夹名称:')

#获取要操作文件夹下的所有文件
file_names = os.listdir(folder_name)

# #进入操作的文件目录中
# os.chdir(folder_name)

for name in file_names:
    old_file_name = folder_name+"/"+name
    new_file_name = folder_name+"/"+'[python批量更改文件名]-'+name
    os.rename(old_file_name, new_file_name)

