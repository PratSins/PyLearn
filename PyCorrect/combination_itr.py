from itertools import combinations

def combinations_example(iterable, size):
    result = combinations (iterable, size)
    print(list(result))

combinations_example("ABCD", 4)
combinations_example("ABCD", 2)