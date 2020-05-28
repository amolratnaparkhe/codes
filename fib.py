# Iterative method
def fib(n):
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(1,n):
            a, b = b, a + b
    return b

#print(fib(3))

# Recursive method

def fib_rec(n):
    if n == 0  or n == 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

#print(fib_rec(3))

# Dynamic programming 

dict1 = {0:0,1:1}
def fib_dyn(n):
    if n  in dict1:
        return dict1[n]
    else:
        dict1[n] = fib_dyn(n - 1) + fib_dyn(n - 2)
        return dict1[n]

#print(fib_dyn(3))