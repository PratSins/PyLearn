for i in range(10):
    print(i, end="")
else:
    print("\nThis is inside else of for")
print()
   
for i in range(10):
    print(i, end="")
    if(i==5):
        break
else:
    print("\ntHIS is inside for --")
    

print()
print()
print()

k = range(10)
print(type(k))
print(k)

k=list(k)
print(k)