#-*- coding=utf-8 -*-

def test(a,b,function):
    return  function(a,b)


result = test(11,22,lambda a,b:a+b)

print(result)

input = eval(input('请输入匿名函数'))

rsu = test(22,33,input)

print(rsu)
