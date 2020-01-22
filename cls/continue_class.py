class my_class:
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        return '{}'.format((self.args))


print(my_class())
