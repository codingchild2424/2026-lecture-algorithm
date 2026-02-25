"""Randomized Select - find k-th smallest element in O(n) average."""
import random


def partition(arr, left, right, pivot_idx):
    pivot = arr[pivot_idx]
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    store = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[store] = arr[store], arr[i]
            store += 1
    arr[store], arr[right] = arr[right], arr[store]
    return store


def randomized_select(arr, left, right, k):
    """Find the k-th smallest element (0-indexed) in arr[left..right]."""
    if left == right:
        return arr[left]

    pivot_idx = random.randint(left, right)
    pivot_idx = partition(arr, left, right, pivot_idx)

    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return randomized_select(arr, left, pivot_idx - 1, k)
    else:
        return randomized_select(arr, pivot_idx + 1, right, k)


def kth_smallest(arr, k):
    """Find k-th smallest (1-indexed) element."""
    a = arr[:]
    return randomized_select(a, 0, len(a) - 1, k - 1)


if __name__ == "__main__":
    data = [7, 10, 4, 3, 20, 15, 8]
    print(f"Array: {data}")
    print(f"Sorted: {sorted(data)}")
    for k in range(1, len(data) + 1):
        result = kth_smallest(data, k)
        print(f"  {k}-th smallest: {result}")

    # Performance comparison
    import time
    n = 1000000
    big_data = [random.randint(1, 10**9) for _ in range(n)]

    start = time.perf_counter()
    result1 = kth_smallest(big_data, n // 2)
    t1 = time.perf_counter() - start

    start = time.perf_counter()
    result2 = sorted(big_data)[n // 2 - 1]
    t2 = time.perf_counter() - start

    print(f"\nN={n:,}, finding median:")
    print(f"  Randomized Select: {t1:.4f}s (result={result1})")
    print(f"  Sort + index:      {t2:.4f}s (result={result2})")
