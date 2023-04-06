from itertools import count


def count_example(start, step):
    counter = count (start, step)
    for c in counter:
        print(c)
        if c == 100:
            break


count_example(10, 5)
