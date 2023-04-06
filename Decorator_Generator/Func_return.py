def hello(name='Jose'):
    print('\nThe hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!\n'

    def welcome():
        return '\t This is welcome() inside hello\n'

    print("I am going to return a function! !\n")

    if name == 'Jose':
        return greet
    else:
        return welcome 

func = hello()
print(func)
print(func())