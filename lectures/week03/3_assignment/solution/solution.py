"""Homework 3: Reference Solution — Music Playlist Sorting"""
import time
import random


def selection_sort(arr, key=None):
    """Selection Sort — O(n^2). Returns (sorted list, comparisons, swaps)."""
    a = arr[:]
    n = len(a)
    comparisons = swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            val_j = key(a[j]) if key else a[j]
            val_min = key(a[min_idx]) if key else a[min_idx]
            if val_j < val_min:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return a, comparisons, swaps


def insertion_sort(arr, key=None):
    """Insertion Sort — O(n^2). Returns (sorted list, comparisons, swaps)."""
    a = arr[:]
    n = len(a)
    comparisons = swaps = 0
    for i in range(1, n):
        current = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            val_j = key(a[j]) if key else a[j]
            val_cur = key(current) if key else current
            if val_j > val_cur:
                a[j + 1] = a[j]
                swaps += 1
                j -= 1
            else:
                break
        a[j + 1] = current
    return a, comparisons, swaps


def merge_sort(arr, key=None):
    """Merge Sort — O(n log n). Returns (sorted list, comparisons, swaps)."""
    comparisons = [0]
    swaps = [0]

    def _merge_sort(a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = _merge_sort(a[:mid])
        right = _merge_sort(a[mid:])
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            val_l = key(left[i]) if key else left[i]
            val_r = key(right[j]) if key else right[j]
            if val_l <= val_r:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
            swaps[0] += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    result = _merge_sort(arr[:])
    return result, comparisons[0], swaps[0]


def benchmark(sizes=None):
    if sizes is None:
        sizes = [100, 1000, 5000]
    algorithms = {
        "selection_sort": selection_sort,
        "insertion_sort": insertion_sort,
        "merge_sort": merge_sort,
    }
    results = {name: {} for name in algorithms}
    for n in sizes:
        data = list(range(n))
        random.shuffle(data)
        for name, func in algorithms.items():
            start = time.perf_counter()
            sorted_arr, comps, swps = func(data)
            elapsed = time.perf_counter() - start
            results[name][n] = {
                "time": elapsed,
                "comparisons": comps,
                "swaps": swps,
            }
    return results
