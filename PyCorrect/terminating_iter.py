# Terminating Iterators
from itertools import accumulate

def accumulate_example(elements):
    running_sum = accumulate(elements)
    print( list(running_sum))
    

accumulate_example([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
