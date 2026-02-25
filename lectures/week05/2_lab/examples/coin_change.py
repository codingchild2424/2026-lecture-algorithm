"""Coin Change - Greedy success and failure cases."""


def coin_change_greedy(amount, coins):
    coins_sorted = sorted(coins, reverse=True)
    result = []
    remaining = amount
    for coin in coins_sorted:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin
    return result if remaining == 0 else None


def coin_change_dp(amount, coins):
    """DP solution for comparison - always optimal."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
                parent[i] = c
    if dp[amount] == float('inf'):
        return None
    result = []
    cur = amount
    while cur > 0:
        result.append(parent[cur])
        cur -= parent[cur]
    return result


if __name__ == "__main__":
    # Case 1: Greedy works
    print("=== Case 1: Standard coins ===")
    coins1, amount1 = [500, 100, 50, 10], 1260
    g1 = coin_change_greedy(amount1, coins1)
    print(f"Coins: {coins1}, Amount: {amount1}")
    print(f"Greedy: {g1} ({len(g1)} coins)")

    # Case 2: Greedy fails
    print("\n=== Case 2: Non-standard coins ===")
    coins2, amount2 = [1, 3, 4], 6
    g2 = coin_change_greedy(amount2, coins2)
    d2 = coin_change_dp(amount2, coins2)
    print(f"Coins: {coins2}, Amount: {amount2}")
    print(f"Greedy:  {g2} ({len(g2)} coins)")
    print(f"Optimal: {d2} ({len(d2)} coins)")
    print(f"-> Greedy is NOT optimal here!")
