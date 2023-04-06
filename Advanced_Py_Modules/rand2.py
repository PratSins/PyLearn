import random

mylist = list(range(0,20))
print("mylist - ",mylist)

print("\nRandom.choice(mylist) -")
print(random.choice(mylist))
print(random.choice(mylist))
print()

# Sample with Replacement
mylist2 = random.choices(population= mylist, k = 10)
print("mylist - random.choices() - ",mylist2)
print()

# Sample without Replacement
mylist3 = random.sample(population= mylist, k = 10)
print("mylist - random.sample() - ",mylist3)
print()

print("mylist before shuffle - ",mylist)
random.shuffle(mylist)
print("mylist after shuffle - ",mylist)


print("\n random.uniform -")
k2 = random.uniform(a=0,b=100)
print(k2)

print("\n random.gauss -")
k3 = random.gauss(mu=0,sigma=1)
print(k3)