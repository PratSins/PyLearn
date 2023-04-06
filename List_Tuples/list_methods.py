l1 = [1, 8, 7, 2, 21, 15]
print(l1)
print()

l1_sorted=l1.sort() # l1 gets sorted but l1_sorted remains empty
print(l1_sorted) # output = None
print()

# l1.sort() # sorts the list
print(l1)
l1.reverse() # reverses the list
print(l1)
l1.append(45) # adds 45 at the end of the list 
print(l1)
l1.insert(2, 544) # inserts 544 at index 2
print(l1)
l1.pop(2) # removes element at index 2
print(l1)
l1.remove(21) # removes 21 from the list
print(l1)
print()

a = [2, 4, 56, 7]
print("a - ",a)
#print(a[0] + a[1] + a[2] + a[3])
print("sum(a) - ",sum(a))