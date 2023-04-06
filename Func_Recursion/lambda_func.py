n = 3

sq = lambda num: num**2
print(sq(n))

mynums = [1,2,3,4,5,6]
print(mynums)
my_sq = list(map(sq, mynums))
print(my_sq)

print("---------------------------")

my_sq = list(map(lambda num: num**2, mynums))
print(my_sq)

even = list(filter(lambda num: num%2 == 0, mynums))
print(even)

names = ["Prat", "Eve", "Chaitanya", "Alia",]
lttr = list(map(lambda name: name[0], names))
print(lttr)

lttr = list(map(lambda name: name[::-1], names))
print(lttr)