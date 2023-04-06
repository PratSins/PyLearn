# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

def sumNat(n):
    if(n==1):
        return n
    elif(n<1):
        return -99
    return n + sumNat(n-1)


n = sumNat(10)
print(n)