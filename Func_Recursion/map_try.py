print("\nMap try 1\n")

def sq(num):
    return num**2

my_nums = [1, 2, 3, 4, 5]

print(" Using map func in for loop")
for i in map(sq, my_nums):
    print(i,end=" ")

print("\n\n Using Map func with the list() func")
my_sq = list(map(sq, my_nums))
print(my_sq)

print("\nMap try 2\n")

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
    
names = ["Prat", "Eve", "Chaitanya", "Alia",]

new_n = list(map(splicer, names))
print(new_n)

print("\nMap try 3\n")

def check_even(num):
    return num % 2 == 0

mynums = [1,2,3,4,5,6]

for n in filter(check_even, mynums):
    print(n,end=" ")

mn = list(filter(check_even, mynums))
print("\n",mn)