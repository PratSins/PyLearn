x = 50

def func(x):
    print(f'X is {x}')

    # LOCAL REASSIGNMENT!
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}')

func(x)
print(x)

print("----------Using global keyword-----------------")
def func():
    global x # has to be the very first line
    print(f'X is {x}')

    # LOCAL REASSIGNMENT!
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}')

func()
print(x)

print("--------------------")
X=50
def func(x):
    print(f'X is {x}')

    # LOCAL REASSIGNMENT
    x = 'NEW ****'
    print(f'I JUST LOCALLY CHANGED X TO {x}')
    return x

x = func(X)
print(x)