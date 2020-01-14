class my_class:
    def __init__(self, *args):
        self.args = args

    def __add__(self, other):
        a = self.args + self.other
        return a

    def __str__(self):
        return '{0} + {1} = {2}'.format()


Value1 = mycls("Red", "Green", "Blue")
Value2 = mycls("Yellow", "Purple", "Cyan")
Value3 = Value1 + Value2
print("{0} + {1} = {2}".format(Value1, Value2, Value3))
