
def fib_slow(n):
    if n < 0:
        raise ValueError('n must be non-negative')
    if n == 1 or n == 0:
        return 1
    return fib_slow(n-1) + fib_slow(n-2)


def fib_fast(n):
    cache = {0: 1, 1: 1, 2: 2}

    def inner_fib(m):
        if (m in cache):
            return cache[m]
        value = inner_fib(m-1) + inner_fib(m-2)
        cache[m] = value
        return value

    return inner_fib(n)
