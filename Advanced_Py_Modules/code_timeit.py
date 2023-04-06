
import timeit

stmt = '''func_one(100)'''
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''

k = timeit.timeit(stmt, setup, number=100000)
print("Time for func2 from timeit() =  ",k)

stmt2 = '''func_two(100)'''
setup2 = '''
def func_two(n):
    return list(map(str, range(n)))
'''

k = timeit.timeit(stmt2, setup2, number=100000)
print("Time for func2 from timeit() =  ",k)