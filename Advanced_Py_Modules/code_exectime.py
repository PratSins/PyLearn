def f1(n):
    return [str(num) for num in range(n)]

def f2(n):
    return list(map(str, range(n)))

import time

def f3_time(func):
    start_time = time.time()
    r1 = func(1000_000)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Time to execute ",func," function is ---", elapsed_time," seconds")

print()
f3_time(f1)
print()
f3_time(f2)
print()