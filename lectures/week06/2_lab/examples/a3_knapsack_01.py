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

    # Fill the table
    for i in range(1, n + 1):
        name, weight, value = items[i - 1]
        for w in range(capacity + 1):
            # Exclude case
            dp[i][w] = dp[i - 1][w]

            # Include case (only when weight is allowed)
            if weight <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)

    # Backtracking: reconstruct which items were selected
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            # The i-th item was selected
            selected.append(i - 1)  # 0-indexed
            w -= items[i - 1][1]  # Reduce by the item's weight

    selected.reverse()

    return dp[n][capacity], dp, selected


def print_dp_table(dp, items, capacity, selected):
    """Visually print the DP table.

    Args:
        dp: DP table
        items: list of items
        capacity: knapsack capacity
        selected: list of selected item indices
    """
    n = len(items)

    # Show only a portion if capacity is large
    max_cols = min(capacity + 1, 20)
    if capacity + 1 > max_cols:
        print(f"    (capacity is large, showing only w=0~{max_cols-1})")

    # Header (weights)
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

    # Table body
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

    # ===== Example 1: Basic example =====
    print(f"\n{'='*65}")
    print("[Example 1] Basic Knapsack Problem")
    print(f"{'='*65}")

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

    # ===== Example 2: Textbook example =====
    print(f"\n{'='*65}")
    print("[Example 2] Textbook Example")
    print(f"{'='*65}")

    items2 = [
        ("A", 2, 12),
        ("B", 1,  10),
        ("C", 3, 20),
        ("D", 2, 15),
    ]
    capacity2 = 5

    print(f"\n  Knapsack capacity: {capacity2}kg")
    print(f"  Item list:")
    print(f"  {'Name':<8} {'Weight':>6} {'Value':>6}")
    print(f"  {'-'*22}")
    for name, weight, value in items2:
        print(f"  {name:<8} {weight:>4}kg {value:>5}")

    max_value, dp, selected = knapsack_01(capacity2, items2)

    print(f"\n  --- DP Table (* = selected item) ---")
    print_dp_table(dp, items2, capacity2, selected)

    # Detailed backtracking explanation
    print(f"  --- Backtracking Process ---")
    n = len(items2)
    w = capacity2
    print(f"  Start: dp[{n}][{w}] = {dp[n][w]}")
    for i in range(n, 0, -1):
        name, weight, value = items2[i - 1]
        if dp[i][w] != dp[i - 1][w]:
            print(f"  i={i} ({name}): dp[{i}][{w}]={dp[i][w]} != dp[{i-1}][{w}]={dp[i-1][w]}"
                  f" -> selected! (w: {w} -> {w - weight})")
            w -= weight
        else:
            print(f"  i={i} ({name}): dp[{i}][{w}]={dp[i][w]} == dp[{i-1}][{w}]={dp[i-1][w]}"
                  f" -> not selected")

    print(f"\n  === Result ===")
    print(f"  Maximum value: {max_value}")
    print(f"  Selected items:")
    total_weight = 0
    for idx in selected:
        name, weight, value = items2[idx]
        total_weight += weight
        print(f"    - {name}: {weight}kg, {value}")
    print(f"  Total weight: {total_weight}kg / {capacity2}kg")

    # ===== Example 3: Case where greedy fails =====
    print(f"\n{'='*65}")
    print("[Example 3] Case Where Greedy (by ratio) Fails")
    print(f"{'='*65}")

    items3 = [
        ("A", 3, 31),   # ratio 10.3
        ("B", 4, 40),   # ratio 10.0
        ("C", 5, 45),   # ratio 9.0
    ]
    capacity3 = 8

    print(f"\n  Knapsack capacity: {capacity3}kg")
    print(f"  Item list (sorted by ratio):")
    sorted_items = sorted(items3, key=lambda x: x[2] / x[1], reverse=True)
    for name, weight, value in sorted_items:
        print(f"    {name}: {weight}kg, {value} (ratio: {value/weight:.1f}/kg)")

    # Greedy (by ratio)
    print(f"\n  Greedy result (insert by ratio order):")
    greedy_value = 0
    greedy_weight = 0
    greedy_items = []
    remaining = capacity3
    for name, weight, value in sorted_items:
        if weight <= remaining:
            greedy_items.append(name)
            greedy_value += value
            greedy_weight += weight
            remaining -= weight
            print(f"    + {name}: {weight}kg, {value} (remaining capacity: {remaining}kg)")
    print(f"  Greedy total value: {greedy_value} (weight: {greedy_weight}kg)")

    # DP
    max_value, dp, selected = knapsack_01(capacity3, items3)
    print(f"\n  DP result:")
    print(f"  Maximum value: {max_value}")
    print(f"  Selected items:")
    for idx in selected:
        name, weight, value = items3[idx]
        print(f"    - {name}: {weight}kg, {value}")

    if greedy_value < max_value:
        print(f"\n  -> Greedy({greedy_value}) < DP({max_value}): Greedy fails!")
    else:
        print(f"\n  -> Greedy = DP: identical in this case")

    # Summary
    print(f"\n{'='*65}")
    print(" Summary")
    print("=" * 65)
    print("""
  0-1 Knapsack DP:
  - dp[i][w] = max value with first i items under weight limit w
  - Recurrence: dp[i][w] = max(dp[i-1][w], dp[i-1][w-w_i] + v_i)
  - Time complexity: O(n * W) (pseudo-polynomial)
  - Space complexity: O(n * W), can be reduced to O(W) with 1D array

  Backtracking:
  - Start from dp[n][W]
  - If dp[i][w] != dp[i-1][w], the i-th item was selected
  - When selected, decrease w to w - w_i

  Greedy vs DP:
  - Fractional knapsack: greedy is optimal (by ratio)
  - 0-1 knapsack: greedy can fail -> DP is needed
""")
