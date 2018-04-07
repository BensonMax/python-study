# -*- coding:utf-8 -*-

list = [11,33,44,55,66,77,88]

# 使用for 删除某个元素

# 定义一个空列表
remove_list = []

for i in list:
    if i == 33 or i == 44 or i == 55 or i == 66:
        remove_list.append(i)  # 把需要删除的值保存到空列表

for i in remove_list:
    list.remove(i)

print(list)