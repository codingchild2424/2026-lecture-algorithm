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
    # TODO: implement greedy coin change
    # Hints:
    # 1. Sort coins in descending order
    # 2. For each coin, use it as many times as possible (while remaining >= coin)
    # 3. Return the result list if remaining == 0, else None
    pass


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
    # TODO: implement DP coin change
    # Hints:
    # 1. Create dp array of size (amount+1), initialized to infinity; dp[0] = 0
    # 2. Create parent array of size (amount+1) for backtracking (last coin used)
    # 3. For each amount i from 1 to amount:
    #      For each coin c: if c <= i and dp[i-c]+1 < dp[i], update dp[i] and parent[i]
    # 4. If dp[amount] == inf, return None
    # 5. Backtrack using parent array to recover the list of coins used
    pass


if __name__ == "__main__":
    # Case 1: Greedy finds the optimal solution (standard coins)
    print("=== Case 1: Standard coins ===")
    coins1, amount1 = [500, 100, 50, 10], 1260
    g1 = coin_change_greedy(amount1, coins1)
    print(f"Coins: {coins1}, Amount: {amount1}")
    if g1:
        print(f"Greedy: {g1} ({len(g1)} coins)")
    else:
        print("Greedy: Not implemented yet")

    # Case 2: Greedy fails (non-standard coins)
    # With {1, 3, 4} making 6: greedy gives 4+1+1=3 coins, optimal is 3+3=2 coins
    print("\n=== Case 2: Non-standard coins ===")
    coins2, amount2 = [1, 3, 4], 6
    g2 = coin_change_greedy(amount2, coins2)
    d2 = coin_change_dp(amount2, coins2)
    print(f"Coins: {coins2}, Amount: {amount2}")
    if g2:
        print(f"Greedy:  {g2} ({len(g2)} coins)")
    else:
        print("Greedy: Not implemented yet")
    if d2:
        print(f"Optimal: {d2} ({len(d2)} coins)")
        print(f"-> Greedy is NOT optimal here!")
    else:
        print("DP: Not implemented yet")
