# === A-2: Find All Duplicate Elements ===
# Compares two algorithms for finding all duplicate elements in an array.
# - Brute Force: O(n^2) — nested loops comparing all pairs
# - HashSet: O(n) — linear scan using two sets
#
# Difference from a2_find_duplicate.py:
#   - find_duplicate: only checks existence of duplicates (True/False)
#   - find_duplicates: finds and returns all duplicate elements (set)
"""
Find all duplicate elements — O(n^2) vs O(n) comparison
"""

import time
import random


def find_duplicates_bruteforce(arr):
    """
    Finds all duplicate elements using brute force.

    Algorithm: nested loops comparing all (i, j) pairs, collecting matching values
    Time complexity: O(n^2) — n*(n-1)/2 comparisons
    Space complexity: O(d) — where d is the number of duplicate elements
    """
    # TODO: Create an empty set called `duplicates`
    # TODO: Use nested loops (i, j where j > i) to compare all pairs
    #   - If arr[i] == arr[j], add arr[i] to the duplicates set
    # TODO: Return the duplicates set
    return set()  # TODO: implement


def find_duplicates_hashset(arr):
    """
    Finds all duplicate elements using hash sets.

    Algorithm:
      - seen: stores elements encountered so far
      - duplicates: stores elements that appear more than once
      - Iterate through array; if element is in seen, add to duplicates

    Time complexity: O(n) — set lookup/insertion is O(1) on average
    Space complexity: O(n) — seen set stores up to n elements
    """
    # TODO: Create two empty sets: `seen` and `duplicates`
    # TODO: Iterate through each element x in arr:
    #   - If x is in seen, add x to duplicates
    #   - Otherwise, add x to seen
    # TODO: Return the duplicates set
    return set()  # TODO: implement


def generate_test_data(n, duplicate_ratio=0.3):
    """
    Generates test data containing duplicates.

    Parameters:
      n              — total data size
      duplicate_ratio — ratio of duplicates (default: 0.3 = 30%)

    Algorithm:
      1. Number of unique elements = n * (1 - duplicate_ratio)
      2. Fill remaining slots with random picks from existing range to create duplicates
      3. Shuffle and return

    Time complexity: O(n)
    Space complexity: O(n)
    """
    unique_count = int(n * (1 - duplicate_ratio))  # compute number of unique elements
    base = list(range(unique_count))  # unique elements from 0 to unique_count-1
    extras = [random.randint(0, unique_count - 1) for _ in range(n - unique_count)]  # generate duplicates
    data = base + extras  # combine unique and duplicate elements
    random.shuffle(data)  # randomize order
    return data


def benchmark_one(func, data, repeat=3):
    """
    Repeatedly measures a function's execution time and returns the average.

    Time complexity: O(repeat * T(func))
    """
    times = []
    for _ in range(repeat):
        start = time.perf_counter()  # high-resolution start time
        func(data)
        end = time.perf_counter()  # high-resolution end time
        times.append(end - start)
    return sum(times) / len(times)  # return average


if __name__ == "__main__":
    print("=" * 65)
    print("Find Duplicates: O(n^2) vs O(n) Benchmark")
    print("=" * 65)

    # Correctness verification: ensure both algorithms produce the same result
    test = [1, 2, 3, 2, 4, 5, 1, 6]
    bf_result = find_duplicates_bruteforce(test)  # brute-force result
    hs_result = find_duplicates_hashset(test)  # hash set result
    print(f"\nTest data: {test}")
    print(f"Bruteforce result: {bf_result}")
    print(f"HashSet result:    {hs_result}")
    if bf_result == hs_result and len(bf_result) > 0:
        print("-> Both results match\n")
    else:
        print("-> TODO: implement the functions above to find duplicates {1, 2}\n")

    # Benchmark: compare execution times across input sizes
    sizes = [1000, 2000, 5000, 10000]
    print(f"{'N':>8s} | {'O(n^2) [sec]':>12s} | {'O(n) [sec]':>12s} | {'Speedup':>8s}")
    print("-" * 50)

    for n in sizes:
        data = generate_test_data(n)  # generate test data with duplicates

        # O(n^2) is too slow for large N, so skip if necessary
        if n <= 10000:
            t_bf = benchmark_one(find_duplicates_bruteforce, data, repeat=1)
        else:
            t_bf = float("inf")  # too slow — skip

        t_hs = benchmark_one(find_duplicates_hashset, data, repeat=3)

        if t_bf != float("inf"):
            ratio = t_bf / t_hs if t_hs > 0 else float("inf")  # compute speedup ratio
            print(f"{n:>8d} | {t_bf:>12.6f} | {t_hs:>12.6f} | {ratio:>7.1f}x")
        else:
            print(f"{n:>8d} | {'(skip)':>12s} | {t_hs:>12.6f} | {'N/A':>8s}")

    # Key takeaway: impact of algorithm complexity on real-world performance
    print("\nConclusion: As N grows, the gap between O(n^2) and O(n) becomes dramatic.")
    print("When N doubles, O(n^2) takes ~4x longer while O(n) takes ~2x longer.")
