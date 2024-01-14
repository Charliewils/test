def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fac(n-1) * fac(n-2)

def count(f):
    def counted(n):
        counted.number += 1
        return f(n)
    counted.number = 0
    return counted

def fib(n):
    if n == 0 or n== 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def memo(f):
    cashe = {}
    def memoized(n):
        if n not in cashe:
            cashe[n] = f(n)
        return cashe[n]
    return memoized

def is_prime(x):
    if x <= 1:
        return False
    return all(map(lambda y: x % y, range(2, x)))

def sum_prime(a,b):
    return sum(filter(is_prime, range(a, b)))
