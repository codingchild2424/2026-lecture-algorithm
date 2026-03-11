# === A-2: Advanced Sorting Algorithms ===
# Merge Sort and Quick Sort — sorting based on Divide and Conquer
# Both algorithms have average time complexity O(n log n)
"""Advanced sorting algorithms - Merge Sort and Quick Sort."""
import random


def merge_sort(arr):
    """
    Merge Sort
    - Algorithm: split array in half -> recursively sort -> merge
    - Time complexity: O(n log n) — always the same (best/average/worst)
    - Space complexity: O(n) — additional array needed for merging
    - Characteristics: stable sort, consistent performance regardless of data distribution
    """
    # Base case: array with 1 or fewer elements is already sorted
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2  # Split the array in half
    left = merge_sort(arr[:mid])    # Recursively sort the left half
    right = merge_sort(arr[mid:])   # Recursively sort the right half
    return _merge(left, right)      # Merge the two sorted halves


def _merge(left, right):
    """
    Merge two sorted arrays into one sorted array
    - Compare from the front of both arrays and add the smaller element in order
    - Time complexity: O(n) — each element is processed only once
    """
    result = []
    i = j = 0  # Current comparison position in each array
    # Merge by comparing while both arrays have remaining elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])  # Add from left if smaller or equal (ensures stable sort)
            i += 1
        else:
            result.append(right[j])  # Add from right if smaller
            j += 1
    # Append remaining elements to result (one side was exhausted first)
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """
    Quick Sort
    - Algorithm: choose pivot -> partition around pivot -> recursively sort -> combine
    - Time complexity: O(n log n) average, O(n^2) worst (when pivot is always min/max)
    - Space complexity: O(n) — uses additional space due to list comprehension approach
    - Characteristics: one of the fastest general-purpose sorts in practice, good cache efficiency
    - This implementation uses a concise 3-way partition (Dutch National Flag)
    """
    # Base case: array with 1 or fewer elements is already sorted
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    # 3-way partition: classify elements as less than / equal to / greater than pivot
    left = [x for x in arr if x < pivot]      # Elements less than pivot
    middle = [x for x in arr if x == pivot]    # Elements equal to pivot
    right = [x for x in arr if x > pivot]      # Elements greater than pivot
    # Recursively sort left and right, then combine
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    test_data = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original:   {test_data}")
    print(f"Merge Sort: {merge_sort(test_data)}")
    print(f"Quick Sort: {quick_sort(test_data)}")

    # Verify correctness with 100 random datasets
    for _ in range(100):
        data = [random.randint(-100, 100) for _ in range(50)]
        expected = sorted(data)
        assert merge_sort(data) == expected, "Merge Sort failed!"
        assert quick_sort(data) == expected, "Quick Sort failed!"
    print("\nAll tests passed!")
