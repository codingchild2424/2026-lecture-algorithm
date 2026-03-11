# === A-2: Fractional Knapsack Problem ===
# A knapsack problem where the greedy algorithm guarantees the optimal solution
#
# Key concepts:
# - Greedy strategy: Select items with the highest value-to-weight ratio first
# - Since items can be split, greedy always guarantees the optimal solution
# - Difference from 0-1 knapsack: Splittable -> greedy optimal, Not splittable -> DP needed
# - Time complexity: O(n log n) (sorting dominates)
# - Space complexity: O(n)
"""
Fractional Knapsack Problem

Greedy strategy: Select items with the highest value/weight ratio first.
Since items can be split, greedy always guarantees the optimal solution.
"""


def fractional_knapsack(capacity, items):
    """Solve the fractional knapsack problem using a greedy approach.

    Args:
        capacity: Maximum weight of the knapsack
        items: [(name, weight, value), ...] list

    Returns:
        (maximum value, list of selected items)
        Selected items: [(name, weight added, value added, ratio, was_split), ...]
    """
    # TODO: implement fractional knapsack
    # Hints:
    # 1. Sort items by value/weight ratio in descending order
    #    sorted_items = sorted(items, key=lambda x: x[2] / x[1], reverse=True)
    # 2. Initialize total_value = 0.0, remaining_capacity = capacity, selected = []
    # 3. For each item (name, weight, value) in sorted order:
    #    a. If remaining_capacity <= 0, break
    #    b. Calculate ratio = value / weight
    #    c. If weight <= remaining_capacity:
    #       - Take the whole item: append (name, weight, value, ratio, False)
    #       - Update total_value and remaining_capacity
    #    d. Else:
    #       - Take a fraction: fraction = remaining_capacity / weight
    #       - partial_value = value * fraction
    #       - Append (name, remaining_capacity, partial_value, ratio, True)
    #       - Update total_value, set remaining_capacity = 0
    # 4. Return (total_value, selected)
    pass


def knapsack_01_bruteforce(capacity, items):
    """Solve the 0-1 knapsack problem using brute force (for comparison).

    Args:
        capacity: Maximum weight of the knapsack
        items: [(name, weight, value), ...] list

    Returns:
        (maximum value, list of selected item indices)
    """
    n = len(items)
    best_value = 0
    best_selection = []

    for mask in range(1 << n):
        total_weight = 0
        total_value = 0
        selection = []

        for i in range(n):
            if mask & (1 << i):
                name, weight, value = items[i]
                total_weight += weight
                total_value += value
                selection.append(i)

        if total_weight <= capacity and total_value > best_value:
            best_value = total_value
            best_selection = selection

    return best_value, best_selection


if __name__ == "__main__":
    print("=" * 60)
    print(" Fractional Knapsack Problem")
    print("=" * 60)

    # Example 1: Basic example
    items1 = [
        ("Gold",     10.0, 600),
        ("Silver",   20.0, 500),
        ("Copper",   30.0, 400),
        ("Jewels",    5.0, 300),
        ("Ceramics", 15.0, 200),
    ]

    print("\n" + "=" * 60)
    print("[Example 1] Basic knapsack problem")
    print("=" * 60)

    result = fractional_knapsack(40, items1)

    if result:
        total_value, selected = result
        print(f"\n  === Result ===")
        print(f"  Maximum value: {total_value:.0f}")
        print(f"  Selected items:")
        for name, weight, value, ratio, is_fraction in selected:
            marker = " (split)" if is_fraction else ""
            print(f"    - {name}: {weight:.1f}kg, {value:.0f}{marker}")
    else:
        print("\n  fractional_knapsack not implemented yet")

    # Example 2: Comparison with 0-1 knapsack
    items2 = [
        ("A",  10.0, 60),
        ("B",  20.0, 100),
        ("C",  30.0, 120),
    ]

    print("\n" + "=" * 60)
    print("[Example 2] Fractional vs 0-1 knapsack comparison")
    print("=" * 60)

    frac_result = fractional_knapsack(50, items2)

    if frac_result:
        frac_value, frac_selected = frac_result
        print(f"\n  === Fractional knapsack result ===")
        print(f"  Maximum value: {frac_value:.0f}")
    else:
        frac_value = None
        print("\n  fractional_knapsack not implemented yet")

    # 0-1 knapsack (brute force)
    bf_value, bf_selection = knapsack_01_bruteforce(50, items2)

    print(f"\n  === 0-1 knapsack result (brute force) ===")
    print(f"  Maximum value: {bf_value:.0f}")
    print(f"  Selected items:")
    for i in bf_selection:
        name, weight, value = items2[i]
        print(f"    - {name}: {weight:.1f}kg, {value:.0f}")

    if frac_value is not None:
        print(f"\n  Fractional knapsack({frac_value:.0f}) >= 0-1 knapsack({bf_value:.0f})")
        print(f"  Fractional knapsack can always achieve value >= 0-1 knapsack")

    # Summary
    print("\n" + "=" * 60)
    print(" Summary")
    print("=" * 60)
    print("""
  Fractional knapsack -- greedy strategy:
  1. Calculate the value/weight ratio for each item
  2. Sort by ratio in descending order
  3. Fill the knapsack with remaining capacity (split if needed)

  Time complexity: O(n log n) -- sorting dominates
  Space complexity: O(n)

  Why greedy is optimal:
  - Prioritizing items with the highest value per unit weight
    maintains optimal selection for the remaining capacity
  - Since items can be split, the question is not "include or not"
    but "how much to include"
""")
