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

    Steps:
      1. Base case: if len(arr) <= 1, return a copy
      2. Find the midpoint and split into left and right halves
      3. Recursively sort each half
      4. Merge the two sorted halves using _merge()
    """
    # TODO: Implement merge sort
    # Hint: base case -> split -> recurse on halves -> merge
    if len(arr) <= 1:
        return arr[:]
    pass  # TODO: implement the rest


def _merge(left, right):
    """
    Merge two sorted arrays into one sorted array
    - Compare from the front of both arrays and add the smaller element in order
    - Time complexity: O(n) — each element is processed only once

    Steps:
      1. Initialize an empty result list and two index pointers i, j = 0, 0
      2. While both arrays have remaining elements:
         - Append the smaller of left[i] and right[j] to result
         - Advance the corresponding pointer
      3. Append any remaining elements from either array
      4. Return result
    """
    result = []
    i = j = 0
    # TODO: Implement the merge of two sorted arrays
    # Hint: use a while loop comparing left[i] and right[j],
    #       then extend with the remaining elements.
    pass
    return result


def quick_sort(arr):
    """
    Quick Sort
    - Algorithm: choose pivot -> partition around pivot -> recursively sort -> combine
    - Time complexity: O(n log n) average, O(n^2) worst (when pivot is always min/max)
    - Space complexity: O(n) — uses additional space due to list comprehension approach
    - Characteristics: one of the fastest general-purpose sorts in practice, good cache efficiency
    - This implementation uses a concise 3-way partition (Dutch National Flag)

    Steps:
      1. Base case: if len(arr) <= 1, return a copy
      2. Choose the middle element as pivot
      3. Partition into three lists:
         - left:   elements < pivot
         - middle: elements == pivot
         - right:  elements > pivot
      4. Recursively sort left and right, then concatenate: left + middle + right
    """
    # TODO: Implement quick sort with 3-way partition
    # Hint: use list comprehensions for the partition step.
    if len(arr) <= 1:
        return arr[:]
    pass  # TODO: implement the rest


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
