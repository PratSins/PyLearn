x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

print("---------------------------------")

def printer2():
    print(x)

print(x)
print(printer2())

print("-----------------------------------")
# GLOABAL
name = 'THIS IS A GLOBAL STRING'
name2 = 'XYZ'
def greet():
    # ENCLOSING
    name = 'Sammy'

    def hello():
        # LOCAL
        name = 'local'
        print('Hello '+name)
        print(name2)

    hello()
    print(name)
    
greet()
print(name)

print("\n--->Help function to know about Built-in functionS\n")
help(len)