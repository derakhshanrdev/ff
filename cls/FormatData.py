class FormatData:
    def __init__(self, name='', age=0, married=False):
        self.name, self.age, self.married = name, age, married

    def __str__(self):
        outstring = '{0} is aged {1} {2}'.format(self.name, self.age, self.married)
        return outstring




