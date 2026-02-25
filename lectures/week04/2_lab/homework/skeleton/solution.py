"""Homework 3: Karatsuba Multiplication"""


def naive_multiply(x, y):
    """Standard multiplication (baseline)."""
    return x * y


def karatsuba(x, y):
    """
    Karatsuba multiplication algorithm.

    TODO: Implement.
    Base case: if x or y < 10, return x * y
    """
    # TODO
    return 0


def benchmark(sizes=None):
    """
    Compare naive_multiply vs karatsuba for large numbers.
    sizes: list of number of digits.
    Returns: dict of {method: {digits: time}}

    TODO: Implement.
    """
    if sizes is None:
        sizes = [100, 1000, 10000]
    results = {}
    # TODO
    return results
