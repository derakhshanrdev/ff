class AgeName:
    def __init__(self, name='anna', age=20):
        self.name = name
        self.age = age

    def GetName(self):
        return self.name

    def SetName(self, name):
        self.name = name

    def GetAge(self):
        return self.age

    def SetAge(self, age):
        self.age = age

    def __str__(self):
        return '{0} is aged {1}'.format(self.name, self.age)


#a = age_name()
#print(a)
#print(type(age_name))
#a = AgeName()
#print(a.getname())
#a.SetName('ahmad')
#print(a)
#print(a.GetName())