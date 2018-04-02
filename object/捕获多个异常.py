#coding=utf-8
try:
    print(a)
    open('1111.txt')
    11/0
except(NameError,IndentationError):
    print('异常处理的程序')
except Exception:
    print('其他异常处理的程序')