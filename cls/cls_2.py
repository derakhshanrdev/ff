class my_class:
    def DoOad(self, value_1=12, value_2=54):
        sum = value_1 + value_2
        print('the sum of {0} and {1} is {2}'.format(value_1, value_2, sum))


a = my_class()
print(a.DoOad())
print(a.DoOad(5, 6))
