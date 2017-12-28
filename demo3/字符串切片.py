#-*- coding=utf-8 -*-

name = 'abcdEFGHIJKLMN'

print(name[0:3+1])  #abcd

print(name[0:-2:3])

print(name[-1::-1]) #NMLKJIHGFEdcba

print(name[::-1]) #NMLKJIHGFEdcba

names = ['张高元','21',3522322]

names.append('孙悟空')

print(names[0::2])

del names[1]

print(names)

names[0] = 'apple'

print(names)

print(3522322 in names)