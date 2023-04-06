from itertools import permutations

def permutations_example(iterable, size):
    result = permutations (iterable, size)
    print(list(result))

permutations_example ("ABCD", 2)
# print("\n")
# permutations_example ("ABCD", 4)
# permutations_example ("ABCD", 5)