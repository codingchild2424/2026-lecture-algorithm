# === A-1: Basic Sorting Algorithms ===
# Implementation of Selection Sort, Bubble Sort, and Insertion Sort
# All three algorithms have time complexity O(n^2) and space complexity O(n) (using copies)
"""Basic sorting algorithms - implement the TODOs."""
import random


def selection_sort(arr):
    """
    Selection Sort
    - Algorithm: find the minimum value in the unsorted portion and swap with the current position
    - Time complexity: O(n^2) — always compares all pairs
    - Space complexity: O(1) (in-place, excluding the copy)
    - Characteristics: only O(n) swaps, unstable sort

    Steps:
      1. Copy the input array
      2. For each position i from 0 to n-1:
         a. Find the index of the minimum element in arr[i:]
         b. Swap arr[i] with arr[min_idx]
      3. Return the sorted copy
    """
    a = arr[:]  # Copy to preserve the original array
    n = len(a)
    # TODO: Implement selection sort
    # Hint: use a nested loop — outer loop picks the position,
    #       inner loop finds the minimum in the remaining unsorted portion,
    #       then swap.
    pass
    return a


def bubble_sort(arr):
    """
    Bubble Sort
    - Algorithm: compare adjacent elements and swap larger values to the back (repeatedly)
    - Time complexity: O(n^2) worst/average, O(n) best (already sorted)
    - Space complexity: O(1) (in-place, excluding the copy)
    - Characteristics: early termination optimization applied — stops if no swaps occur

    Steps:
      1. Copy the input array
      2. For each pass i from 0 to n-1:
         a. Track whether any swap occurred (swapped flag)
         b. Compare adjacent pairs a[j] and a[j+1] for j in range(0, n-i-1)
         c. Swap if a[j] > a[j+1]
         d. If no swaps occurred in this pass, break early
      3. Return the sorted copy
    """
    a = arr[:]  # Copy to preserve the original array
    n = len(a)
    # TODO: Implement bubble sort with early termination
    # Hint: use a `swapped` flag — if no swaps happen in a full pass,
    #       the array is already sorted and you can break.
    pass
    return a


def insertion_sort(arr):
    """
    Insertion Sort
    - Algorithm: insert each element into the correct position within the already sorted front portion
    - Time complexity: O(n^2) worst/average, O(n) best (already sorted)
    - Space complexity: O(1) (in-place, excluding the copy)
    - Characteristics: very efficient for nearly sorted data, stable sort

    Steps:
      1. Copy the input array
      2. For each index i from 1 to n-1:
         a. Save a[i] as `key`
         b. Shift all elements a[j] > key one position to the right (j from i-1 downward)
         c. Place key at the correct position
      3. Return the sorted copy
    """
    a = arr[:]  # Copy to preserve the original array
    # TODO: Implement insertion sort
    # Hint: for each element, use a while loop to shift larger elements
    #       to the right, then insert the key.
    pass
    return a


if __name__ == "__main__":
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {test_data}")
    print(f"Selection Sort: {selection_sort(test_data)}")
    print(f"Bubble Sort:    {bubble_sort(test_data)}")
    print(f"Insertion Sort: {insertion_sort(test_data)}")

    # Verify correctness with 100 random datasets
    for _ in range(100):
        data = [random.randint(-100, 100) for _ in range(50)]
        expected = sorted(data)
        assert selection_sort(data) == expected, "Selection Sort failed!"
        assert bubble_sort(data) == expected, "Bubble Sort failed!"
        assert insertion_sort(data) == expected, "Insertion Sort failed!"
    print("\nAll tests passed!")
