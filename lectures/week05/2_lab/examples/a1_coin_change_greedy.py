# === A-1: Coin Change - Greedy vs DP Detailed Comparison ===
# Analysis of when the greedy algorithm guarantees optimality and when it fails
#
# Key concepts:
# - Greedy strategy: Always use the largest coin first
# - Greedy choice property: Holds when coins have divisibility relationships
# - DP can always find the optimal solution
# - Time complexity: Greedy O(k), DP O(k * amount)
"""
Coin Change -- Success and Failure of the Greedy Algorithm

Greedy strategy: Always use the largest coin first.
- Guarantees the optimal solution for standard coin sets.
- Does NOT guarantee the optimal solution for non-standard coin sets.
"""


def greedy_coin_change(coins, amount):
    """Calculate change using the greedy approach.

    Strategy: use the largest coin as much as possible.

    Args:
        coins: List of coin denominations (no need to pre-sort descending; sorted internally)
        amount: The amount of change to make

    Returns:
        (list of coins used, total coin count) or None if change cannot be made
    """
    coins_sorted = sorted(coins, reverse=True)
    result = []
    remaining = amount

    for coin in coins_sorted:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin

    if remaining == 0:
        return result, len(result)
    return None


def dp_coin_change(coins, amount):
    """Calculate minimum number of coins using DP.

    dp[i] = minimum number of coins to make amount i

    Args:
        coins: List of coin denominations
        amount: The amount of change to make

    Returns:
        (list of coins used, total coin count) or None if change cannot be made
    """
    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)  # Array for backtracking

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin

    if dp[amount] == INF:
        return None

    # Recover the coins used via backtracking
    result = []
    current = amount
    while current > 0:
        result.append(parent[current])
        current -= parent[current]

    return result, len(result)


def test_coin_set(coins, amount, label):
    """Compare greedy and DP results for a given coin set."""
    print(f"\n{'='*60}")
    print(f"[{label}]")
    print(f"Coin types: {coins}")
    print(f"Amount to change: {amount}")
    print(f"{'='*60}")

    greedy_result = greedy_coin_change(coins, amount)
    dp_result = dp_coin_change(coins, amount)

    if greedy_result:
        g_coins, g_count = greedy_result
        print(f"\n  Greedy result: {g_coins}")
        print(f"  Coin count: {g_count}")
    else:
        print("\n  Greedy: Cannot make change")

    if dp_result:
        d_coins, d_count = dp_result
        print(f"\n  DP result (optimal): {d_coins}")
        print(f"  Coin count: {d_count}")
    else:
        print("\n  DP: Cannot make change")

    # Comparison
    if greedy_result and dp_result:
        g_count = greedy_result[1]
        d_count = dp_result[1]
        if g_count == d_count:
            print(f"\n  --> Greedy = Optimal (same {g_count} coins)")
        else:
            print(f"\n  --> Greedy failed! Greedy({g_count}) > Optimal({d_count})")
            print(f"      Greedy uses {g_count - d_count} more coins")


if __name__ == "__main__":
    print("=" * 60)
    print(" Coin Change: Greedy vs DP (Optimal)")
    print("=" * 60)

    # --- Success cases: Standard coin sets ---

    test_coin_set(
        coins=[500, 100, 50, 10],
        amount=770,
        label="Success Case 1: Korean standard coins",
    )

    test_coin_set(
        coins=[25, 10, 5, 1],
        amount=63,
        label="Success Case 2: US standard coins (quarter/dime/nickel/penny)",
    )

    # --- Failure cases: Non-standard coin sets ---

    test_coin_set(
        coins=[7, 5, 1],
        amount=10,
        label="Failure Case 1: {7, 5, 1} coins for amount 10",
    )
    # Greedy: 7+1+1+1 = 4 coins, Optimal: 5+5 = 2 coins

    test_coin_set(
        coins=[6, 4, 1],
        amount=8,
        label="Failure Case 2: {6, 4, 1} coins for amount 8",
    )
    # Greedy: 6+1+1 = 3 coins, Optimal: 4+4 = 2 coins

    test_coin_set(
        coins=[12, 9, 1],
        amount=18,
        label="Failure Case 3: {12, 9, 1} coins for amount 18",
    )
    # Greedy: 12+1*6 = 7 coins, Optimal: 9+9 = 2 coins

    # --- Summary ---
    print("\n" + "=" * 60)
    print(" Summary")
    print("=" * 60)
    print("""
  When greedy is optimal:
  - When each coin is a multiple of smaller coins (e.g., 500, 100, 50, 10)
  - In this case, the 'greedy choice property' holds

  When greedy fails:
  - When the divisibility relationship between coins does not hold
  - In this case, DP must be used to find the optimal solution
  - Time complexity: Greedy O(k), DP O(k * amount)  (k = number of coin types)
""")
