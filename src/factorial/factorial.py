def factorial_recursive(n):
    if n < 0:
        raise ValueError('n must be non-negative')
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)


def factorial_iterative(n):
    product = 1
    for i in range(1, n):
        product *= i
    return product
