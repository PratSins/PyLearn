from itertools import compress

def compress_example(data, selectors):
     compressed = compress (data, selectors)
     print(list(compressed))

compress_example ([["a", "b", "c"], [1, 2, 3], [True, False, True]], [True, False, False])
