# === A-3: 0-1 Knapsack Problem ===
# Solving the 0-1 knapsack problem using DP + backtracking
#
# Key concepts:
# - Each item can only be included (1) or excluded (0)
# - Recurrence: dp[i][w] = max(dp[i-1][w], dp[i-1][w-w_i] + v_i)
#     - dp[i-1][w]: case where the i-th item is not included
#     - dp[i-1][w-w_i] + v_i: case where the i-th item is included
# - Backtracking: if dp[i][w] != dp[i-1][w], the i-th item was selected
# - Time complexity: O(n * W) (n = number of items, W = knapsack capacity, pseudo-polynomial)
# - Space complexity: O(n * W), can be optimized to O(W) with a 1D array
"""0-1 Knapsack Problem -- find the optimal solution and selected items using DP + backtracking."""


def knapsack_01(capacity, items):
    """Solve the 0-1 knapsack problem using DP.

    Algorithm:
    1. dp[i][j] = maximum value achievable with the first i items under weight limit j
    2. For each item, choose the larger value between including and excluding it
    3. Backtrack to reconstruct the actually selected items

    Time complexity: O(n * capacity)
    Space complexity: O(n * capacity)

    Args:
        capacity: maximum weight of the knapsack (integer)
        items: [(value, weight, name), ...] list

    Returns:
        (maximum value, list of selected items)
    """
    n = len(items)
    # DP table initialization: dp[i][j] = max value with first i items and weight limit j
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the table
    for i in range(1, n + 1):
        v, w, _ = items[i - 1]  # value and weight of the i-th item
        for j in range(capacity + 1):
            dp[i][j] = dp[i - 1][j]  # Exclude case (copy value from previous row)
            # Include case: if weight is allowed and including yields greater value
            if w <= j and dp[i - 1][j - w] + v > dp[i][j]:
                dp[i][j] = dp[i - 1][j - w] + v

    # Backtracking: trace back through the DP table to reconstruct selected items
    selected = []
    j = capacity
    for i in range(n, 0, -1):
        # If dp[i][j] != dp[i-1][j], the i-th item was selected
        if dp[i][j] != dp[i - 1][j]:
            selected.append(items[i - 1])
            j -= items[i - 1][1]  # Reduce remaining capacity by the selected item's weight

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
