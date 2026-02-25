"""Merge Sort with step-by-step tracing."""


def merge_sort_trace(arr, depth=0):
    """Merge sort with recursive call visualization."""
    indent = "  " * depth
    print(f"{indent}merge_sort({arr})")

    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort_trace(arr[:mid], depth + 1)
    right = merge_sort_trace(arr[mid:], depth + 1)

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])

    print(f"{indent}  -> merged: {merged}")
    return merged


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("=== Merge Sort Trace ===\n")
    result = merge_sort_trace(data)
    print(f"\nFinal result: {result}")
