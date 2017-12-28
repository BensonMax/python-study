#-*- coding=utf-8 -*-
b = [100]

def test(num):
    # 如果是不可变类型,函数不会修改原始的值.如果是可变类型.函数默认是引用传递.会修改以前的值
    # num +=num
    num = num+num
    print(num)

test(b)
print(b)