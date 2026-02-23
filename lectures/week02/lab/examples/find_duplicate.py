"""Find duplicate element - O(n^2) vs O(n) comparison."""
import random
from timer_util import measure_time


def has_duplicate_bruteforce(arr):
    """O(n^2): Check all pairs."""
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    return False


def has_duplicate_hashset(arr):
    """O(n): Use a set."""
    seen = set()
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False


if __name__ == "__main__":
    print(f"{'N':>10} | {'O(n²)':>12} | {'O(n)':>12} | {'Speedup':>8}")
    print("-" * 50)

    for n in [100, 1000, 10000, 50000]:
        data = list(range(n))  # No duplicates (worst case for both)
        random.shuffle(data)

        t1, _ = measure_time(has_duplicate_bruteforce, data)
        t2, _ = measure_time(has_duplicate_hashset, data)
        speedup = t1 / t2 if t2 > 0 else float('inf')

        print(f"{n:>10,} | {t1:>12.6f} | {t2:>12.6f} | {speedup:>7.1f}x")
