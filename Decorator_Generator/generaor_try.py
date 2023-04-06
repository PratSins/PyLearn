print()
# def create_cubes(n):
#     result = []
#     for x in range(n):
#         result.append(x**3)
#     return result

# print(create_cubes(10))

# for x in create_cubes(10):
#     print(x, end=' ')
# print()

'''
Generator test
'''
def create_cubes(n):
    for x in range(n):
        yield x**3
        
print(create_cubes(10))
print("--Above call didn't print a list but returned a generator object")
print("--To get a list u will have to use list()")

print("\nThe following is done using for loop")
for x in create_cubes(10):
    print(x, end=' ')
print("\n")