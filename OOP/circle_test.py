class Circle():

    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius=1): #constructor

        self.radius = radius
        self.area = radius * radius * Circle.pi # pi can be used as both Circle.pi and self.pi

    # METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2


myc = Circle(30)

print("Radius = ",myc.radius)
# print("Radius = ",Circle.radius)
#    ---->  AttributeError: type object 'Circle' has no attribute 'radius'
print("Pi = ", Circle.pi)
print("Pi = ", myc.pi)
print("Area = ", myc.area)
print("Circumference = ", myc.get_circumference())