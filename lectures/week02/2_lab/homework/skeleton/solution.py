"""Homework 1: Complexity Analysis"""
import time


def func_a(n):
    """What is the time complexity?"""
    total = 0
    for i in range(n):
        total += i
    return total


def func_b(n):
    """What is the time complexity?"""
    total = 0
    for i in range(n):
        for j in range(n):
            total += i + j
    return total


def func_c(n):
    """What is the time complexity?"""
    if n <= 1:
        return 1
    return func_c(n // 2) + 1


def func_d(n):
    """What is the time complexity?"""
    total = 0
    i = 1
    while i < n:
        total += i
        i *= 2
    return total


def func_e(n):
    """What is the time complexity?"""
    total = 0
    for i in range(n):
        j = 1
        while j < n:
            total += 1
            j *= 2
    return total


def analyze():
    """
    Return a dictionary mapping function names to their Big-O complexity.
    Example: {"func_a": "O(n)", "func_b": "O(n^2)", ...}

    TODO: Fill in the correct complexities.
    """
    return {
        "func_a": "",  # TODO
        "func_b": "",  # TODO
        "func_c": "",  # TODO
        "func_d": "",  # TODO
        "func_e": "",  # TODO
    }


def benchmark(sizes=None):
    """
    Measure execution time of each function for different input sizes.
    Returns: dict of {func_name: {size: time_in_seconds}}

    TODO: Implement benchmarking.
    """
    if sizes is None:
        sizes = [100, 1000, 10000]

    results = {}
    # TODO: Measure each function for each size
    return results
