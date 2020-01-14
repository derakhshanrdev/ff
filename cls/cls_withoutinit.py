class mycls:
    greeting = ''

    def say_hello(self):
        print('hello {first}'.format(first=self.greeting))


mycls.greeting = 'reza'
print((mycls.greeting))
a = mycls()
print(a.say_hello())
