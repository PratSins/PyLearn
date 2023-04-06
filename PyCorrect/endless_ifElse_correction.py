def factorial(x):
    f=1
    for i in range(1,x+1):
        f = f*i
    print(f)

def do_one(x):
    factorial(x)
def do_two(x):
    factorial(x)
def do_three(x):
    factorial(x)
def do_default(x):
    factorial(x)

x = 2

# if x == 1:
#     do_one(x)
# elif x == 2:
#     do_two(x)
# elif x == 3:
#     do_three(x)
# else:
#     do_default(x)

actions = {1:do_one, 2:do_two, 3:do_three} 
# action = actions.get(x) # ALSO CORRECT but default case not there
action = actions.get(x, do_default)

action(x)
