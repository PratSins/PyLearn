my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3) # Generator Comprehension
gencomp1 = [item for item in my_list if item > 3] # List

print("gencomp uses () --->",type(gencomp))
print("gencomp1 uses [] --->",type(gencomp1))

print("\n> Output")
for item in gencomp:
    print(item)
