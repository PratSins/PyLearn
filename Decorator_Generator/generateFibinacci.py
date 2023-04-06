def gen_fibon(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a, b = b, a+b

print("gen_fibon(10) -> ",gen_fibon(10))
print("list(gen_fibon(10)) -> ",list(gen_fibon(10)))