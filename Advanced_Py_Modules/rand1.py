import random

k = random. randint(0,100)
print(k)

print()

random. seed(42)
# the sequence of random no.s generated will be the same, no matter how many time u execute the code

k1 = random.randint (2,100)
print(k1)   # 83
k1 = random.randint (2,100)
print(k1)   # 16
k1 = random.randint (2,100)
print(k1)   # 5
