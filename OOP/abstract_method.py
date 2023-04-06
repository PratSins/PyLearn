class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method") 
        # raise -> throw keyword in java

myanimal = Animal('Fred')
# myanimal.speak()
#        ----> will cause error as the function needs to overridden by child classes

class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"

class Cat (Animal):
    def speak(self):
        return self.name + " says meow!"

fido = Dog("Fido")
feli = Cat("feli")

print(fido. speak())
print (feli. speak())