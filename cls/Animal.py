class Animal:
    def __init__(self, name='', type='', age=0):
        self.name, self.type, self.age = name, type, age

    def setname(self, name):
        self.name = name

    def setage(self, age):
        self.age = age

    def settype(self, type):
        self.type = type

    def getname(self):
        return self.name

    def gettype(self):
        return self.type

    def getage(self):
        return self.age

    def __str__(self):
        return '{0} is a {1} aged {2}'.format(self.name, self.type, self.age)


class chicken(Animal):
    def __init__(self, name='', age=0):
        self.name, self.age = name, age

    def settype(self, type):
        return 'sorry {0} will always be a {1}'.format(self.name, self.type)

    def makesound(self):
        return '{0} says cluck cluck'.format(self.name)
