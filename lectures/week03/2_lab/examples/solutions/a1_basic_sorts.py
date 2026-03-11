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
    """
    a = arr[:]  # Copy to preserve the original array
    n = len(a)
    for i in range(n):
        min_idx = i  # Assume current position as the minimum index
        # Search for the minimum value in the remaining unsorted portion
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        # Swap the found minimum value with the current position
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def bubble_sort(arr):
    """
    Bubble Sort
    - Algorithm: compare adjacent elements and swap larger values to the back (repeatedly)
    - Time complexity: O(n^2) worst/average, O(n) best (already sorted)
    - Space complexity: O(1) (in-place, excluding the copy)
    - Characteristics: early termination optimization applied — stops if no swaps occur
    """
    a = arr[:]  # Copy to preserve the original array
    n = len(a)
    for i in range(n):
        swapped = False  # Track whether any swaps occurred in this pass
        # Each pass moves the largest element to the end, so reduce the range
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]  # Swap adjacent elements
                swapped = True
        # If no swaps occurred, the array is already sorted -> early termination
        if not swapped:
            break
    return a


def insertion_sort(arr):
    """
    Insertion Sort
    - Algorithm: insert each element into the correct position within the already sorted front portion
    - Time complexity: O(n^2) worst/average, O(n) best (already sorted)
    - Space complexity: O(1) (in-place, excluding the copy)
    - Characteristics: very efficient for nearly sorted data, stable sort
    """
    a = arr[:]  # Copy to preserve the original array
    for i in range(1, len(a)):
        key = a[i]  # Temporarily store the element to insert
        j = i - 1
        # Shift elements greater than key one position to the right
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        # Insert key at the correct position
        a[j + 1] = key
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
