"""Binary Search - Iterative and Recursive implementations."""


def binary_search_iterative(arr, target):
    """Return the index of target in sorted arr, or -1 if not found."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursive(arr, target, left, right):
    """Return the index of target in sorted arr[left..right], or -1."""
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7

    # Iterative
    idx = binary_search_iterative(data, target)
    print(f"Iterative: {target} found at index {idx}")

    # Recursive
    idx = binary_search_recursive(data, target, 0, len(data) - 1)
    print(f"Recursive: {target} found at index {idx}")

    # Step-by-step trace
    print(f"\n--- Binary Search Trace for target={target} ---")
    left, right = 0, len(data) - 1
    step = 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Step {step}: range=[{left},{right}], mid={mid}, arr[mid]={data[mid]}")
        if data[mid] == target:
            print(f"  -> Found at index {mid}!")
            break
        elif data[mid] < target:
            print(f"  -> {data[mid]} < {target}, search right half")
            left = mid + 1
        else:
            print(f"  -> {data[mid]} > {target}, search left half")
            right = mid - 1
        step += 1
