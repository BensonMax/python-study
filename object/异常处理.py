
try:
    open('xxx.txt')
    print (num)
except FileNotFoundError:
    print('出现异常后的处理逻辑.')