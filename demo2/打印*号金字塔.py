# -*- coding=utf-8 -*-
num = int(input('请输入金字塔的高度'))
i = 1

# 金字塔行数
while i <= num:

    j = 1
    while j <= i:
        print("*",end=" ")
        j+=1

    print('')
    i+= 1
