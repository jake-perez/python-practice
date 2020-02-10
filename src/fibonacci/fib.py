
def fib_slow(n):
    if n < 0:
        raise ValueError('n must be non-negative')
    if n == 1 or n == 0:
        return 1
    return fib_slow(n-1) + fib_slow(n-2)
