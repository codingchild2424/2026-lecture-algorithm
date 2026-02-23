"""0-1 Knapsack with backtracking."""


def knapsack_01(capacity, items):
    """
    items: list of (value, weight, name)
    Returns: max value, selected items.
    """
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        v, w, _ = items[i - 1]
        for j in range(capacity + 1):
            dp[i][j] = dp[i - 1][j]
            if w <= j and dp[i - 1][j - w] + v > dp[i][j]:
                dp[i][j] = dp[i - 1][j - w] + v

    # Backtrack
    selected = []
    j = capacity
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected.append(items[i - 1])
            j -= items[i - 1][1]

    return dp[n][capacity], list(reversed(selected))


if __name__ == "__main__":
    items = [
        (60, 10, "Laptop"),
        (100, 20, "Camera"),
        (120, 30, "Painting"),
        (40, 5, "Book"),
    ]
    capacity = 50

    print(f"Items: {[(name, f'v={v}, w={w}') for v, w, name in items]}")
    print(f"Capacity: {capacity}\n")

    max_val, selected = knapsack_01(capacity, items)
    print(f"Maximum value: {max_val}")
    print(f"Selected items:")
    total_weight = 0
    for v, w, name in selected:
        print(f"  {name}: value={v}, weight={w}")
        total_weight += w
    print(f"Total weight: {total_weight}/{capacity}")
