# === A-3: 0-1 Knapsack Problem - Detailed DP Table Visualization ===
# Visually show the DP table construction process and explain the backtracking in detail
#
# Key concepts:
# - dp[i][w] = maximum value with the first i items under weight limit w
# - Recurrence: dp[i][w] = max(dp[i-1][w], dp[i-1][w-w_i] + v_i)
# - Backtracking: if dp[i][w] != dp[i-1][w], the i-th item was selected
# - Demonstrate with an example that greedy (by ratio) can fail for 0-1 knapsack
# - Time complexity: O(n * W) (pseudo-polynomial)
# - Space complexity: O(n * W), can be optimized to O(W) with a 1D array
"""
0-1 Knapsack Problem -- DP + Backtracking

A knapsack problem where each item can only be included (1) or excluded (0).
Build the DP table and reconstruct the selected items via backtracking.

Recurrence:
  dp[i][w] = max(
      dp[i-1][w],                          # case: do not include the i-th item
      dp[i-1][w - weight[i]] + value[i]     # case: include the i-th item (weight[i] <= w)
  )
"""


def knapsack_01(capacity, items):
    """Solve the 0-1 knapsack problem using DP.

    Args:
        capacity: maximum weight of the knapsack (integer)
        items: [(name, weight, value), ...] list

    Returns:
        (maximum value, DP table, list of selected item indices)
    """
    n = len(items)

    # DP table: dp[i][w] = max value with first i items under weight limit w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # TODO: Fill the table
    # For i in range(1, n+1):
    #   Get name, weight, value from items[i-1]
    #   For w in range(capacity+1):
    #     dp[i][w] = dp[i-1][w]  (exclude case)
    #     If weight <= w:
    #       dp[i][w] = max(dp[i][w], dp[i-1][w-weight] + value)
    pass  # TODO: implement

    # TODO: Backtracking - reconstruct which items were selected
    # Start from w = capacity
    # For i from n down to 1:
    #   If dp[i][w] != dp[i-1][w], item i-1 was selected
    #   Append index and reduce w by item's weight
    selected = []
    pass  # TODO: implement backtracking

    return dp[n][capacity], dp, selected


def print_dp_table(dp, items, capacity, selected):
    """Visually print the DP table."""
    n = len(items)
    max_cols = min(capacity + 1, 20)
    if capacity + 1 > max_cols:
        print(f"    (capacity is large, showing only w=0~{max_cols-1})")

    print(f"    {'Item':<8} ", end="")
    for w in range(max_cols):
        print(f"{w:>4}", end=" ")
    if capacity + 1 > max_cols:
        print(f" ... {capacity:>4}", end="")
    print()

    print(f"    {'-'*8}-", end="")
    for w in range(max_cols):
        print(f"{'----'}", end="-")
    print()

    for i in range(n + 1):
        if i == 0:
            label = "(none)"
        else:
            name, weight, value = items[i - 1]
            marker = " *" if (i - 1) in selected else ""
            label = f"{name}{marker}"

        print(f"    {label:<8} ", end="")
        for w in range(max_cols):
            val = dp[i][w]
            if val > 0:
                print(f"{val:>4}", end=" ")
            else:
                print(f"{'0':>4}", end=" ")

        if capacity + 1 > max_cols:
            print(f" ... {dp[i][capacity]:>4}", end="")
        print()

    print()


if __name__ == "__main__":
    print("=" * 65)
    print(" 0-1 Knapsack Problem -- DP + Backtracking")
    print("=" * 65)

    # Example 1: Basic example
    items1 = [
        ("Gold",     3, 60),
        ("Silver",   4, 70),
        ("Jewel",    2, 40),
        ("Pottery",  5, 90),
    ]
    capacity1 = 10

    print(f"\n  Knapsack capacity: {capacity1}kg")
    print(f"  Item list:")
    print(f"  {'Name':<8} {'Weight':>6} {'Value':>6} {'Ratio':>10}")
    print(f"  {'-'*32}")
    for name, weight, value in items1:
        print(f"  {name:<8} {weight:>4}kg {value:>5} {value/weight:>9.1f}/kg")

    max_value, dp, selected = knapsack_01(capacity1, items1)

    print(f"\n  --- DP Table (* = selected item) ---")
    print_dp_table(dp, items1, capacity1, selected)

    print(f"  === Result ===")
    print(f"  Maximum value: {max_value}")
    print(f"  Selected items:")
    total_weight = 0
    for idx in selected:
        name, weight, value = items1[idx]
        total_weight += weight
        print(f"    - {name}: {weight}kg, {value}")
    print(f"  Total weight: {total_weight}kg / {capacity1}kg")
