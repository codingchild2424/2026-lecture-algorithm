"""Homework 2: Sorting Algorithms"""


def heap_sort(arr):
    """
    Heap Sort implementation.
    Return a new sorted list (do not modify the input).

    TODO: Implement heap sort.
    Hint: Build a max-heap, then repeatedly extract the max.
    """
    a = arr[:]
    # TODO
    return a


def counting_sort(arr):
    """
    Counting Sort for non-negative integers.
    Return a new sorted list.

    TODO: Implement counting sort.
    """
    if not arr:
        return []
    # TODO
    return []


def benchmark(sizes=None):
    """
    Compare heap_sort, counting_sort, and sorted() for given sizes.
    Returns: dict of {algorithm_name: {size: time_in_seconds}}

    TODO: Implement.
    """
    if sizes is None:
        sizes = [1000, 10000, 100000]
    results = {}
    # TODO
    return results
