"""Basic sorting algorithms - implement the TODOs."""
import random


def selection_sort(arr):
    """Selection Sort: find minimum, swap to front. O(n^2)"""
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def bubble_sort(arr):
    """Bubble Sort: repeatedly swap adjacent elements. O(n^2)"""
    a = arr[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def insertion_sort(arr):
    """Insertion Sort: insert each element into sorted prefix. O(n^2)"""
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


if __name__ == "__main__":
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {test_data}")
    print(f"Selection Sort: {selection_sort(test_data)}")
    print(f"Bubble Sort:    {bubble_sort(test_data)}")
    print(f"Insertion Sort: {insertion_sort(test_data)}")

    # Verify correctness
    for _ in range(100):
        data = [random.randint(-100, 100) for _ in range(50)]
        expected = sorted(data)
        assert selection_sort(data) == expected, "Selection Sort failed!"
        assert bubble_sort(data) == expected, "Bubble Sort failed!"
        assert insertion_sort(data) == expected, "Insertion Sort failed!"
    print("\nAll tests passed!")
