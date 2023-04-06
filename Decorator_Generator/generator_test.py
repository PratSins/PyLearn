import random

print("Random No. test ---- ",random.randint(1,10))

def rand_num(low, high,n):
    for i in range(n):
        yield random.randint(low, high)

for num in rand_num(1,20,5):
    print (num)
