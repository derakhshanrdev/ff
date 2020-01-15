class age_name:
    def __init__(self, name='anna', age=20):
        self.name = name
        self.age = age

    def getname(self):
        return self.name

    def setname(self, name):
        self.name = name

    def getage(self):
        return self.age

    def __str__(self):
        return '{0} is aged {1}'.format(self.name, self.age)


a = age_name()
print(a)
print(type(age_name))
