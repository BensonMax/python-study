age = int(input('你年龄多大?'))

moeny = int(input('你身上有多少钱?'))

if age >= 18 and moeny >= 10:
    print('你已经成年了,可以尽情嗨皮!')
elif  moeny < 10:
    print('你身上已经没钱了.不能上网了')
else:
    print('你不能上网')