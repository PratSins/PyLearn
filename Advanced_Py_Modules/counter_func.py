from collections import Counter

print("\n---Functions in Counter---")

letters = 'abcdddddeeeeff'
c = Counter(letters)
print("letters = ",letters)
print("c = ",c)
print()

print("c.most_common() = ",c.most_common()) # returns the dictionary as list of tuples
print("c.most_common(2) = ",c.most_common(2)) # returns the top 2 most common elements
n = 3
print("c.most_common()[:-n-1:-1] = ",c.most_common()[:-n-1:-1]) # n least common elements

print()

print("c.values() = ",c.values())
print("type(c.values()) = ",type(c.values()))
print("sum(c.values()) = ",sum(c.values()))
print()

print("list(c) = ",list(c)) # gives unique elements as a list
print("set(c) = ",set(c))
print("dict(c) = ",dict(c))
print("c.items() = ", c.items())
print("type(c.items()) = ", type(c.items()))
print()

print("c.clear() -->")
c.clear()
print("c = ",c)