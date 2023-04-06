from collections import namedtuple

print("\nnamedtuple from collections\n")

Dog = namedtuple( 'Dog', ['age','breed','name'] )
sammy = Dog(age=5,breed='Husky' ,name='Sam')
print("sammy = ",sammy)
print("type(sammy) = ",type(sammy))
print("sammy.name = ",sammy.name)
print("sammy.breed = ",sammy.breed)
print("sammy.age = ",sammy.age)
print("sammy[1] = ",sammy[1])

# print("sammy['name'] = ",sammy['name'])   --> can't do this - error

print()