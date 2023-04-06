def hello(name="Jose"):
    print('The hello() function has been executed! ')

    def greet():
        return '\tThis is the greet() func inside hello!'

    def welcome():
        return '\tThis is welcome inside hello'
    
    print (greet())
    print (welcome())
    
    print('THis is the end of the hello function')


hello()
# welcome() ---> error