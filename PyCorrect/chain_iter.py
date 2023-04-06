from itertools import chain

def chain_example(elements1, elements2):
    chained = chain (elements1, elements2)
    print(list(chained))
    
chain_example ("ABC", "DEF")


def chain_from_iterable_example(iterable):
    chained= chain. from_iterable (iterable)
    print (list (chained))

chain_from_iterable_example([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
