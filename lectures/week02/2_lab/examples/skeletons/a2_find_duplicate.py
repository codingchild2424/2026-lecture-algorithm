# === A-2: Duplicate Element Detection ===
# Compares two algorithms for detecting whether an array contains duplicates.
# - Brute Force: O(n^2) — compares all pairs
# - HashSet: O(n) — linear scan using a set
#
# As N grows, the performance gap between O(n^2) and O(n) becomes dramatic.
"""Find duplicate element - O(n^2) vs O(n) comparison.

NOTE: The n=50,000 brute-force case may take several minutes due to O(n^2)
complexity. This is intentional -- it demonstrates why quadratic algorithms
become impractical at scale. Reduce the last test size if you need faster runs.
"""
import random
from a1_timer_util import measure_time


def has_duplicate_bruteforce(arr):
    """
    Brute-force duplicate detection: compares all pairs of elements.

    Algorithm: nested loops comparing arr[i] with arr[j] (j > i)
    Time complexity: O(n^2) — n*(n-1)/2 comparisons
    Space complexity: O(1) — no additional memory used
    """
    # TODO: Use nested loops to compare all pairs
    #   - Outer loop: i from 0 to n-1
    #   - Inner loop: j from i+1 to n-1
    #   - If arr[i] == arr[j], return True (duplicate found)
    # TODO: Return False if no duplicates found after all comparisons
    pass  # TODO: implement


def has_duplicate_hashset(arr):
    """
    HashSet duplicate detection: uses a set to track previously seen elements.

    Algorithm: iterate through array, check if each element is already in the set
    Time complexity: O(n) — set lookup/insertion is O(1) on average
    Space complexity: O(n) — worst case stores all elements in the set
    """
    # TODO: Create an empty set called `seen`
    # TODO: Iterate through each element x in arr:
    #   - If x is already in seen, return True (duplicate found)
    #   - Otherwise, add x to seen
    # TODO: Return False if all elements are unique
    pass  # TODO: implement


if __name__ == "__main__":
    # Prerequisite: implement measure_time() in a1_timer_util.py first
    _test = measure_time(lambda: None)
    if _test is None:
        print("ERROR: implement measure_time() in a1_timer_util.py first.")
        raise SystemExit(1)

    # Benchmark results table header
    print(f"{'N':>10} | {'O(n²)':>12} | {'O(n)':>12} | {'Speedup':>8}")
    print("-" * 50)

    for n in [100, 1000, 10000, 50000]:
        # Generate data with no duplicates (worst case: must compare all elements)
        data = list(range(n))  # No duplicates (worst case for both)
        random.shuffle(data)  # shuffle to avoid bias

        t1, _ = measure_time(has_duplicate_bruteforce, data)  # measure O(n^2)
        t2, _ = measure_time(has_duplicate_hashset, data)  # measure O(n)
        speedup = t1 / t2 if t2 > 0 else float('inf')  # compute speedup ratio

        print(f"{n:>10,} | {t1:>12.6f} | {t2:>12.6f} | {speedup:>7.1f}x")
