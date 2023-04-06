# Combinatoric Iterators
from itertools import product

def product_example(iterable1, iterable2):
    result = product (iterable1, iterable2)
    print(list(result))


product_example ([1, 2, 3], ["a", "b", "c"])
