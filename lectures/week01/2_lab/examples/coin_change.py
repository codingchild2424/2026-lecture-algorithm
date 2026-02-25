"""Coin Change - Greedy approach demonstration."""


def coin_change_greedy(amount, coins):
    """
    Greedy coin change: always pick the largest coin possible.
    Returns list of coins used.
    Note: Greedy does NOT always give optimal solution!
    """
    coins_sorted = sorted(coins, reverse=True)
    result = []
    remaining = amount

    for coin in coins_sorted:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin

    if remaining > 0:
        return None  # Cannot make exact change
    return result


if __name__ == "__main__":
    # Case 1: Greedy works (standard coins)
    coins1 = [500, 100, 50, 10]
    amount1 = 1260
    result1 = coin_change_greedy(amount1, coins1)
    print(f"Amount: {amount1}, Coins: {coins1}")
    print(f"Greedy result: {result1} ({len(result1)} coins)\n")

    # Case 2: Greedy fails (non-standard coins)
    coins2 = [1, 3, 4]
    amount2 = 6
    result2 = coin_change_greedy(amount2, coins2)
    print(f"Amount: {amount2}, Coins: {coins2}")
    print(f"Greedy result: {result2} ({len(result2)} coins)")
    print(f"Optimal: [3, 3] (2 coins) — Greedy is NOT optimal here!")
