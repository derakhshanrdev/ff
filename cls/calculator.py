class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x_new = self.x + other.x
        y_new = self.y + other.y
        return Calculator(x_new, y_new)

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __mul__(self, other):
        x_new = self.x * other.x
        y_new = self.y * other.y
        return Calculator(x_new, y_new)


v1 = Calculator(7, 3)
v2 = Calculator(12, 14)
v3 = v1 + v2
v4 = v1 * v2
print(v3)
print(v4)
