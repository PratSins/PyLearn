def sq(n):
    return n**2

mn = [1,2,3,4,5,6,]

for i in map(sq, mn):
    print(i,end = " ")


print("\nType return by map() = ",type(map(sq, mn)))

msq = list(map(sq, mn))
print(msq)