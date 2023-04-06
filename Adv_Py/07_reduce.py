from functools import reduce

sum = lambda a, b: a+b

l = [1, 2, 3, 4]
val = reduce(sum, l)   # can work with 2 arguments ONLY
print(val)