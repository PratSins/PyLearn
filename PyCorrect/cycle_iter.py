from itertools import cycle


def cycle_example(elements):
    i = 0
    cycler = cycle (elements)
    while i < 100:
        print (next (cycler), end=" ")
        i += 1


cycle_example ("ABCDEF")
