s = "HELLO"

for i in s:
    print(i)

# next(s) --> will give error as str is not iterator
print('---Using iter kw')
s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
