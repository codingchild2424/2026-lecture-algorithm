# === A-1: Coin Change ===
# Success/failure cases of the greedy algorithm and comparison with DP optimal solution
#
# Key concepts:
# - Greedy: Use the largest coin first (optimal only for standard coin sets)
# - DP: Considers all cases to guarantee the optimal solution
# - Time complexity: Greedy O(k), DP O(k * amount) (k = number of coin types)
"""Coin change -- success and failure cases of the greedy approach."""


def coin_change_greedy(amount, coins):
    """Calculate change using the greedy approach.

    Algorithm: Use the largest coin as much as possible first
    Time complexity: O(k * amount/min_coin) (k = number of coin types)
    Space complexity: O(amount/min_coin) (result list)

    Args:
        amount: The amount of change to make
        coins: List of coin denominations

    Returns:
        List of coins used, or None (if impossible)
    """
    # Sort coins in descending order (key to greedy selection)
    coins_sorted = sorted(coins, reverse=True)
    result = []
    remaining = amount
    # For each coin, use it as many times as possible
    for coin in coins_sorted:
        while remaining >= coin:
            result.append(coin)  # Use the current coin
            remaining -= coin     # Decrease remaining amount
    # Success if remaining is 0, failure otherwise
    return result if remaining == 0 else None


def coin_change_dp(amount, coins):
    """Calculate minimum number of coins using DP (always guarantees optimal solution).

    Algorithm: dp[i] = minimum number of coins to make amount i
    Recurrence: dp[i] = min(dp[i - c] + 1) (for all coins c)
    Time complexity: O(k * amount)
    Space complexity: O(amount)

    Args:
        amount: The amount of change to make
        coins: List of coin denominations

    Returns:
        Optimal list of coins, or None (if impossible)
    """
    # dp[i]: minimum number of coins to make amount i (initial value: infinity)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: amount 0 requires 0 coins
    parent = [-1] * (amount + 1)  # For backtracking: last coin used at each amount
    # Try all coins for every amount
    for i in range(1, amount + 1):
        for c in coins:
            # If coin c can be used and results in fewer coins
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
                parent[i] = c  # Record the coin used for backtracking
    # If the amount cannot be made
    if dp[amount] == float('inf'):
        return None
    # Backtrack: recover the coins used by following the parent array
    result = []
    cur = amount
    while cur > 0:
        result.append(parent[cur])
        cur -= parent[cur]
    return result


if __name__ == "__main__":
    # Case 1: Greedy finds the optimal solution (standard coins)
    print("=== Case 1: Standard coins ===")
    coins1, amount1 = [500, 100, 50, 10], 1260
    g1 = coin_change_greedy(amount1, coins1)
    print(f"Coins: {coins1}, Amount: {amount1}")
    print(f"Greedy: {g1} ({len(g1)} coins)")

    # Case 2: Greedy fails (non-standard coins)
    # With {1, 3, 4} making 6: greedy gives 4+1+1=3 coins, optimal is 3+3=2 coins
    print("\n=== Case 2: Non-standard coins ===")
    coins2, amount2 = [1, 3, 4], 6
    g2 = coin_change_greedy(amount2, coins2)
    d2 = coin_change_dp(amount2, coins2)
    print(f"Coins: {coins2}, Amount: {amount2}")
    print(f"Greedy:  {g2} ({len(g2)} coins)")
    print(f"Optimal: {d2} ({len(d2)} coins)")
    print(f"-> Greedy is NOT optimal here!")
