a = 8

# 1. if-elif-else ladder in Python
if(a<3): 
    print("The value of a is greater than 3")
elif(a>13):
    print("The value of a is greater than 13")
elif(a>7):
    print("The value of a is greater than 7")
elif(a>17):
    print("The value of a is greater than 17")
else:
    print("The value is not greater than 3 or 7")

# 2. Multiple if statements
if(a<3): 
    print("The value of a is greater than 3")

if(a>13):
    print("The value of a is greater than 13")
    
if(a>7):
    print("The value of a is greater than 7")

if(a>17):
    print("The value of a is greater than 17")
else:
    print("The value is not greater than 3 or 7")
    

print()
age = int(input("Enter your age: "))

if age>18:
    print("Yes")
else:
    print("No")

print()

age = int(input("Enter your age: "))
if(age>34 or age<56):
    print("You can work with us")
else:
    print("You cannot work with us")
print("Done")