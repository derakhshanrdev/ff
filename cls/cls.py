class myclass:
    greeting = ''

    def __init__(self, name='there'):
        self.greeting = name + '!'

    def say_hello(self):
        print('hello {0}'.format(self.greeting))


a = myclass()
print(a.say_hello())
