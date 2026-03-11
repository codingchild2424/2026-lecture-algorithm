# === A-2: Finding the k-th Smallest Element (Randomized Select) ===
# An algorithm that finds the k-th smallest element in average O(n) time without sorting
# Selection algorithm using quicksort's partition (Quickselect)
"""Randomized Select - find k-th smallest element in O(n) average."""
import random


def partition(arr, left, right, pivot_idx):
    """
    Lomuto partition scheme
    - Partitions the array into two parts based on the pivot
    - Elements smaller than the pivot go left, larger ones go right
    - Time complexity: O(n) -- compares each element in the range once
    - Returns: the final position (index) of the pivot
    """
    # TODO: implement Lomuto partition
    # 1. Save arr[pivot_idx] as the pivot value
    # 2. Swap pivot to the end (arr[right])
    # 3. Use a store pointer starting at left
    # 4. Iterate i from left to right-1:
    #    - if arr[i] < pivot, swap arr[i] with arr[store] and increment store
    # 5. Swap pivot (at right) back to arr[store]
    # 6. Return store
    pass


def randomized_select(arr, left, right, k):
    """
    Randomized Select (Quickselect)
    - Finds the k-th (0-indexed) smallest element in arr[left..right]
    - Algorithm: Partition with a random pivot, then recurse only on the side containing k
    - Time complexity: O(n) average, O(n^2) worst case
    - Space complexity: O(log n) average (recursion stack), O(n) worst case
    - Key insight: Unlike quicksort, only one side is recursed, yielding average O(n)
    """
    # TODO: implement randomized select
    # 1. Base case: if left == right, return arr[left]
    # 2. Choose a random pivot_idx in [left, right]
    # 3. Partition around the pivot
    # 4. If k == pivot position, return arr[k]
    # 5. If k < pivot position, recurse on the left half
    # 6. If k > pivot position, recurse on the right half
    pass


def kth_smallest(arr, k):
    """
    Find the k-th smallest element (1-indexed interface)
    - Uses a copy to avoid modifying the original array
    - Internally calls 0-indexed randomized_select
    """
    a = arr[:]  # Copy to preserve original
    return randomized_select(a, 0, len(a) - 1, k - 1)


if __name__ == "__main__":
    data = [7, 10, 4, 3, 20, 15, 8]
    print(f"Array: {data}")
    print(f"Sorted: {sorted(data)}")
    for k in range(1, len(data) + 1):
        result = kth_smallest(data, k)
        print(f"  {k}-th smallest: {result}")

    # Performance comparison: Quickselect O(n) vs sort-then-index O(n log n)
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
