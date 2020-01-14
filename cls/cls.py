class myclass:
    greeting = ''

    def __init__(self, name='there'):
        self.greeting = name + '!'

    def say_hello(self):
        print('hello {first}'.format(first=self.greeting))


a = myclass()
print(a.say_hello())
b = myclass('amy')
print(b.say_hello())
