class Dog(object):

    __instance = None

    __init_flag = False

    def __init__(self,name):
        if(self.__init_flag == False):
         self.name = name
         self.__init_flag = True

    def __new__(cls,name):

        if(cls.__instance == None):
            cls.__instance = object.__new__(cls)
            return cls.__instance

        else:
            return cls.__instance

dog = Dog('哮天犬')
print(dog.name)
print(id(dog))
dog2 = Dog('小黄')
print(dog2.name)
print(id(dog2))