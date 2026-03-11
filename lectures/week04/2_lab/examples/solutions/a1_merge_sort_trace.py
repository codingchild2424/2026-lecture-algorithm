# === A-1: Merge Sort Trace ===
# Step-by-step visualization of the recursive merge sort process
# Displays the Divide -> Conquer -> Combine phases using indentation
"""Merge Sort with step-by-step tracing."""


def merge_sort_trace(arr, depth=0):
    """
    Merge sort + recursive call visualization
    - Algorithm: Split the array in half -> recursively sort -> merge two sorted arrays
    - Time complexity: O(n log n)
    - Space complexity: O(n log n) -- recursion depth O(log n) x O(n) per level
    - Uses the depth parameter to track recursion depth for indented output
    """
    indent = "  " * depth  # Indentation based on recursion depth
    print(f"{indent}merge_sort({arr})")

    # Base case: cannot split further if array has 1 or fewer elements
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2  # Determine split point at the middle index
    left = merge_sort_trace(arr[:mid], depth + 1)    # Recursively sort left half
    right = merge_sort_trace(arr[mid:], depth + 1)   # Recursively sort right half

    # Merge step: combine two sorted subarrays into one
    merged = []
    i = j = 0  # Current comparison positions in left/right arrays
    # Select the smaller element from each array in order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Append remaining elements after one array is exhausted
    merged.extend(left[i:])
    merged.extend(right[j:])

    print(f"{indent}  -> merged: {merged}")  # Print merge result
    return merged


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("=== Merge Sort Trace ===\n")
    result = merge_sort_trace(data)
    print(f"\nFinal result: {result}")
