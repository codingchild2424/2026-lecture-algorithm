# === A-2: Randomized Select (Quickselect) -- Detailed Implementation ===
# An algorithm that finds the k-th smallest element in average O(n) without sorting
# Includes performance comparison benchmark (Quickselect vs Sort+index)
"""
Randomized Select (Quickselect) -- Finding the k-th Smallest Element
Finds the k-th smallest element in average O(n) without sorting.
"""

import random
import time


def partition(arr, left, right, pivot_idx):
    """
    Partitions the array based on the pivot.
    - Uses Lomuto partition scheme
    - Elements smaller than the pivot move left, larger ones move right.
    - Time complexity: O(right - left) -- iterates through elements in range once
    - Returns: the final position of the pivot
    """
    # TODO: implement Lomuto partition
    # 1. Save arr[pivot_idx] as pivot_val
    # 2. Swap pivot to end: arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    # 3. Initialize store_idx = left
    # 4. For each i in range(left, right):
    #    - if arr[i] < pivot_val, swap arr[i] with arr[store_idx], increment store_idx
    # 5. Swap pivot back: arr[store_idx], arr[right] = arr[right], arr[store_idx]
    # 6. Return store_idx
    pass


def randomized_select(arr, left, right, k):
    """
    Finds the k-th (0-indexed) smallest element in arr[left..right].
    - Algorithm: Random pivot selection -> partition -> recurse on one side based on pivot position
    - Average time complexity: O(n) -- T(n) = T(n/2) + O(n)
    - Worst-case time complexity: O(n^2) -- when the pivot is always the min/max
    - Key idea: Unlike quicksort, only one side is recursed, achieving linear time
    """
    # TODO: implement randomized select
    # 1. Base case: if left == right, return arr[left]
    # 2. Choose random pivot_idx in [left, right] using random.randint
    # 3. Partition and get the pivot's final position
    # 4. If k == pivot_idx, return arr[k]
    # 5. If k < pivot_idx, recurse on arr[left..pivot_idx-1]
    # 6. If k > pivot_idx, recurse on arr[pivot_idx+1..right]
    pass


def kth_smallest(arr, k):
    """
    Finds the k-th (1-indexed) smallest element in the array.
    - Uses a copy to avoid modifying the original array
    - Includes k range validation (1 <= k <= len(arr))
    """
    if k < 1 or k > len(arr):
        raise ValueError(f"k={k} is out of range [1, {len(arr)}]")
    a = arr[:]  # Preserve original -- partition modifies the array in-place
    return randomized_select(a, 0, len(a) - 1, k - 1)


def kth_smallest_sort(arr, k):
    """
    Sort-based method: O(n log n)
    - Sorts the entire array then accesses index k-1
    - Reference implementation for performance comparison with Quickselect
    """
    return sorted(arr)[k - 1]


if __name__ == "__main__":
    print("=" * 60)
    print("Randomized Select (Quickselect) Demo")
    print("=" * 60)

    # Correctness verification: compare Quickselect results with sort-based results
    data = [7, 10, 4, 3, 20, 15, 8]
    print(f"\nArray: {data}")
    print(f"Sorted: {sorted(data)}")
    print()

    for k in range(1, len(data) + 1):
        qs_result = kth_smallest(data, k)
        sort_result = kth_smallest_sort(data, k)
        status = "OK" if qs_result == sort_result else "MISMATCH"
        print(f"  {k}-th smallest: {qs_result} ({status})")

    # Performance comparison: Quickselect vs Sort at various input sizes
    # Quickselect is O(n), Sort is O(n log n), so the gap grows with n
    print("\n" + "=" * 60)
    print("Performance Comparison: Quickselect vs Sort")
    print("=" * 60)

    for n in [100_000, 500_000, 1_000_000]:
        big_data = [random.randint(1, 10**9) for _ in range(n)]
        k = n // 2  # Finding the median -- the most disadvantageous position

        # Quickselect measurement
        start = time.perf_counter()
        result_qs = kth_smallest(big_data, k)
        t_qs = time.perf_counter() - start

        # Sort + index measurement
        start = time.perf_counter()
        result_sort = kth_smallest_sort(big_data, k)
        t_sort = time.perf_counter() - start

        speedup = t_sort / t_qs if t_qs > 0 else float("inf")
        print(f"\n  N = {n:>10,}, k = {k:,} (median)")
        print(f"    Quickselect:  {t_qs:.4f}s")
        print(f"    Sort+index:   {t_sort:.4f}s")
        print(f"    Speedup:      {speedup:.1f}x")
