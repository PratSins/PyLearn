def myfunc(*args, **kwargs) :
    print(args)
    print (kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']) )

myfunc(10, 20, 30, fruit='orange', food='eggs', animal='dog')

# myfunc(10, 20, 30, fruit='orange', food='eggs', animal='dog', 100) ---> Error cuz of 100 is after the dictionary