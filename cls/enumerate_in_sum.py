class CLS:
    def printlist_1(*args):
        for count, item in enumerate(args):
            print('{0} . {1}'.format(count, item))

    def printlist_2(**kwargs):
        for name, vlue in kwargs.items():
            print('{0} likes {1}'.format(name, vlue))


print(CLS.printlist_1(1, '47', 'hj', '444'))
print(CLS.printlist_2(ali='red', mdd='blue'))
