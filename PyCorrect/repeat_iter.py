# Infinite Iterators
from itertools import repeat

def repeat_example (element, max_repeats):
    repeater = repeat (element, max_repeats)
    
    for val in repeater:
        print (val)


repeat_example("hello", 10)
