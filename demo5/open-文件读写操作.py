#coding=utf-8

f = open("test.txt", "wb")
f.write( "www.runoob.com!\nVery good site!\n")
f.close()

r = open('test.txt','r')
conent = r.read()
print(conent)
f.close()