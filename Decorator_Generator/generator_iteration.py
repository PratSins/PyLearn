def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print (number, end=" ")
print("\n")

g = simple_gen()
print(g)
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  ---> will give error as elements generated are finished

print()

g = simple_gen     # () are not there so now the next() will behave differently
print(g)
print(next(g()))
print(next(g()))
print(next(g()))
print(next(g())) # didn't give error as it's generating the first no. only
